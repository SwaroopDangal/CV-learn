import cv2

#load
image = cv2.imread("phase-1\\py.png")

if image is not None:
    grayscale = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imwrite("phase-1\\black-white.png",grayscale)
    cv2.imshow("Image", grayscale)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Cant find Image")