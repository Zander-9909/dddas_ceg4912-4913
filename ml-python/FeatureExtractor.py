from scipy.spatial import distance
import cv2
import numpy as np
import math
import os.path
import csv
import imageio
import FeatureMeasurement as fm
import matplotlib.pyplot as plt
from mlxtend.image import extract_face_landmarks

def getFrame(sec):
    start = 180000
    vidcap.set(cv2.CAP_PROP_POS_MSEC, start + sec*1000)
    hasFrames,image = vidcap.read()
    return hasFrames, image

data = []
labels = []
for j in [60]:
  for i in [10]:
    vidcap = cv2.VideoCapture('drive/My Drive/Fold5_part2/' + str(j) +'/' + str(i) + '.mp4')
    sec = 0
    frameRate = 1
    success, image  = getFrame(sec)
    count = 0
    while success and count < 240: 
          landmarks = extract_face_landmarks(image)
          if sum(sum(landmarks)) != 0:
              count += 1
              data.append(landmarks)
              labels.append([i])
              sec = sec + frameRate
              sec = round(sec, 2)
              success, image = getFrame(sec)
              print(count)
          else:  
              sec = sec + frameRate
              sec = round(sec, 2)
              success, image = getFrame(sec)
              print("not detected")
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