import cv2
#load
image = cv2.imread("phase-2\\py.png")


if image is not None:
    resized = cv2.resize(image,(200,200))
    cv2.imshow("Original Image",image)
    cv2.imshow("Resized Image",resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Image is not loaded")