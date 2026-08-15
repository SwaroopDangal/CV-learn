import cv2
import numpy as np
#load
image = cv2.imread("phase-6\\flower.jpg",cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(image,50,150)


cv2.imshow("Original Image",image)
cv2.imshow("Image",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()