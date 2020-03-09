#!/usr/bin/env python
# coding: utf-8

# In[8]:


from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO
import numpy as np

from random import randrange
import os
from PIL import Image
from matplotlib.pyplot import imshow

camera = PiCamera()
camera.resolution = (256,256)
count = 0
names = []
for r, d, f in os.walk('/home/pi/Desktop/data'):
    for file in f:
        names.append(int(file[:len(file)-4]))
count = max(names) + 1

while True:

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(32, GPIO.OUT, initial = GPIO.HIGH)
    GPIO.setup(36, GPIO.OUT, initial = GPIO.LOW)

    while True:
        if(GPIO.input(36) == GPIO.HIGH):
            break

    camera.start_preview()
    sleep(2)
    camera.capture('/home/pi/Desktop/data/' + str(count) + '.jpg')
    camera.stop_preview()
    count+=1

    
    print('done')
    
GPIO.cleanup()
