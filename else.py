import RoboPiLib as RPL
import time

RPL.RoboPiInit("/dev/ttyAMA0",115200)

motorR = 0
motorL = 1
AnalogSensor = 3
sensorF = 17
sensorS = 16

while True:
  readingF = RPL.digitalRead(sensorF)
  if readingF == 1:
     RPL.servoWrite(motorR, 1600)
  else:
     RPL.servoWrite(motorR, 1400)
