# main.py -- put your code here!

import pyb

led4 = pyb.LED(4)
led3 = pyb.LED(3)
led2 = pyb.LED(2)
led1 = pyb.LED(1)

sw = pyb.Switch()

intensity4 = 0
intensity3 = 0
intensity2 = 0
intensity1 = 0

led4.on()
led4.intensity(0)
led3.on()
led3.intensity(0)
led2.on()
led2.intensity(0)
led1.on()
led1.intensity(0)

while True:
    if sw():
        intensity4 = min(255, intensity4 +1)
    else:
        if intensity3 == 0:
            intensity4 = max(0, intensity4 - 1)

    if sw():
        if intensity4 == 255:
            intensity3 = min(255, intensity3 +1)
    else:
        if intensity2 == 0:
            intensity3 = max(0, intensity3 -1)

    if sw():
        if intensity3 == 255:
            intensity2 = min(255, intensity2 +1)
    else:
        if intensity1 == 0:
            intensity2 = max(0, intensity2 -1)

    if sw():
        if intensity2 == 255:
            intensity1 = min(255, intensity1 +1)
    else:
            intensity1 = max(0, intensity1 -1)
    led4.intensity(intensity4)
    led3.intensity(intensity3)
    led2.intensity(intensity2)
    led1.intensity(intensity1)
    pyb.delay(20)
