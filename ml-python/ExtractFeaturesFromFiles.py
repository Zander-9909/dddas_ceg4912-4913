#Using the mlxtend python library, we can take a grayscale photo and
#extract certain facial landmarks from it, and overlay them onto the photo
import cv2
from datetime import datetime
import sys
import FeatureMeasurement as fm
from imutils import face_utils
import VideoThreads as vt
import dlib #required for mlxtend to function.
import time

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

def printMeasurements(shape,timeP,timeD):
    eye = shape[36:68]# Get useful facial landmarks (some are extraneous for our use, so we can ignore them.)
    avEAR.append(fm.EAR(eye)) # Calculate the Eye Aspect Ratio from FeatureMeasurement.py
    avMAR.append(fm.MAR(eye))# Calculate Mouth Aspect Ratio from FeatureMeasurement.py
    avCIR.append(fm.eyeCircularity(eye))# Calculate the Eye Circularity from FeatureMeasurement.py
    avMOE.append(fm.mouth_over_eye(eye))# Calculate the Mouth Over Eye ratio (MAR/EAR) from FeatureMeasurement.py
    timesD.append(timeD)
    timesP.append(timeP)

def video_to_frames(input_loc, output_loc):
    """Function to extract frames from input video file
    and save them as separate frames in an output directory.
    Args:
        input_loc: Input video file.
        output_loc: Output directory to save the frames.
    Returns:
        None
    """
    try:
        os.mkdir(output_loc)
    except OSError:
        pass
    # Log the time
    time_start = time.time()
    # Start capturing the feed
    cap = cv2.VideoCapture(input_loc)
    # Find the number of frames
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print ("Number of frames: ", video_length)
    count = 0
    print ("Converting video..\n")
    # Start converting the video
    while cap.isOpened():
        # Extract the frame
        ret, image = cap.read()
        if(ret):
            image = cv2.resize(image,(300,300))
            grayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)#Make grayscale
            startTime = cv2.getTickCount()
            faces = faceDetector.detectMultiScale(grayScale, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30),flags=cv2.CASCADE_SCALE_IMAGE)
            timeD = (cv2.getTickCount() - startTime)/ cv2.getTickFrequency()
            for (x, y, w, h) in faces:
                print("Face found.")
                #Grabbing bounding box coordinates for facial detection
                face = dlib.rectangle(int(x), int(y), int(x + w),int(y + h))
                startTime = cv2.getTickCount() #Starting time for prediction measurement
                shape = facePredictor(grayScale, face)
                timeP=(cv2.getTickCount() - startTime)/ cv2.getTickFrequency()
                shape = face_utils.shape_to_np(shape)
                printMeasurements(shape,timeP,timeD)
        # Write the results back to output location.
        count = count + 1
        # If there are no more frames left
        if (count > (video_length-1)):
            # Log the time again
            time_end = time.time()
            # Show the image
            file = open(path+"resultsFromFile.txt",'w')
            printAveragesToFile(file)
            os.system("clear")
            print("Saved results and video to /frames directory. Exiting.")
            file.close()
            # Release the feed
            cap.release()
            # Print stats
            print ("Done extracting frames.\n%d frames extracted" % count)
            print ("It took %d seconds forconversion." % (time_end-time_start))
            break
input_loc = '/home/zander/CEG4912-3/dddas_ceg4912-4913/ml-python/2023-10-05 17-45-37.mkv'
output_loc = '/home/zander/CEG4912-3/dddas_ceg4912-4913/ml-python/framesTEST'
video_to_frames(input_loc,output_loc)
