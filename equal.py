import RoboPiLib as RPL
import time

RPL.RoboPiInit("/dev/ttyAMA0",115200)

motorR = 0
motorL = 1
speedR = 1400
speedL = 2900

while True:
 analog = RPL.analogRead(3)
 if analog > 550:
    break
 elif analog > 400:
    speedL -= 10
    if speedL < 1501:
          speedL = 1501
    speedR -= 10
    if speedR < 1:
          speedR = 1
    RPL.servoWrite(motorL, speedL)
    RPL.servoWrite(motorR, speedR)
 elif analog > 300:
    RPL.servoWrite(motorL, speedL - 200)
    RPL.servoWrite(motorR, speedR - 200)
#  elif analog > 200:
#    RPL.servoWrite(motorL, speedL - 100)
#    RPL.servoWrite(motorR, speedR - 100)
 elif analog > 200:
    RPL.servoWrite(motorL, speedR)
    RPL.servoWrite(motorR, speedL)

 else:
    pass
     
RPL.servoWrite(motorL, 0)
RPL.servoWrite(motorR, 0)
