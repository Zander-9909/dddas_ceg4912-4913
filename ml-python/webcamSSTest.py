import cv2
import math
import dlib
from imutils import face_utils
from scipy.spatial import distance as dist
from datetime import datetime

camera = cv2.VideoCapture(0)#enable camera[0] as a capture device
framerate = camera.get(5) * 0.5 #Get half the frame rate
path = "/Users/RyeTo/Documents/GitHub/dddas_ceg4912-4913/ml-python/frames"
testpath = "shape_predictor_68_face_landmarks.dat"
i = 0

def face(image):
    detector = dlib.get_frontal_face_detector()
    find = detector(image,1)
    predictor = dlib.shape_predictor(testpath)
    
    #converting faces to allow the finding of eyes
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = detector(gray, 0)
    for i in faces:
            shape = predictor(gray,i)
            shape = face_utils.shape_to_np(shape)
            
    #finding face
    if ((len(find) > 0)):
        print("Face found!")
        
    #finding eye blinks
    (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
    (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
    leftEye = shape[lStart:lEnd]
    rightEye = shape[rStart:rEnd]
    leftEAR = eye_aspect_ratio(leftEye)
    rightEAR = eye_aspect_ratio(rightEye)
    if ((leftEAR+rightEAR)/2 < 0.25):
        print("Blink!")

def eye_aspect_ratio(eye):
    #vertical
	A = dist.euclidean(eye[1], eye[5])
	B = dist.euclidean(eye[2], eye[4])
	#horizontal
	C = dist.euclidean(eye[0], eye[3])
	#eye aspect ratio
	ear = (A + B) / (2.0 * C)
	return ear

while(i < 10):
    framenum = camera.get(1) #get current frame number
    return_value, image = camera.read()
    if(return_value != True):
        break;
    if(framenum % math.floor(framerate) == 0):
        now = datetime.now()

        current_time = now.strftime("%H-%M-%S")

        name = path + "/frame" + current_time+ ".png"
        cv2.imwrite(name, image)
        face(image)
        print("Captured at :" +current_time)
        i+=1

camera.release()
cv2.destroyAllWindows()