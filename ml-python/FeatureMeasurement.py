import numpy 
import math
from scipy.spatial import distance
# ^Must install with apt-get 

#defines
#Eye aspect ratio using the scipy library
#As you get drowsy, this should decrease (eyes more closer)
def EAR(eye): #numpy array
    leftVert = distance.euclidean(eye[1],eye[5])
    rightVert = distance.euclidean(eye[2],eye[4])
    horiz = distance.euclidean(eye[0],eye[3])
    return (leftVert + rightVert)/(2 * horiz)

#Mouth aspect ratio, using scipy similar to above
#As you get drowsy, this should increase (yawning)
def MAR(mouth): #numpy array
    vertical = distance.euclidean(mouth[14],mouth[18])
    horizontal = distance.euclidean(mouth[12],mouth[16])
    return vertical/horizontal

def eyeCircularity(eye):
    A = distance.euclidean(eye[1], eye[4])
    radius  = A/2.0
    Area = math.pi * (radius ** 2)
    p = 0
    p += distance.euclidean(eye[0], eye[1])
    p += distance.euclidean(eye[1], eye[2])
    p += distance.euclidean(eye[2], eye[3])
    p += distance.euclidean(eye[3], eye[4])
    p += distance.euclidean(eye[4], eye[5])
    p += distance.euclidean(eye[5], eye[0])
    return 4 * math.pi * Area /(p**2)

def mouth_over_eye(eye):
    ear = EAR(eye)
    mar = MAR(eye)
    mouth_eye = mar/ear
    return mouth_eye