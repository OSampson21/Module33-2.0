import RoboPiLib as RPL
import time

RPL.RoboPiInit("/dev/ttyAMA0",115200)
list = [1,2,3]
motorR = 0
motorL = 1
theB = time.time()
sensorF = 17
sensorL = 16

while True:
  readingF = RPL.digitalRead(sensorF)
  trim = time.time() - theB
  if trim > 20:
     break
  elif readingF == 0:
     for number in list:
        RPL.servoWrite(motorR, 1600)
        time.sleep(1.5)
        RPL.servoWrite(motorR, 0)
        time.sleep(1.5)
  else:
     RPL.servoWrite(motorR, 0) 
