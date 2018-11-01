import RoboPiLib as RPL
import time

RPL.RoboPiInit("/dev/ttyAMA0",115200)
motorR = 0
motorL = 1
sensorF = 17


while True:
  readingF = RPL.digitalRead(senorF)
  if readingF == 0:
     for i in range(1,3):
        RPL.servoWrite(motorR, 1600)
        time.sleep(1.5)
        RPL.servowrite(motorR, 0)
        time.sleep(1.5)
  else:
     break

RPL.servoWrite(motorR, 0) 
