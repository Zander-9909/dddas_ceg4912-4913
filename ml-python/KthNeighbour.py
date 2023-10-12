import dlib
import cv2
from imutils import face_utils
from scipy.spatial import distance
import math
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# This is taken from https://github.com/sandyying/APM-Drowsiness-Detection/blob/master/Live%20Demo.ipynb
def average (y_pred):
    for i in range(len(y_pred)):
        if i % 240 == 0 or (i+1) % 240 == 0:
            pass
        else:
            average = float(y_pred[i-1] +  y_pred[i] + y_pred[i+1])/3
            if average >= 0.5:
                y_pred = 1
            else:
                y_pred = 0
    return y_pred

