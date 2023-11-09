from flask import Flask,request
from datetime import datetime
from KthNeighbour import modelKNNWebServer
import statistics
import pandas as pd
import numpy as np
app = Flask(__name__)
##################################
#                                #
#      Command to start Flask    #
#                                #
# flask --app BasicWebServer run #
#                                #
##################################
counter = 0
first20 = False
featuresRAW = []
mean = 0
std = 0

avMAR = []
avMOE = []
avCIR = []
avEAR = []
startTime = ""
endTime = ""

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print("Data received from Webhook is: ", request.json)

        return "Webhook received!"

@app.route('/data', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = dict(request.json)
        if(json.get("type")=="facial"):
            global avMAR,avMOE,counter,avCIR,avEAR,startTime,endTime,mean,first20,std,featuresRAW

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
                rString,rProb = modelKNNWebServer(dictR, mean, std)
                result.update({"mess":rString})
                result.update({"prob":str(rProb)})
                print(dictR)
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
                rString,rProb = modelKNNWebServer(dictR, mean, std)
                result.update({"mess":rString})
                result.update({"prob":str(rProb)})
                featuresRAW = []
            return result 

        elif (json.get("type")=="ULTRAsonic"):
            #do stuff
            return json
    else:
        return "<p>Incorrect Datatype<p>"