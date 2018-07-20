import cv2
import numpy as np
#from matplotlib import pyplot as plt

img=cv2.imread('object1.png')
img2=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template=cv2.imread('template1.png', 0)
w,h=template.shape[::-1]

#comparison methods
methods=['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
         'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    #img=img2.copy()
    method=eval(meth)
    print(meth)

    #apply template matching
    res=cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc=cv2.minMaxLoc(res)

    #if method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left=min_loc
    else:
        top_left=max_loc
    bottom_right=(top_left[0] +w, top_left[1]+h)

    cv2.rectangle(img, top_left, bottom_right, (255,0,0), 2)

    cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
    cv2.imshow('Original Image', img)
    cv2.namedWindow('templateMatching', cv2.WINDOW_NORMAL)
    cv2.imshow('templateMatching', res)
    cv2.waitKey(0)

    
