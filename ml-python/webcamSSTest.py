import cv2
import math
from datetime import datetime

camera = cv2.VideoCapture(0)#enable camera[0] as a capture device
framerate = camera.get(5) * 0.5 #Get half the frame rate
path = "/Users/RyeTo/Documents/GitHub/dddas_ceg4912-4913/ml-python/frames"
i = 0

while(i < 100):
    framenum = camera.get(1) #get current frame number
    return_value, image = camera.read()
    if(return_value != True):
        break;
    if(framenum % math.floor(framerate) == 0):
        now = datetime.now()

        current_time = now.strftime("%H.%M.%S")

        name = path + "/frame" + current_time+ ".png"
        print(name)
        cv2.imwrite(name, image)
        print("Captured at :" +current_time)
        i+=1

camera.release()
cv2.destroyAllWindows()