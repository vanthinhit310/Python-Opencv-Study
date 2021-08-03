import cv2 as cv

img = cv.imread("images/image_08.jpg")
cv.imshow("Orginal", img)

# # 1.Converting to Gray
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Convert to Gray", gray)

# # 2. Blur
# blur = cv.GaussianBlur(img, (9, 9), cv.BORDER_DEFAULT)
# cv.imshow("Blur Image", blur)

# # 3.Edge Cascade
# cascade = cv.Canny(img, 125, 175)
# cv.imshow("Edge Cascade", cascade)
#
# # 4.Dilating Image
# dilated = cv.dilate(cascade, (7, 7), iterations=3)
# cv.imshow("Dilated After Edge", dilated)
#
# # 5.Eroding
# eroded = cv.erode(dilated, (3, 3), iterations=1)
# cv.imshow("Eroded After Dilated", eroded)

# # 6. Resize
# resize = cv.resize(img, (300, 350), interpolation=cv.INTER_CUBIC)
# cv.imshow("Resized Image", resize)

# 7. crop
crop = img[30:285, 192:460]
cv.imshow("Cropped", crop)

cv.waitKey(0)
