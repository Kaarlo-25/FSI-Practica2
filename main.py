import random
from Person import Person
import cv2

body_detector = cv2.CascadeClassifier('full_body_detector.xml')  # load body detector
video = cv2.VideoCapture("people_walking.mp4")  # Creates an object of opencv to be able to work with the video
people = []
frame_people = []
upper_size_threshold = 3000
lower_size_threshold = 400
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
        #if 10 < width < 35 and 25 < height < 90:
        if upper_size_threshold > (width * height) > lower_size_threshold:
            color = None
            if len(people) == 0:
                color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))  # color for each person
                person = Person(center[0], center[1], x, y, width, height, color)  # creation of Person instance
                frame_people.append(person)
            else:
                i = 0
                for person in people[i]:
                    distance_x = float(person.get_center()[0] - center[0])
                    distance_y = float(person.get_center()[1] - center[1])
                    print(distance_x)
                    print(distance_y)
                    print()
                    if (-0.5 <= distance_x <= 0.5) and (-3.0 <= distance_y <= 3.0):
                        color = person.get_color()
                        person = Person(center[0], center[1], x, y, width, height, color)
                        frame_people.append(person)
                i += 1
            rectangle = cv2.rectangle(frame, (x, y), (x + width, y + height), color, 2)  # Draw rectangle
    people.append(frame_people.copy())
    frame_people.clear()
    cv2.imshow('frame', frame)  # Shows the video in a new window
    k = cv2.waitKey(5) & 0xFF  # escape button to exit the video
    if k == 27:
        break
cv2.destroyAllWindows()  # closes all the windows opened with imshow
video.release()  # releases all the resources used in the video processing

# TODO error following people after a few frames
# TODO track people
# TODO different color in rectangles for each person
# TODO useful
