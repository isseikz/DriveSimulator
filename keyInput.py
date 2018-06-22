import numpy as np
# import getkey as keylib
# import cv2
import win32api
from virtualKey import *
from math import pi

def getInput():
    status = 1
    ctrl = np.array([0.0,0.0])

    # key = keylib.getkey()
    image = cv2.imread('./topview_car_wagon.png')
    cv2.imshow('image',image)
    key = cv2.waitKey(10)
    # print(key)
    if key == ord('s'):
        status = 0
    elif key == ord('l'):
        ctrl[0] += 10
    elif key == ord('j'):
        print('j')
        ctrl[0] += -10
    elif key == ord('i'):
        ctrl[1] -= 10
    elif key == ord(','):
        ctrl[1] -= -10
    else:
        ctrl = [0,0]

    return status, ctrl

def getInputWin32():
    status = 1
    ctrl = np.array([0.0,0.0])
    if isPressed(key['g']):
        status = 0
    else:
        if isPressed(key['u']):
            ctrl[0] = 30.0
        elif isPressed(key['i']):
            ctrl[0] = 25.0
        elif isPressed(key['o']):
            ctrl[0] = 20.0
        elif isPressed(key['p']):
            ctrl[0] = 15.0
        elif isPressed(key['j']):
            ctrl[0] = 10.0
        elif isPressed(key['k']):
            ctrl[0] = 5.0
        elif isPressed(key['l']):
            ctrl[0] = -5.0
        elif isPressed(key['+']):
            ctrl[0] = -10.0
        elif isPressed(key['m']):
            ctrl[0] = -15.0
        elif isPressed(key[',']):
            ctrl[0] = -20.0
        elif isPressed(key['.']):
            ctrl[0] = -25.0
        elif isPressed(key['/']):
            ctrl[0] = -30.0
        else:
            ctrl[0] = 0.0

        if  isPressed(key['a']):
            print('a')
            ctrl[1] = pi/300
        elif isPressed(key['s']):
            print('s')
            ctrl[1] = pi/600
        elif isPressed(key['d']):
            print('d')
            ctrl[1] = -pi/600
        elif isPressed(key['f']):
            print('f')
            ctrl[1] = -pi/300
        else:
            ctrl[1] = 0.0

    return status, ctrl



def isPressed(key):
    if win32api.GetAsyncKeyState(key) != 0:
        return True
    else:
        return False
