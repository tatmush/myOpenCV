import cv2

def detectImage(image):
    #variable for measuring the speed of the function
    e1=cv2.getTickCount()
    #reading the image
    img=cv2.imread(image)
    #canny library is used to identify edges in an picture
    edges=cv2.Canny(img, 200,300)
    
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

detectImage('object4.png')
