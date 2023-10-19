import requests
import cv2
from datetime import datetime
import sys
import pandas as pd
import numpy as np
import FeatureMeasurement as fm
from imutils import face_utils
import VideoThreads as vt
import dlib #required for mlxtend to function.

p = "models/shape_predictor_gtx.dat"
d = "models/haarcascade_frontalface_default.xml"

# ^ dlib landmark example file for it to compare to
from mlxtend.image import extract_face_landmarks
# Function to take in a photo and extract landmarks
import os

avEAR,avMAR, avCIR, avMOE, timesP, timesD,timesC = [],[],[],[],[],[],[]
if not os.path.exists('frames'):
    os.mkdir('frames/')
path = os.path.dirname(__file__)
path = os.path.join(path, 'frames/')

faceDetector = cv2.CascadeClassifier(d) # Using lighter weight Haar cascade face detector
facePredictor = dlib.shape_predictor(p) #dlib face shape predictor
file = open(path+"resultsRemote.txt",'w')

def postMeasurements(shape):
    eye = shape[36:68]# Get useful facial landmarks (some are extraneous for our use, so we can ignore them.)
    EAR = fm.EAR(eye)# Calculate the Eye Aspect Ratio from FeatureMeasurement.py
    MAR = fm.MAR(eye)# Calculate Mouth Aspect Ratio from FeatureMeasurement.py
    CIR = fm.eyeCircularity(eye)# Calculate the Eye Circularity from FeatureMeasurement.py
    MOE = fm.mouth_over_eye(eye)# Calculate the Mouth Over Eye ratio (MAR/EAR) from FeatureMeasurement.py
    dict = {
        "type":"facial",
        "time": str(datetime.now()),
        "MOE": MOE,
        "MAR": MAR,
        "EAR": EAR,
        "CIR": CIR}
    request = requests.post("http://127.0.0.1:5000/data", json=dict)
    file.write(str(request.json())+"\n")
    for entry in request.json():
        if(entry == "mess"):
            if(request.json().get(entry) != "Got a packet"):
                print(request.json().get(entry)+"\n")
        else:
            print(entry + ": "+request.json().get(entry)+"\n")



def liveDemo(delay,camNum,height, width):
    camera = cv2.VideoCapture(camNum)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(path+'/outputRemote.avi', fourcc, 15.0, (width, height))
    
    while True:
        succ, image = camera.read()
        if(succ):
            image = cv2.resize(image,(width,height))
            grayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)#Make grayscale
            faces = faceDetector.detectMultiScale(grayScale, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30),flags=cv2.CASCADE_SCALE_IMAGE)
            for (x, y, w, h) in faces:
                #Grabbing bounding box coordinates for facial detection
                face = dlib.rectangle(int(x), int(y), int(x + w),int(y + h))
                shape = facePredictor(grayScale, face)
                shape = face_utils.shape_to_np(shape)
                for (x,y) in shape: #For the coordinates saved in shape, extracted from the photo.
                    cv2.circle (image, (x,y),2, (0, 0, 255),-1)
                #draw a circle at x,y with a radius of 2, red colour
                postMeasurements(shape)
            # Show the image
            out.write(image)
            
            cv2.imshow("Live feed",image)
            if cv2.waitKey(delay) & 0xFF == 27:
                break
    print("Saved results and video to /frames directory. Exiting.")
    file.close()
    camera.release()
    out.release()  
    cv2.destroyAllWindows()

#main
#Arguments are [period of pictures, in ms][0 for default camera, 2 for secondary (if on laptop)]

if(len(sys.argv) == 5):
    print('hmm')
    liveDemo(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
else:
    print("No parameters set, running at 10ms and default camera.")
    liveDemo(10,0,480,640)




