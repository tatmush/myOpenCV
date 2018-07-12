import cv2

#detect edges
def detectImage(image):
    #variable for measuring the speed of the function
    e1=cv2.getTickCount()
    
    #canny library is used to identify edges in an picture
    edges=cv2.Canny(img, 100,300)
    
    #display using mapplotlib
    '''plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(edges, cmap='gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])'''
    
    #display original image
    cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
    cv2.imshow('Original Image', img)
    
    #display edged image
    cv2.namedWindow('Edges', cv2.WINDOW_NORMAL)
    cv2.imshow('Edges', edges)
    
    #print('It took me: {} seconds'.format((e2-e1)/cv2.getTickFrequency()))
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return edges

#crop image
def cropImage(OriginalImage, edgedImaged):
    #find all the edges in the image and trace them objects
    (contours, _)=cv2.findContours(edgedImaged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    index=0
    for contour in contours:
        x,y,w,h=cv2.boundingRect(contour)
        
        #determine w and h depending on the type of object you want to identify
        if 75 and h>75:
            index+=1
            croppedImg=OriginalImage[y:y+h, x:x+w]
            cv2.imwrite(str(index)+'.png', croppedImg)

image='object4.png'
#reading the image
img=cv2.imread(image)
edgedImage=detectImage(img)
cropImage(img, edgedImage)
