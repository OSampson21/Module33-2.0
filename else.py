import RoboPiLip as RPL
import time

RPL.RoboPiInit("/dev/ttyAMA0",115200)

motorR = 0
motorL = 1
AnalogSensor = 3
sensorF = 17
sensorS = 16

while True:
  readingF = digitalRead(sensorF)
  if reading F == 1:
     RPL.servoWrite(motorR, 1600)
  else:
     RPL.servoWrite(motorR, 1400)
