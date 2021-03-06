import RoboPiLib as RPL
import time

RPL.RoboPiInit("/dev/ttyAMA0",115200)

motorR = 0
motorL = 1

sensorF = 17
sensorL = 16

while True:
  readingF = RPL.digitalRead(sensorF)
  readingL = RPL.digitalRead(sensorL)
  if readingF == 0 and readingL == 0:
     break
  elif readingF == 0:
     RPL.servoWrite(motorL, 0)
     RPL.servoWrite(motorR, 1600)
     time.sleep(1.5)
     RPL.servoWrite(motorR, 0)
     time.sleep(1.5)
    
  elif readingL == 0:
     RPL.servoWrite(motorR, 0)
     RPL.servoWrite(motorL, 1600)
     time.sleep(1)
     RPL.servoWrite(motorL, 0)
     time.sleep(1)
  else:
    pass
    
RPL.servoWrite(motorL,0)
RPL.servoWrite(motorR,0)
