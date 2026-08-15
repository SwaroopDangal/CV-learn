import cv2
#load
image = cv2.imread("phase-5\\great-nature-waterfall-wide.webp")


blurred = cv2.GaussianBlur(image,(9,9),4)

cv2.imshow("Original Image",image)
cv2.imshow("Blurred Image",blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()