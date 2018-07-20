import cv2
import numpy as np

#detect edges
def detectImage(OriginalImage):
    #variable for measuring the speed of the function
    e1=cv2.getTickCount()
    
    #canny library is used to identify edges in an picture
    edges=cv2.Canny(OriginalImage, 100,300)
    
    #display using mapplotlib
    '''plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(edges, cmap='gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])'''
    
    #display original image
    cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
    cv2.imshow('Original Image', OriginalImage)
    
    #display edged image
    cv2.namedWindow('Edges', cv2.WINDOW_NORMAL)
    cv2.imshow('Edges', edges)

    e2=cv2.getTickCount()
    print('Object detection took me: {} seconds'.format((e2-e1)/cv2.getTickFrequency()))
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return edges

#crop image
def cropImage(OriginalImage, edgedImaged):
    e1=cv2.getTickCount()
    #find all the edges in the image and trace them objects
    (contours, _)=cv2.findContours(edgedImaged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    index=0
    for contour in contours:
        x,y,w,h=cv2.boundingRect(contour)
        
        #determine w and h depending on the type of object you want to identify
        if w>75 and h>75:
            index+=1
            croppedImg=OriginalImage[y:y+h, x:x+w]
            cv2.imwrite(str(index)+'.png', croppedImg)
    e2=cv2.getTickCount()
    print('Cropping the images took me: {} seconds'.format((e2-e1)/cv2.getTickFrequency()))


def colorDetection(img):
    e1=cv2.getTickCount()

    #next line unsure
    #blurred=cv2.pyrMeanShiftfiltering(img, 5,5)
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    
    #banana green
    lowerRange=np.array([65, 60, 60])
    upperRange=np.array([80, 255, 255])
    '''
    #dark green
    lowerRange=np.array([0,0,20])
    upperRange=np.array([50,128,100])
    
    lowerRange=np.array([40, 100, 50])
    upperRange=np.array([80, 255, 255])
    '''
    mask=cv2.inRange(hsv, lowerRange, upperRange)
    #output=cv2.bitwise_and(img, img, mask=mask)

    
    kernel=np.ones((5,5), np.uint8)
    dilation=cv2.dilate(hsv, kernel, iterations=1)

    closing=cv2.morphologyEx(dilation, cv2.MORPH_GRADIENT, kernel)
    closing=cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)
    
    #getting the edge of the morphology
    edge=cv2.Canny(mask, 100,300)
    '''
    cropImage(img, edge)
    contours, hierach=cv2.findContours(edge.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #find the index of the largest contour
    areas=[cv2.contourArea(c) for c in contours]

    #print(areas)
    maxIndex=np.argmax(areas)
    cntMax=contours[maxIndex]

    x,y,w,h=cv2.boundingRect(cntMax)
    rctc=cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,0),0)
    imggc=img[y:y+h,x:x+h]
    areas=np.array(areas)
    cnt=0
    
    for i in areas:
        
        aIndex=np.array(cnt)
        aCnt=contours[aIndex]
        x,y,w,h=cv2.boundingRect(aCnt)
        rct=cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255,255), 2)
       
        #determine w and h depending on the type of object you want to identify
        croppedImg=img[y:y+h, x:x+w]
        cnt+=1
        cv2.imwrite(str(cnt)+'usingColor' +'.png', croppedImg)
        
        #imgg=img[np.where((img==[0,0,0]).all(axis=2))]=[0,33,166]
    '''
    cv2.namedWindow('Color Detection', cv2.WINDOW_NORMAL)
    cv2.imshow('Color Detection', mask)

    cv2.namedWindow('mask', cv2.WINDOW_NORMAL)
    cv2.imshow('mask', closing)
    cv2.waitKey(0)
    '''
    
        cv2.destroyAllWindows()  
    
    e2=cv2.getTickCount()
    '''
    #print('Colour detection took me: {} seconds'.format((e2-e1)/cv2.getTickFrequency()))
    

image='object4.png'
#reading the image
img=cv2.imread(image)
edgedImage=detectImage(img)
cropImage(img, edgedImage)
colorDetection(img)
