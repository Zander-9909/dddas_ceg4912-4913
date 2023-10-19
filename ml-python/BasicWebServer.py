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
            global avMAR,avMOE,counter,avCIR,avEAR,startTime,endTime

            counter = counter + 1 
            avMOE.append(json.get("MOE"))
            avCIR.append(json.get("CIR"))
            avEAR.append(json.get("EAR"))
            avMAR.append(json.get("MAR"))
            features.append([json.get("EAR"),json.get("MAR"),json.get("CIR"),json.get("MOE")])
            result = {"mess":"Got a packet"}
            if counter == 1:
                startTime = json.get("time")
                result = {"mess":"Received first packet OK"}
            elif counter%21 == 0:#server has received 20 packets
                endTime = json.get("time")
                counter = 0
                print("Stats of the last 20 Measurements:")
                print("Time range: "+ startTime + " -> "+endTime)
                print("MAR: Mean = "+str(statistics.mean(avMAR)) + ", STD = "+ str(statistics.stdev(avMAR)))
                print("EAR: Mean = "+str(statistics.mean(avEAR)) + ", STD = "+ str(statistics.stdev(avEAR)))
                print("CIR: Mean = "+str(statistics.mean(avCIR)) + ", STD = "+ str(statistics.stdev(avCIR)))
                print("MOE: Mean = "+str(statistics.mean(avMOE)) + ", STD = "+ str(statistics.stdev(avMOE)))

                result = {"mess":"****Received 20 packets OK****"}
                result.update ({"EAR": "Mean = "+str(statistics.mean(avEAR)) + ", STD = "+ str(statistics.stdev(avEAR))})
                result.update ({"CIR": "Mean = "+str(statistics.mean(avCIR)) + ", STD = "+ str(statistics.stdev(avCIR))})
                result.update ({"MOE": "Mean = "+str(statistics.mean(avMOE)) + ", STD = "+ str(statistics.stdev(avMOE))})
                result.update ({"MAR": "Mean = "+str(statistics.mean(avMAR)) + ", STD = "+ str(statistics.stdev(avMAR))})
            return result 

        elif (json.get("type")=="ULTRAsonic"):
            #do stuff
            return json
    else:
        return "<p>Incorrect Datatype<p>"