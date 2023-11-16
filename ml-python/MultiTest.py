from threading import Thread
from datetime import datetime
import argparse
import cv2
import math
import sys
import FeatureMeasurement as fm
from imutils import face_utils
import dlib #required for mlxtend to function.
#p = "shape_predictor_68_face_landmarks.dat"
p = "models/shape_predictor_gtx.dat"
# ^ dlib landmark example file for it to compare to
from mlxtend.image import extract_face_landmarks
# Function to take in a photo and extract landmarks

faceDetector = dlib.get_frontal_face_detector() #dlib facial detector
facePredictor = dlib.shape_predictor(p) #dlib face shape predictor

class VideoGet:
    """
    Class that continuously gets frames from a VideoCapture object
    with a dedicated thread.
    """

    def __init__(self, src=0):
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False

    def start(self):    
        Thread(target=self.get, args=()).start()
        return self

    def get(self):
        while not self.stopped:
            if not self.grabbed:
                self.stop()
            else:
                (self.grabbed, self.frame) = self.stream.read()

    def stop(self):
        self.stopped = True

class VideoShow:
    """
    Class that continuously shows a frame using a dedicated thread.
    """

    def __init__(self, frame=None):
        self.frame = frame
        self.stopped = False

    def start(self):
        Thread(target=self.show, args=()).start()
        return self

    def show(self):
        while not self.stopped:
            cv2.imshow("Video", self.frame)
            if cv2.waitKey(250) == ord("q"):
                self.stopped = True

    def stop(self):
        self.stopped = True

class Landmarks:
    """
    Class that continuously shows a frame using a dedicated thread.
    """

    def __init__(self, frame=None):
        self.frame = frame
        self.out = frame
        self.stopped = False
        self.flag = False

    def start(self):
        Thread(target=self.extract, args=()).start()
        return self

    def extract(self):
        while not self.stopped:
            if(not self.flag):
                frame = self.frame
                grayScale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#Make grayscale
                faces = faceDetector(frame, 0)
                for(i, face) in enumerate(faces):
                    shape = facePredictor(grayScale, face)
                    shape = face_utils.shape_to_np(shape)
                    for (x,y) in shape: #For the coordinates saved in shape, extracted from the photo.
                        cv2.circle (frame, (x,y),2, (0, 0, 255),-1)
                    #draw a circle at x,y with a radius of 2, red colour
                self.out = frame
                self.flag = True

    def stop(self):
        self.stopped = True


class CountsPerSec:
    """
    Class that tracks the number of occurrences ("counts") of an
    arbitrary event and returns the frequency in occurrences
    (counts) per second. The caller must increment the count.
    """

    def __init__(self):
        self._start_time = None
        self._num_occurrences = 0

    def start(self):
        self._start_time = datetime.now()
        return self

    def increment(self):
        self._num_occurrences += 1

    def countsPerSec(self):
        elapsed_time = (datetime.now() - self._start_time).total_seconds()
        return self._num_occurrences / elapsed_time if elapsed_time > 0 else 0
    
