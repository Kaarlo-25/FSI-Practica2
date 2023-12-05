# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import cv2

# Load the cascade
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# face_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')    # face detector

cap = cv2.VideoCapture("people_walking.mp4")    #
# cap = cv2.VideoCapture(1)

while (1):
    retVal, frame = cap.read()  # Take each frame
    if not retVal:  # if there's still frames
        break
    frame = cv2.resize(frame, (400, 300)) # Resize image


    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Convertir la imagen a grises
    faces = body_cascade.detectMultiScale(frame)    # Detect bodies
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)    # pinta rectangulo

    cv2.imshow('frame', frame)

##### do not touch this ##############################################################
    k = cv2.waitKey(5) & 0xFF   #
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release()
######################################################################################

class people:


