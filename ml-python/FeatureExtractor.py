from scipy.spatial import distance
import cv2
import numpy as np
import math
import os.path
import csv
import dlib #required for mlxtend to function.
import imageio
import FeatureMeasurement as fm
import matplotlib.pyplot as plt
from mlxtend.image import extract_face_landmarks
from imutils import face_utils

def getFrame(sec):
    start = 180000
    vidcap.set(cv2.CAP_PROP_POS_MSEC, start + sec*1000)
    hasFrames,image = vidcap.read()
    return hasFrames, image

cwd = os.getcwd()
p = cwd + "/ml-python/models/shape_predictor_gtx.dat"
d = cwd + "/ml-python/models/haarcascade_frontalface_default.xml"

faceDetector = cv2.CascadeClassifier(d) # Using lighter weight Haar cascade face detector
facePredictor = dlib.shape_predictor(p) #dlib face shape predictor

path = cwd+'/dataset/Fold1_part1/0'

#fileExtensions = [[".mov",".mov",".mov"],[".mov",".MOV",".MOV"],[".mov",".mov",".mov"],[".mp4",".mp4",".mp4"],[".MOV",".MOV",".MOV"],[".mp4",".mp4",".mp4"]]

numsI = [0,5,10]
numsJ = [1,2]

data = []
labels = []
for j in numsJ:
  personIndex = 0
  for i in numsI:
    
    print("Starting "+str(j)+" - "+str(i))
    currPath = path + str(j) +'/' + str(i)+".mp4"
    '''if j == 6 or j == 4:
        currPath += '.mp4'
    else:
        currPath += '.mov'''
    print(currPath)
    vidcap = cv2.VideoCapture(currPath)

    sec = 0
    frameRate = 1
    success, image  = getFrame(sec)
    count = 0
    while success and count < 240: 
        try:
            #image=cv2.resize(image,(800,800))
            grayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)#Make grayscale
            faces = faceDetector.detectMultiScale(grayScale,scaleFactor=1.05, minNeighbors=5, minSize=(30, 30),flags=cv2.CASCADE_SCALE_IMAGE)
            for (x, y, w, h) in faces:
                #Grabbing bounding box coordinates for facial detection
                face = dlib.rectangle(int(x), int(y), int(x + w),int(y + h))
                shape = facePredictor(image, face)
                shape = face_utils.shape_to_np(shape)
                count += 1
                data.append(shape)
                labels.append([i])
                sec = sec + frameRate
                sec = round(sec, 2)
                print("Face found: "+str(count))
                success, image = getFrame(sec)
        except Exception: 
            print("error, moving on")
            sec = sec + frameRate
            sec = round(sec, 2)
            success, image = getFrame(sec)
    personIndex +=1
              
data = np.array(data)
labels = np.array(labels)
features = []
for d in data:
    eye = d[36:68]
    ear = fm.EAR(eye)
    mar = fm.MAR(eye)
    moe = fm.mouth_over_eye(eye)
    cir = fm.mouth_over_eye(eye)
    features.append([ear,mar,cir,moe])
features = np.array(features)
#features.shape = (240,4)
# data.shape = (240, 68, 2)
# labels.shape = (240,1)
np.savetxt("Fold5_part2_features_60_10.csv", features, delimiter = ",")
np.savetxt("Fold5_part2_labels_60_10.csv", labels, delimiter = ",")