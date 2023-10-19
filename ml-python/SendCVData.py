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

p = "ml-python/models/shape_predictor_gtx.dat"
d = "ml-python/models/haarcascade_frontalface_default.xml"

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
file = open(path+"results.txt",'w')

def calibration(detector, predictor, cap = cv2.VideoCapture(0)):
    """Helper function for determing mean and std"""
    
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (10,400)
    fontScale              = 1
    fontColor              = (255,255,255)
    lineType               = 2
    data = []
    cap = cap

    while True:
        # Getting out image by webcam 
        _, image = cap.read()
        # Converting the image to gray scale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Get faces into webcam's image
        rects = detector(image, 0)

        # For each detected face, find the landmark.
        for (i, rect) in enumerate(rects):
            # Make the prediction and transfom it to numpy array
            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)
            data.append(shape)
            cv2.putText(image,"Calibrating...", bottomLeftCornerOfText, font, fontScale, fontColor,lineType)

            # Draw on our image, all the finded cordinate points (x,y) 
            for (x, y) in shape:
                cv2.circle(image, (x, y), 2, (0, 255, 0), -1)

        # Show the image
        cv2.imshow("Output", image)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

    cv2.destroyAllWindows()
    cap.release()
    
    features_test = []
    for d in data:
        eye = d[36:68]
        ear = fm.EAR(eye)
        mar = fm.MAR(eye)
        cir = fm.eyeCircularity(eye)
        mouth_eye = fm.mouth_over_eye(eye)
        features_test.append([ear, mar, cir, mouth_eye])
    
    features_test = np.array(features_test)
    x = features_test
    y = pd.DataFrame(x, columns=["EAR","MAR","Circularity","MOE"])
    df_means = y.mean(axis=0)
    df_std = y.std(axis=0)
    
    return df_means, df_std

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


def liveDemo(delay,camNum,height, width):
    camera = cv2.VideoCapture(camNum)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(path+'/output.avi', fourcc, 15.0, (width, height))
    
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




