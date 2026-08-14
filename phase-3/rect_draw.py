import cv2
#load
image = cv2.imread("phase-3\\py.png")

if image is not None:
    h,w,_ = image.shape
    top_left_point = (120,0)
    bottom_right_point = (450,380)
    color = (255,0,0)
    thickness = 4
    rectangle_image = cv2.rectangle(image,top_left_point,bottom_right_point,color,thickness)
    cv2.imshow("Original Image",image)
    cv2.imshow("Image with rectangle",rectangle_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

