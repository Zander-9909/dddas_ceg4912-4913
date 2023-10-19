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
##################################
counter = 0
first20 = False
features = []
df_means = 0
df_std = 0

avMAR = []
avMOE = []
avCIR = []
avEAR = []
startTime = ""
endTime = ""

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/data', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = dict(request.json)
        if(json.get("type")=="facial"):
            global avMAR
            global avMOE
            global counter
            global avCIR
            global avEAR
            global startTime
            global endTime
            global first20
            global df_means
            global df_std

            counter = counter + 1 
            avMOE.append(json.get("MOE"))
            avCIR.append(json.get("CIR"))
            avEAR.append(json.get("EAR"))
            avMAR.append(json.get("MAR"))
            features.append([json.get("EAR"),json.get("MAR"),json.get("CIR"),json.get("MOE")])

            if counter == 1:
                startTime = json.get("time")
            elif counter%20 == 0 and not first20:#server has received 20 packets
                first20 = True
                endTime = json.get("time")
                counter = 0
                print("Stats of the first 20 Measurements:")
                print("Time range: "+ startTime + " -> "+endTime)
                print("MAR: Mean = "+str(statistics.mean(avMAR)) + ", STD = "+ str(statistics.stdev(avMAR)))
                print("EAR: Mean = "+str(statistics.mean(avEAR)) + ", STD = "+ str(statistics.stdev(avEAR)))
                print("CIR: Mean = "+str(statistics.mean(avCIR)) + ", STD = "+ str(statistics.stdev(avCIR)))
                print("MOE: Mean = "+str(statistics.mean(avMOE)) + ", STD = "+ str(statistics.stdev(avMOE)))
                
                features = np.array(features)
                x = features
                y = pd.DataFrame(x, columns=["EAR","MAR","Circularity","MOE"])
                df_means = y.mean(axis=0)
                df_std = y.std(axis=0)

                avMAR = []
                avMOE = []
                avCIR = []
                avEAR = []
                result = modelKNNWebServer(json,df_means,df_std)
            elif counter % 20 and first20:
                endTime = json.get("time")
                counter = 0
                print("Stats of the last 10 Measurements:")
                print("Time range: "+ startTime + " -> "+endTime)
                print("MAR: Mean = "+str(statistics.mean(avMAR)) + ", STD = "+ str(statistics.stdev(avMAR)))
                print("EAR: Mean = "+str(statistics.mean(avEAR)) + ", STD = "+ str(statistics.stdev(avEAR)))
                print("CIR: Mean = "+str(statistics.mean(avCIR)) + ", STD = "+ str(statistics.stdev(avCIR)))
                print("MOE: Mean = "+str(statistics.mean(avMOE)) + ", STD = "+ str(statistics.stdev(avMOE)))
                avMAR = []
                avMOE = []
                avCIR = []
                avEAR = []
            return result 

        elif (json.get("type")=="ULTRAsonic"):
            #do stuff
            return json
    else:
        return "<p>Incorrect Datatype<p>"