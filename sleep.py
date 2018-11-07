import RoboPiLib as RPL
import time

RPL.RoboPiInit("/dev/ttyAMA0",115200)

motorR = 0
motorL = 1
AnalogSensor = 3
sensorF = 17
sensorL = 16

while True:
  readingF = RPL.digitalRead(sensorF)
  readingL = RPL.digitalRead(sensorL)
  if readingL == 0:
     RPL.servoWrite(motorL, 1600)
     time.sleep(1)
     RPL.servoWrite(motorL, 0)
     time.sleep(1)
  else:
     break
     
RPL.servoWrite(motorR, 0)

