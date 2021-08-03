import cv2 as cv

img = cv.imread('images/image_01.jpeg')

cv.imshow("Flower", img)

cv.waitKey(0)