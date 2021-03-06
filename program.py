import cv2 as cv

original_image = cv.imread("image.jpeg")
grayscale_image = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)
face_cascade = cv.CascadeClassifier("haarcascade_frontalface_alt.xml")
detected_faces = face_cascade.detectMultiScale(grayscale_image, 1.25)

for (column, row, width, height) in detected_faces:
    cv.rectangle(
        original_image,
        (column, row),
        (column + width, row + height),
        (0, 255, 0),
        2
    )

cv.imshow('Image', original_image)
cv.waitKey(0)
cv.destroyAllWindows()
