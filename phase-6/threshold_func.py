import cv2
import numpy as np
#load
image = cv2.imread("phase-6\\great-nature-waterfall-wide.webp",cv2.IMREAD_GRAYSCALE)

ret,thres_img = cv2.threshold(image,120,255,cv2.THRESH_BINARY)

cv2.imshow("Original Image",image)
cv2.imshow("Image",thres_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


"""
90-> 0 black
130-> 255 white
180-> 255 white


"""