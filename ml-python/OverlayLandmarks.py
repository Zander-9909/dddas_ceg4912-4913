#Using the mlxtend python library, we can take a grayscale photo and
#extract certain facial landmarks from it, and overlay them onto the photo
import cv2
import math
import FeatureMeasurement as fm
from imutils import face_utils
import dlib #required for mlxtend to function.
p = "shape_predictor_68_face_landmarks.dat"
# ^ dlib landmark example file for it to compare to
from mlxtend.image import extract_face_landmarks
# Function to take in a photo and extract landmarks
import os

avEAR,avMAR, avCIR, avMOE = [],[],[],[]
if not os.path.exists('frames'):
    os.mkdir('frames/')
path = os.path.dirname(__file__)
path = os.path.join(path, 'frames/')
#path = "/home/zander/CEG4912-3/dddas_ceg4912-4913/ml-python/frames/"

faceDetector = dlib.get_frontal_face_detector() #dlib facial detector
facePredictor = dlib.shape_predictor(p) #dlib face shape predictor

def getLandmarks(image):
    landmarks = extract_face_landmarks(image)
    if(sum(sum(landmarks)) != 0):#if it detected a face
        return landmarks
    else: return "Could not detect a face"

def printAveragesToFile(file):
    file.write("Val:\tMean\t Max\t Min\n")
    file.write("EAR:\t"+str(round(sum(avEAR)/len(avEAR),5))+"\t"+str(round(max(avEAR),5))+"\t"+str(round(min(avEAR),5))+"\n")
    file.write("MAR:\t"+str(round(sum(avMAR)/len(avMAR),5))+"\t"+str(round(max(avMAR),5))+"\t"+str(round(min(avMAR),5))+"\n")
    file.write("CIR:\t"+str(round(sum(avCIR)/len(avCIR),5))+"\t"+str(round(max(avCIR),5))+"\t"+str(round(min(avCIR),5))+"\n")
    file.write("MOE:\t"+str(round(sum(avMOE)/len(avMOE),5))+"\t"+str(round(max(avMOE),5))+"\t"+str(round(min(avMOE),5))+"\n")

def printMeasurements(shape):
    eye = shape[36:68]# Get useful facial landmarks (some are extraneous for our use, so we can ignore them.)
    avEAR.append(fm.EAR(eye)) # Calculate the Eye Aspect Ratio from FeatureMeasurement.py
    avMAR.append(fm.MAR(eye))# Calculate Mouth Aspect Ratio from FeatureMeasurement.py
    avCIR.append(fm.eyeCircularity(eye))# Calculate the Eye Circularity from FeatureMeasurement.py
    avMOE.append(fm.mouth_over_eye(eye))# Calculate the Mouth Over Eye ratio (MAR/EAR) from FeatureMeasurement.py

    os.system("clear")
    print("EAR: "+str(avEAR[len(avEAR)-1])+"\n")
    print("MAR: "+str(avMAR[len(avMAR)-1])+"\n")
    print("EyeCirc: "+str(avCIR[len(avCIR)-1])+"\n")
    print("MOE: "+str(avMOE[len(avMOE)-1])+"")
camera = cv2.VideoCapture(2)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(path+'/output.avi', fourcc, 20.0, (1280, 720))
while True:
    succ, image = camera.read()
    if(succ):
        grayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)#Make grayscale
        faces = faceDetector(image, 0)
        for(i, face) in enumerate(faces):
            shape = facePredictor(grayScale, face)
            shape = face_utils.shape_to_np(shape)
            #landmarks = getLandmarks(shape)
            for (x,y) in shape: #For the coordinates saved in shape, extracted from the photo.
                cv2.circle (image, (x,y),2, (0, 0, 255),-1)
            #draw a circle at x,y with a radius of 2, red colour
            printMeasurements(shape)
            #name = path + "face"+str(i)+ ".png"
            #cv2.imwrite(name, image)
        # Show the image
        image = cv2.resize(image,(1280,720))
        out.write(image)
        
        cv2.imshow("Live feed",image)
        if cv2.waitKey(1) & 0xFF == 27:
            break
file = open(path+"results.txt",'w')
printAveragesToFile(file)
file.close()
camera.release()
out.release()  
cv2.destroyAllWindows()
