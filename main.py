import random
from Person import Person
import cv2

body_detector = cv2.CascadeClassifier('full_body_detector.xml')  # load body detector
video = cv2.VideoCapture("people_walking.mp4")  # Creates an object of opencv to be able to work with the video
people = []
upper_size_threshold = 3000
lower_size_threshold = 500
y_moving_threshold = 3

while True:
    existFrame, frame = video.read()  # Take each frame
    if not existFrame:  # if there's not any frame exit the loop
        break
    frame = cv2.resize(frame, (400, 300))  # Resize image
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert color image to black and white
    bodies = body_detector.detectMultiScale(gray_frame)  # Detect bodies

    for body in bodies:
        x = body[0]
        y = body[1]
        width = body[2]
        height = body[3]
        center = [(width / 2) + x, (height / 2) + y]
        if upper_size_threshold > (width * height) > lower_size_threshold:
            color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))  # color for each person
            person = Person(center[0], center[1], x, y, width, height, color)  # creation of Person instance
            people.append(person)
            print(bodies[0])
            print(person.__str__())
            print(people[0].__str__() + "\n")
        if len(people) != 0 and len(people) != 1:
            i = 1
            if people[i-1].y_center - person.y_center <= y_moving_threshold:
                cv2.rectangle(frame,
                              (person.x_coor, person.y_coor),
                              (person.x_coor + person.width, person.y_coor + person.height),
                              person.color,
                              2)  # Draw rectangles
    cv2.imshow('frame', frame)  # Shows the video in a new window
    k = cv2.waitKey(5) & 0xFF  # escape button to exit the video
    if k == 27:
        break
cv2.destroyAllWindows()  # closes all the windows opened with imshow
video.release()  # releases all the resources used in the video processing



# TODO track people
# TODO different color in rectangles of every people
# TODO useful


