import RoboPiLib as RPL
import time

RPL.RoboPiInit("/dev/ttyAMA0",115200)

motorR = 0
motorL = 1
sensorF = 17
sensorS = 16
n = 0

while True:
  if RPL.digitalRead(sensorF) == 0:
     RPL.servoWrite(motorR, 1600)
     time.sleep(1)
     RPL.servoWrite(motorR, 0)
     time.sleep(1)
     n += 1
     print("The motor has pulsed " + str(n) + " times.")
  else:
     pass
