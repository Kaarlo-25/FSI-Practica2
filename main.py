# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# face_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
# cap = cv2.VideoCapture(1)

import cv2

body_detector = cv2.CascadeClassifier('haarcascade_fullbody.xml')  # load face detector
video = cv2.VideoCapture("people_walking.mp4")  # Creates an object of opencv to be able to work with the video

while 1:
    existFrame, frame = video.read()  # Take each frame
    if not existFrame:  # if there's not any frame exit the loop
        break
    frame = cv2.resize(frame, (400, 300))  # Resize image
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert color image to black and white
    bodies = body_detector.detectMultiScale(frame)  # Detect bodies
    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Draw rectangles
    cv2.imshow('frame', frame)  # Shows the video in a new window

##### do not touch this ##############################################################
    k = cv2.waitKey(5) & 0xFF  # escape button to exit the video
    if k == 27:
        break
cv2.destroyAllWindows()     # closes all the windows opened with imshow
video.release()         # releases all the resources used in the video processing
######################################################################################
#TODO create person class
#TODO track people
#TODO different color in rectangles of every people
#TODO useful
