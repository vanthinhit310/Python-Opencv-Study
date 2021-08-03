import cv2 as cv


# ---------------------[]---------------------
# ---------------------[]---------------------

# Function rescale Video or Image
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# Function to change resolution of video or image
def changeResolution(width, height):
    capture.set(3, width)
    capture.set(4, height)


# ---------------------[Rescale Video]---------------------
capture = cv.VideoCapture('videos/sample_02.mp4')

while True:
    isTrue, frame = capture.read()
    frame_rescaled = rescaleFrame(frame, 0.3)
    cv.imshow('Video', frame)
    cv.imshow('Video Rescaled', frame_rescaled)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
# ---------------------[Rescale Video]---------------------

# ---------------------[Rescale Image]---------------------
img = cv.imread("images/image_08.jpg")
img_rescaled = rescaleFrame(img, 0.5)
cv.imshow("Image Original", img)
cv.imshow("Image Rescale", img_rescaled)

cv.waitKey(0)
# ---------------------[Rescale Image]---------------------
