import cv2

#load
image = cv2.imread("phase-1\\py.png")

if image is None:
    print("Could not open image")
else:
    # display
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #saving
    sucess = cv2.imwrite("phase-1\\py_copy.png", image)
    if sucess:
        print("Sucessfully saved")
    else:
        print("Could not save")
