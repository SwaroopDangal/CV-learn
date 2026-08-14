import cv2
#load
image = cv2.imread("phase-2\\py.png")


if image is not None:
    (h,w,_)=image.shape
    center = (w//2,h//2)
    #center,angle,scale
    M = cv2.getRotationMatrix2D(center,45,1.0)
    
    roated = cv2.warpAffine(image,M,(w,h))

    cv2.imshow("Original Image",image)
    cv2.imshow("Resized Image",roated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Image is not loaded")