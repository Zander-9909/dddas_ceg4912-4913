import random
from flask import Flask,request
from flask import jsonify
from datetime import datetime
from KthNeighbour import modelKNNWebServer
from queue import Queue 
import pandas as pd
from queue import Queue
import numpy as np
app = Flask(__name__)
########################################################
#                                                      #
#      Command to start Flask                          #
#                                                      #
# flask --app BasicWebServer run --host=100.72.37.45   #
#                                                      #
########################################################
counter = 0
first20 = False
featuresRAW = []
alertNotification = False
mean = 0
std = 0

alertsResults = Queue(maxsize=5)
detectionResults = Queue(maxsize=10)
heartRates = Queue(maxsize=10)
lastHR = 0

avMAR = []
avMOE = []
avCIR = []
avEAR = []
startTime = ""
endTime = ""

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

def most_common(lst):
    if(len(lst)==0):
        return 0
    return max(set(lst), key=lst.count)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/webhook', methods=['GET'])
def webhook():
    if request.method == 'GET':
        global detectionResults,lastHR,alertNotification,alertsResults

        dictR = {
        'results': most_common(list(detectionResults.queue)),
        'heartrate': lastHR,
        'alert':bool(most_common(list(alertsResults.queue)))
        }
        returnVal = jsonify(dictR)
        returnVal.status_code = 200

        return returnVal

@app.route('/data', methods=['POST'])
def process_json():
    global lastHR
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = dict(request.json)
        if(json.get("type")=="facial"):
            global avMAR,avMOE,counter,avCIR,avEAR,startTime,endTime,mean,first20,std,featuresRAW,detectionResults

            counter = counter + 1 
            result = {"mess":"****Received packet****"}
            featuresRAW.append([json.get("MOE"),json.get("EAR"),json.get("MAR"),json.get("CIR")])
            if counter == 1:
                startTime = json.get("time")
            elif counter % 11 ==0 and first20: #every 10 packets, do ML
                endTime = json.get("time")
                result={}
                counter = 0
                featureNP = np.array(featuresRAW)
                x = featureNP
                y = pd.DataFrame(x, columns=["MOE","EAR","MAR","Circularity"])
                avgMeasurements = y.mean(axis=0)

                dictR = {"MOE":avgMeasurements.get("MOE"),"EAR":avgMeasurements.get("EAR"),"MAR":avgMeasurements.get("MAR"),"CIR":avgMeasurements.get("Circularity")}
                rString,rProb,iResult = modelKNNWebServer(dictR, mean, std)
                result.update({"mess":rString})
                result.update({"prob":str(rProb)})

                if not detectionResults.full():
                    detectionResults.put(iResult)
                else:
                    detectionResults.get()
                    detectionResults.put(iResult)
                #print(dictR)
                print("Detection Result: "+rString)
                print("Probabilities: "+str(rProb))
                featuresRAW = []
            elif counter%21 == 0 and not first20:#server has received the first 20 packets
                endTime = json.get("time")
                result={}
                counter = 0
                first20 = True
                featureNP = np.array(featuresRAW)
                x = featureNP
                y = pd.DataFrame(x, columns=["MOE","EAR","MAR","Circularity"])
                mean = y.mean(axis=0)
                std = y.std(axis=0)

                dictR = {"MOE":mean.get("MOE"),"EAR":mean.get("EAR"),"MAR":mean.get("MAR"),"CIR":mean.get("Circularity")}
                rString,rProb,RESULTTOUSE = modelKNNWebServer(dictR, mean, std)
                result.update({"mess":rString})
                result.update({"prob":str(rProb)})
                print(rProb)

                detectionResults.put(RESULTTOUSE)
                
                featuresRAW = []
            return result 
        elif (json.get("type")=="bpm"):
            lastHR = json.get("heartrate")
            if not heartRates.full():
                heartRates.put(json.get("heartrate"))
            else:
                heartRates.get()
                heartRates.put(json.get("heartrate"))
            
            avgHR = sum(list(heartRates.queue)) / len(list(heartRates.queue))
            
            if(avgHR <=70 and avgHR !=0) or (most_common(list(detectionResults.queue)))!=0 : 
                alertNotification = True # Set Alert Signal
            else:
                alertNotification = False # Reset Alert Signal

            if not alertsResults.full():
                alertsResults.put(alertNotification)
            else:
                alertsResults.get()
                alertsResults.put(alertNotification)
            

            dictR = {
            'rumble':bool(most_common(list(alertsResults.queue)))
            }
            returnVal = jsonify(dictR)
            returnVal.status_code = 200
            return returnVal
    else:
        return "<p>Incorrect Datatype<p>"