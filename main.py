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

    # Sanitize and draw a rectangle around the faces
    facesIntersect = [True] * len(faces)
    sanatizedFaces = []
    for n in range(len(faces)):
        x, y, w, h = faces[n]
        for n1 in range(n + 1, len(faces)):
            x1, y1, w1, h1 = faces[n1]
            print(str(x) + ", " + str(y) + ", " + str(w)  + ", " + str(h))
            print(str(x1) + ", " + str(y1) + ", " + str(w1)  + ", " + str(h1))
            if overlap(x, y, x+w, y+h, x1, y1, x1+w1, y1+h1):
                if w * h < w1 * h1 and facesIntersect[n1] == True:
                    facesIntersect[n] = False
                else:
                    facesIntersect[n1] = False
        if facesIntersect[n]:
            sanatizedFaces.append(facesIntersect[n])
            cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    cv2.imwrite('worked_image.png', image)
    detect(sanatizedFaces)
    time.sleep(1)
