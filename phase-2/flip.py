import cv2
#load
image = cv2.imread("phase-2\\py.png")


if image is not None:
    #0->vertically flip , 1-> horizontally flip,-1->both
    flipped = cv2.flip(image,-1)

    cv2.imshow("Original Image",image)
    cv2.imshow("Resized Image",flipped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Image is not loaded")