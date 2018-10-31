import RoboPiLip as RPL
import time

RPL.RoboPiInit("/dev/ttyAMA0",115200)

motorR = 0
motorL = 1
AnalogSensor = 3
sensorF = 17
sensorS = 16

while True:
  readingF = RPL.digitalRead(senorF)
  readingS = RPL. digitalRead(sensorF)
  if readingS == 0 or readingS == 0:
     RPL.servoWrite(motorR, 1900)
  else:
     RPL.servoWrite(motorR, 0)
  
  
