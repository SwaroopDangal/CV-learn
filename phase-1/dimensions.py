import cv2

#load
image = cv2.imread("phase-1\\py.png")

if image is not None:
    h,w,c = image.shape
    print(f"Image Loaded:\n Height:{h} \n width:{w} \n Channels:{c}")

else:
    print("Could not load Image")