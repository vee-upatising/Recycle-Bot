#!/usr/bin/env python
# coding: utf-8

# In[8]:


from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO
import numpy as np
import tensorflow as tf
from keras.models import load_model
from random import randrange
import os
from PIL import Image
from matplotlib.pyplot import imshow

def names(number):
    if(number == 0):
        return 'Dog'
    else:
        return 'Cat'

model = load_model('trash.h5')

camera = PiCamera()
camera.resolution = (256,256)

print('Start Up Completed')

while True:

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(32, GPIO.OUT, initial = GPIO.HIGH)
    GPIO.setup(36, GPIO.OUT, initial = GPIO.LOW)
    p = GPIO.PWM(12,50)

    while True:
        if(GPIO.input(36) == GPIO.HIGH):
            break

    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()


    img = Image.open(r'/home/pi/Desktop/image.jpg')
    #x = np.array(img.resize((128,128)))
    x = np.array(img)
    x = x.reshape(1,256,256,3)
    answ = model.predict_on_batch(x)
    classification = np.where(answ == np.amax(answ))[1][0]
    print(str(answ[0][classification]*100) + '% Confidence This Is A ' + names(classification))

    if(classification == 0):
        p.start(0)

        p.ChangeDutyCycle(12.5)
        sleep(1.36)
    else:
        p.start(0)

        p.ChangeDutyCycle(2.5)
        sleep(1.36)
    p.stop()
    print('done')
    
GPIO.cleanup()
