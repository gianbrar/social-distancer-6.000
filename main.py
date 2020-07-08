import cv2
import time
import itertools
import os

def detect(faces):
    if len(faces) == 1:
        return
    for i in list(itertools.combinations(range(len(faces)), 2)):
        if (abs(faces[i[0]][0] - faces[i[1]][0])) * 1152 >= 6:
            os.system('espeak "WARNING. YOU ARE VIOLATING THE LAW BY NOT PRACTICING SOCIAL DISTANCING."')
    

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
    detect(faces)
    time.sleep(1)
