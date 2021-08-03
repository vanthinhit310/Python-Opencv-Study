import cv2 as cv

# ---------------------[Read image by opencv]---------------------
# img = cv.imread('images/image_01.jpeg')
# cv.imshow("Flower", img)
# cv.waitKey(0)
# ---------------------[Read image by opencv]---------------------

# ---------------------[Capture and show video by opencv]---------------------
capture = cv.VideoCapture('videos/sample_02.mp4')

while True:
    isTrue, frame = capture.read()

    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
# ---------------------[Capture and show video by opencv]---------------------
