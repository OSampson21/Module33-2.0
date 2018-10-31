import RoboPiLip as RPL
import time

RPL.RoboPiInit("/dev/ttyAMA0",115200)

motorR = 0
motorL = 1
AnalogSensor = 3
sensorF = 17
sensorL = 16

while True:
  readingF = RPL.digitalRead(senorF)
  readingL = RPL.digitalRead(sensorL)
  if readingF == 0 and readingL == 0:
    RPL.servoWrite(motorL, 1400)
    RPL.servoWrite(motorR, 1600)
  elif readingF == 0:
    RPL.servoWrite(motorL, 0)
    RPL.servoWrite(motorR, 1600)
  elif readingL == 0:
    RPL.servoWrite(motorL, 1600)
    RPL.servoWrite(motorR, 0)
  else:
    RPL.servoWrite(motorL, 0)
    RPL.servoWrite(motorL, 0)
