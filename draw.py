import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('Blank', blank)

# 1. Paint the image a certain colour
# blank[50:100, 350:400] = 0, 0, 255
# cv.imshow('Green', blank)

# # 2. Draw a rectangle
# cv.rectangle(blank, (0, 0), (blank.shape[1] // 2, blank.shape[0] // 2), (0, 255, 0), thickness=-1)
# cv.imshow('Rectangel', blank)
#
# # 3. Draw a circle
# cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 100, (0, 0, 255), thickness=-1)
# cv.imshow("Circle", blank)
#
# # 4. Draw a line
# cv.line(blank, (50, 450), (450, 450), (190, 120, 180), thickness=3)
# cv.imshow("Line", blank)

# 5. Write text
cv.putText(blank, 'Hello Python', (blank.shape[1]//2, blank.shape[0]//2), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
cv.imshow("Text", blank)

cv.waitKey(0)
