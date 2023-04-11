from threading import Thread
from datetime import datetime
import argparse
import cv2
import math
import sys
import FeatureMeasurement as fm
from imutils import face_utils
import dlib #required for mlxtend to function.
p = "shape_predictor_68_face_landmarks.dat"
#p = "models/shape_predictor_gtx.dat"
# ^ dlib landmark example file for it to compare to
from mlxtend.image import extract_face_landmarks
# Function to take in a photo and extract landmarks

from MultiTest import CountsPerSec
from MultiTest import VideoGet
from MultiTest import VideoShow
from MultiTest import Landmarks

import os
faceDetector = dlib.get_frontal_face_detector() #dlib facial detector
facePredictor = dlib.shape_predictor(p) #dlib face shape predictor

avEAR,avMAR, avCIR, avMOE = [],[],[],[]
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
    print("MOE: "+str(avMOE[len(avMOE)-1])+"\n")
    print("Press q to exit.")

def extractLandmarks(frameE):
    grayScale = cv2.cvtColor(frameE, cv2.COLOR_BGR2GRAY)#Make grayscale
    faces = faceDetector(frameE, 0)
    for(i, face) in enumerate(faces):
        shapeE = facePredictor(grayScale, face)
        shapeE = face_utils.shape_to_np(shapeE)
        for (x,y) in shapeE: #For the coordinates saved in shape, extracted from the photo.
            cv2.circle (frameE, (x,y),2, (0, 0, 255),-1)
        #draw a circle at x,y with a radius of 2, red colour
    return shapeE,frameE

def putIterationsPerSec(frame, iterations_per_sec):
    """
    Add iterations per second text to lower-left corner of a frame.
    """

    cv2.putText(frame, "{:.0f} iterations/sec".format(iterations_per_sec),
        (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255))
    return frame

def noThreading(source=0):
    """Grab and show video frames without multithreading."""

    cap = cv2.VideoCapture(source)
    cps = CountsPerSec().start()
    (grabbed, frame) = cap.read()
    landmarker = Landmarks(frame).start()

    while True:
        startTime = cv2.getTickCount()
        grabbed, frame = cap.read()
        if not grabbed:
            landmarker.stop()
            break       
        
        landmarker.frame = frame
        
        if(landmarker.flag):
            time = (cv2.getTickCount() - startTime)/ cv2.getTickFrequency()
            print(time)
            out = landmarker.out
            out = putIterationsPerSec(out, cps.countsPerSec())        
            cv2.imshow("Video", out)
            if cv2.waitKey(1) == ord("q"):
                landmarker.stop()
                break
            cps.increment()
            landmarker.flag = False

def threadVideoGet(source=0):
    """
    Dedicated thread for grabbing video frames with VideoGet object.
    Main thread shows video frames.
    """

    video_getter = VideoGet(source).start()
    cps = CountsPerSec().start()

    while True:
        if (cv2.waitKey(1) == ord("q")) or video_getter.stopped:
            video_getter.stop()
            break

        frame = video_getter.frame
        (shape,frame) = extractLandmarks(frame)
        if(type(shape)!=None):
            printMeasurements(shape)
            frame = putIterationsPerSec(frame, cps.countsPerSec())
        cv2.imshow("Video", frame)
        cps.increment()

def threadVideoShow(source=0):
    """
    Dedicated thread for showing video frames with VideoShow object.
    Main thread grabs video frames.
    """

    cap = cv2.VideoCapture(source)
    (grabbed, frame) = cap.read()
    video_shower = VideoShow(frame).start()
    cps = CountsPerSec().start()

    while True:
        (grabbed, frame) = cap.read()
        if not grabbed or video_shower.stopped:
            video_shower.stop()
            break

        (shape,frame) = extractLandmarks(frame)
        if(type(shape)!=None):
            printMeasurements(shape)
            frame = putIterationsPerSec(frame, cps.countsPerSec())
        video_shower.frame = frame
        cps.increment()

def threadBoth(source=0):
    """
    Dedicated thread for grabbing video frames with VideoGet object.
    Dedicated thread for showing video frames with VideoShow object.
    Main thread serves only to pass frames between VideoGet and
    VideoShow objects/threads.
    """

    video_getter = VideoGet(source).start()
    video_shower = VideoShow(video_getter.frame).start()
    cps = CountsPerSec().start()

    while True:
        if video_getter.stopped or video_shower.stopped:
            video_shower.stop()
            video_getter.stop()
            break

        frame = video_getter.frame
        (shape,frame) = extractLandmarks(frame)
        if(type(shape)!=None):
            printMeasurements(shape)
            frame = putIterationsPerSec(frame, cps.countsPerSec())
        video_shower.frame = frame 
        cps.increment()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", "-s", default=0,
        help="Path to video file or integer representing webcam index"
            + " (default 0).")
    ap.add_argument("--thread", "-t", default="none",
        help="Threading mode: get (video read in its own thread),"
            + " show (video show in its own thread), both"
            + " (video read and video show in their own threads),"
            + " none (default--no multithreading)")
    args = vars(ap.parse_args())

    # If source is a string consisting only of integers, check that it doesn't
    # refer to a file. If it doesn't, assume it's an integer camera ID and
    # convert to int.
    if (
        isinstance(args["source"], str)
        and args["source"].isdigit()
        and not os.path.isfile(args["source"])
    ):
        args["source"] = int(args["source"])

    if args["thread"] == "both":
        threadBoth(args["source"])
    elif args["thread"] == "get":
        threadVideoGet(args["source"])
    elif args["thread"] == "show":
        threadVideoShow(args["source"])
    else:
        noThreading(args["source"])

if __name__ == "__main__":
    main()