#Using the mlxtend python library, we can take a grayscale photo and
#extract certain facial landmarks from it, and overlay them onto the photo
import cv2
from imutils import face_utils
import dlib #required for mlxtend to function.
p = "shape_predictor_68_face_landmarks.dat"
# ^ dlib landmark example file for it to compare to
from mlxtend.image import extract_face_landmarks
# Function to take in a photo and extract landmarks

def getLandmarks(image):
    landmarks = extract_face_landmarks(image)
    if(sum(sum(landmarks)) != 0):#if it detected a face
        return landmarks
    else: return "Could not detect a face"

def overlayLandmarks(image, shape):
    for (x,y) in shape: #For the coordinates saved in shape, extracted from the photo.
        cv2.circle (image, (x,y),2, (0, 255, 0),-1)
        #draw a circle at x,y with a radius of 2, green colour
camera = cv2.VideoCapture(0)
image = camera.read() #Get frame from camera
grayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)#Make grayscale

faceDetector = dlib.get_frontal_face_detection(image, 0) #dlib facial detector
facePredictor = dlib.shape_predictor(p) #dlib face shape predictor

faceList = faceDetector(image, 0)
for(i, face) in enumerate(faceList):
    shape = facePredictor(grayScale, face)
    shape = face_utils.shape_ti_np(shape)
    landmarks = getLandmarks(shape)
    overlayLandmarks(image,shape)

    path = "/home/zander/CEG4912-3/dddas_ceg4912-4913/ml-python/frames/"

    name = path + "/frame/face"+str(i)+ ".png"
    cv2.imwrite(name, image)
