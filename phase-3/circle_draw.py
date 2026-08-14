import cv2
#load
image = cv2.imread("phase-3\\py.png")

if image is not None:
    h,w,_ = image.shape
    center = (300,200)
    radius = 180
    color = (255,0,0)
    thickness = 2

    circular_image = cv2.circle(image,center,radius,color,thickness)
    cv2.putText(image,"Image with circle",(50,300),cv2.FONT_HERSHEY_SIMPLEX,1.2,(0,255,255),2)
    cv2.imshow("Original Image",image)
    cv2.imshow("Image with rectangle",circular_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("NO image")


