import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:    
    _, img = cap.read()
    
    b = img[ : , : , : 1]
    g = img[ : , : ,1: 2]
    r = img[ : , : ,2 : ]

    b_mean = np.mean(b)
    g_mean = np.mean(g)
    r_mean = np.mean(r)

    if (b_mean > g_mean and b_mean > r_mean):
        print("Blue")
    if (g_mean > r_mean and g_mean > b_mean):
        print("Green")
    else:
        print("Red")