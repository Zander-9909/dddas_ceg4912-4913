#Using the mlxtend python library, we can take a grayscale photo and
#extract certain facial landmarks from it, and overlay them onto the photo
import cv2
from datetime import datetime
import sys
import FeatureMeasurement as fm
from imutils import face_utils
import VideoThreads as vt
import dlib #required for mlxtend to function.

#p = "shape_predictor_68_face_landmarks.dat"
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

#faceDetector = dlib.get_frontal_face_detector() #dlib facial detector
faceDetector = cv2.CascadeClassifier(d) # Using lighter weight Haar cascade face detector
facePredictor = dlib.shape_predictor(p) #dlib face shape predictor

def printAveragesToFile(file):
    file.write("Val:\tMean\t Max\t Min\n")
    file.write("EAR:\t"+str(round(sum(avEAR)/len(avEAR),4))+"\t"+str(round(max(avEAR),4))+"\t"+str(round(min(avEAR),4))+"\n")
    file.write("MAR:\t"+str(round(sum(avMAR)/len(avMAR),4))+"\t"+str(round(max(avMAR),4))+"\t"+str(round(min(avMAR),4))+"\n")
    file.write("CIR:\t"+str(round(sum(avCIR)/len(avCIR),4))+"\t"+str(round(max(avCIR),4))+"\t"+str(round(min(avCIR),4))+"\n")
    file.write("MOE:\t"+str(round(sum(avMOE)/len(avMOE),4))+"\t"+str(round(max(avMOE),4))+"\t"+str(round(min(avMOE),4))+"\n")
    file.write("TTP:\t"+str(round(sum(timesP)/len(timesP),4))+"\t"+str(round(max(timesP),4))+"\t"+str(round(min(timesP),4))+"\n")
    file.write("TTD:\t"+str(round(sum(timesD)/len(timesD),4))+"\t"+str(round(max(timesD),4))+"\t"+str(round(min(timesD),4))+"\n")
    file.write("TTC:\t"+str(round(sum(timesC)/len(timesC),4))+"\t"+str(round(max(timesC),4))+"\t"+str(round(min(timesC),4))+"\n")

def printMeasurements(shape,timeP,timeD):
    eye = shape[36:68]# Get useful facial landmarks (some are extraneous for our use, so we can ignore them.)
    avEAR.append(fm.EAR(eye)) # Calculate the Eye Aspect Ratio from FeatureMeasurement.py
    avMAR.append(fm.MAR(eye))# Calculate Mouth Aspect Ratio from FeatureMeasurement.py
    avCIR.append(fm.eyeCircularity(eye))# Calculate the Eye Circularity from FeatureMeasurement.py
    avMOE.append(fm.mouth_over_eye(eye))# Calculate the Mouth Over Eye ratio (MAR/EAR) from FeatureMeasurement.py
    timesD.append(timeD)
    timesP.append(timeP)

    os.system("clear")
    print("EAR: "+str(avEAR[len(avEAR)-1])+"\n")
    print("MAR: "+str(avMAR[len(avMAR)-1])+"\n")
    print("EyeCirc: "+str(avCIR[len(avCIR)-1])+"\n")
    print("MOE: "+str(avMOE[len(avMOE)-1])+"\n")
    print("TTD: "+str(timeD)+"\n")
    print("TTP: "+str(timeP)+"\n")
    print("Press ESC to exit.")

def liveDemo(delay,camNum,height, width):
    camera = cv2.VideoCapture(camNum)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(path+'/output.avi', fourcc, 15.0, (width, height))
    
    while True:
        startC = cv2.getTickCount()
        succ, image = camera.read()
        if(succ):
            image = cv2.resize(image,(width,height))
            grayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)#Make grayscale
            startTime = cv2.getTickCount()
            faces = faceDetector(image, 0)
            timeD = (cv2.getTickCount() - startTime)/ cv2.getTickFrequency()
            for(i, face) in enumerate(faces):
                startTime = cv2.getTickCount()
                shape = facePredictor(grayScale, face)
                timeP=(cv2.getTickCount() - startTime)/ cv2.getTickFrequency()
                shape = face_utils.shape_to_np(shape)
                for (x,y) in shape: #For the coordinates saved in shape, extracted from the photo.
                    cv2.circle (image, (x,y),2, (0, 0, 255),-1)
                #draw a circle at x,y with a radius of 2, red colour
                printMeasurements(shape,timeP,timeD)
            # Show the image
            out.write(image)
            
            cv2.imshow("Live feed",image)
            if cv2.waitKey(delay) & 0xFF == 27:
                break
            timeC =(cv2.getTickCount() - startC)/ cv2.getTickFrequency()
            timesC.append(timeC)
    file = open(path+"results.txt",'w')
    printAveragesToFile(file)
    os.system("clear")
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