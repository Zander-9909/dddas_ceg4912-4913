from flask import Flask,request
from datetime import datetime
import statistics
app = Flask(__name__)
##################################
#                                #
#      Command to start Flask    #
#                                #
# flask --app BasicWebServer run #
##################################
counter = 0
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
        global counter
        global avMAR
        global avMOE
        global avCIR
        global avEAR
        global startTime
        global endTime
        counter = counter + 1       
        #server received a packet
        json = dict(request.json)

        avMOE.append(json.get("MOE"))
        avCIR.append(json.get("CIR"))
        avEAR.append(json.get("EAR"))
        avMAR.append(json.get("MAR"))

        if counter == 1:
            startTime = json.get("time")
        elif counter%10 == 0:#server has received 10 packets
            endTime = json.get("time")
            counter = 0
            print("Average of Past 10 Measurements:")
            print("Time range: "+ startTime + " -> "+endTime)
            print("MAR: "+str(statistics.mean(avMAR)))
            print("EAR: "+str(statistics.mean(avEAR)))
            print("CIR: "+str(statistics.mean(avCIR)))
            print("MOE: "+str(statistics.mean(avMOE)))
            avMAR = []
            avMOE = []
            avCIR = []
            avEAR = []
        
        return json
    else:
        return "<p>Incorrect Datatype<p>"