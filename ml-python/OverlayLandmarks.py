#Using the mlxtend python library, we can take a grayscale photo and
#extract certain facial landmarks from it, and overlay them onto the photo
import cv2
import FeatureMeasurement as fm
from imutils import face_utils
import dlib #required for mlxtend to function.
p = "shape_predictor_68_face_landmarks.dat"
# ^ dlib landmark example file for it to compare to
from mlxtend.image import extract_face_landmarks
# Function to take in a photo and extract landmarks
import os
path = "/home/zander/CEG4912-3/dddas_ceg4912-4913/ml-python/frames/"

faceDetector = dlib.get_frontal_face_detector() #dlib facial detector
facePredictor = dlib.shape_predictor(p) #dlib face shape predictor

def getLandmarks(image):
    landmarks = extract_face_landmarks(image)
    if(sum(sum(landmarks)) != 0):#if it detected a face
        return landmarks
    else: return "Could not detect a face"

def printMeasurements(shape):
    eye = shape[36:68]
    print("EAR: "+str(fm.EAR(eye))+"\n")
    print("MAR: "+str(fm.MAR(eye))+"\n")
    print("eyeCircularity: "+str(fm.eyeCircularity(eye))+"\n")
    print("mouth_over_eye: "+str(fm.mouth_over_eye(eye))+"")

camera = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(path+'output.avi', fourcc, 10.0, (1280, 720))
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
            #draw a circle at x,y with a radius of 2, green colour
            os.system("clear")
            printMeasurements(shape)
            #name = path + "face"+str(i)+ ".png"
            #cv2.imwrite(name, image)
        # Show the image
        image = cv2.resize(image,(1280,720))
        out.write(image)
        
        cv2.imshow("Image",image)
        if cv2.waitKey(1) & 0xFF == 27:
            break
camera.release()
out.release()  
cv2.destroyAllWindows()
