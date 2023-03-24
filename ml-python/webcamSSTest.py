import cv2
import math
import FacialLandmarkExtract as FLE
from datetime import datetime

camera = cv2.VideoCapture(0)#enable camera[0] as a capture device
framerate = camera.get(5) * 0.5 #Get half the frame rate
path = "/home/zander/CEG4912-3/dddas_ceg4912-4913/ml-python/frames/"

while(camera.isOpened()):
    framenum = camera.get(1) #get current frame number
    return_value, image = camera.read()
    if(return_value != True):
        break
    if(framenum % math.floor(framerate) == 0):
        now = datetime.now()

        current_time = now.strftime("%H-%M-%S.%f")

        name = path + "/frame" + current_time+ ".png"
        cv2.imwrite(name, image)
        print("Captured at :" +current_time)
del(camera)