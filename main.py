# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import cv2
import numpy as np


def mask(image):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    img = cv2.imread(image)
    cv2.imshow("Wave", img)
    cv2.waitKey(0)
    # we readed the image

    # The kernel to be used for dilation purpose
    kernel = np.ones((5, 5), np.uint8)

    # converting the image to HSV format
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # defining the lower and upper values of HSV,
    # this will detect yellow colour
    Lower_hsv = np.array([20, 70, 100])
    Upper_hsv = np.array([30, 255, 255])
    #Lower_hsv = np.array([50, 100, 100])
    #Upper_hsv = np.array([70, 255, 255])
    #lower = np.array([00, 100, 100])
    #upper = np.array([100, 255, 255])
    #Lower_hsv = lower
    #Upper_hsv = upper
    # Defining mask for detecting color
    #mask = cv2.inRange(hsv, lower, upper)
    #cv2.imshow("Mask", mask)
    #cv2.waitKey(0)

    # creating the mask by eroding,morphing,
    # dilating process
    Mask = cv2.inRange(hsv, Lower_hsv, Upper_hsv)
    Mask = cv2.erode(Mask, kernel, iterations=1)
    Mask = cv2.morphologyEx(Mask, cv2.MORPH_OPEN, kernel)
    Mask = cv2.dilate(Mask, kernel, iterations=1)
    cv2.imshow("Mask", Mask)
    cv2.waitKey(0)

    mask_yellow = cv2.bitwise_not(Mask)
    MaskedImage = cv2.bitwise_and(img, img, mask=mask_yellow)
    cv2.imshow("Mask", MaskedImage)
    cv2.waitKey(0)
    return Mask, MaskedImage


    #masked = cv2.bitwise_and(img, img, mask=mask)
    #cv2.imshow("Masked", masked)
    #cv2.waitKey(0)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path = r"C:\Users\JasSu\Documents\SHSU\image-inpainting\Capture1.jpg"
    Mask, MaskedImage = mask(path)
    dst = cv2.inpaint(MaskedImage, Mask, 3, cv2.INPAINT_NS)
    cv2.imshow('dst', dst)
    cv2.waitKey(0)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
