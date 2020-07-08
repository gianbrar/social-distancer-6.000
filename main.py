import cv2
import time
import math

def detect(faces):
    if faces == 1:
        return

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
camera = cv2.VideoCapture(0)

while True:
    return_value, image = camera.read()
    cv2.imwrite('working_image.png', image)
    image = cv2.imread('working_image.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30)
    )

    print("Found {0} faces!".format(len(faces)))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imwrite('worked_image.png', image)
    detect(math.factorial(len(faces)) / math.factorial(max(0, len(faces) - 2)))
    time.sleep(1)
