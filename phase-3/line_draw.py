import cv2
#load
image = cv2.imread("phase-3\\py.png")


if image is not None:
    h,w,_ = image.shape
    start = (0,0)
    end = (h//2,w//2)
    color = (255,0,0)
    thickness = 4

    image_with_line=cv2.line(image,start,end,color,thickness)
    cv2.imshow("Original Image",image)
    cv2.imshow("Image with Line",image_with_line)
    cv2.waitKey(0)
    cv2.destroyAllWindows()