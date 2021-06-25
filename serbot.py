import cv2
import BlynkLib
from pop import Camera
import time
from pop import Util
from pop import Pilot

BLYNK_AUTH = 'kgBfMVhaOcl3nHbYmPfwB90DrEDIfZmy'
blynk = BlynkLib.Blynk(BLYNK_AUTH)  # server = '10.10.11.57, port=9443
	
Util.enable_imshow()

# cam = Util.gstrmer(width=640, height=480)

# camera = cv2.VideoCapture(cam, cv2.CAP_GSTREAMER).Camera.isOpened()
# print("Not found camera")
# width = camera.get(cv2.CAP_PROP_FRAME_WIDTH)

bot = Pilot.SerBot()

speed = 50



@blynk.VIRTUAL_WRITE(1)             # 조이스틱(x축)
def joystick1(n):
    global x_pos
    if int(n[0]) < 500:
        bot.move(270, speed)
    elif int(n[0]) > 520:
        bot.move(90, speed)
    else:
        bot.stop()

     

@blynk.VIRTUAL_WRITE(2)             # 조이스틱(y축)
def joystick2(n):
    global y_pos
    if int(n[0]) < 500:
        bot.move(180, speed)
    elif int(n[0]) > 520:
        bot.move(0, speed)
    else:
        bot.stop()
    
@blynk.VIRTUAL_WRITE(3)               # 카메라
def cameraaa(n):
    if int(n[0])==1:
        # print(n)
        cam = Camera(width=1080, height=720)
        cv2.imwrite("picture.png", cam.value)
        imgColor = cv2.imread("picture.png", cv2.IMREAD_COLOR)
        imgColor = cv2.flip(imgColor,-1)
        cv2.imwrite("picture.png", imgColor)
        #cv2.imshow("imgColor", imgColor)


while True:
    blynk.run()


    

