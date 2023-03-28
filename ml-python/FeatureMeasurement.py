import numpy 
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