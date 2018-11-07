import RoboPiLib as RPL
import time

RPL.RoboPiInit("/dev/ttyAMA0",115200)
motorR = 0
motorL = 1
sensorF = 17


while True:
  readingF = RPL.digitalRead(sensorF)
  if readingF == 0:
     for i in range(0,3):
        RPL.servoWrite(motorR, 1600)
        time.sleep(1.5)
        RPL.servoWrite(motorR, 0)
        time.sleep(1.5)
  else:
     break

RPL.servoWrite(motorR, 0) 
