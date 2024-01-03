import random
from Person import Person
import cv2


body_detector = cv2.CascadeClassifier('full_body_detector.xml')  # load body detector
video = cv2.VideoCapture("people_walking.mp4")  # Creates an object of opencv to be able to work with the video

while True:
    exist_frame, frame = video.read()
    if not exist_frame:  # if there's not any frame exit the loop
        break
    frame = cv2.resize(frame, (400, 300))
    grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert color image to black and white
    rectangle_frame = grey_frame.copy()
    bodies = body_detector.detectMultiScale(grey_frame)  # Detect bodies

    for body in bodies:
        x = body[0]
        y = body[1]
        width = body[2]
        height = body[3]
        color = None
        center = None
        template = None

        if 10 < width < 35 and 25 < height < 90:
            center = [(width / 2) + x, (height / 2) + y]
            template = frame[y:y + height, x:x + width]
            if len(Person.people) == 0:
                color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
                Person.people.append(Person(center, x, y, width, height, color, template))
            else:
                coincidence = Person.same_person(template, frame)
                if coincidence is not None:
                    print(coincidence)
                    # TODO assign those values to x, y, width, height and color
                else:
                    color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
                    Person.people.append(Person(center, x, y, width, height, color, template))

            rectangle = cv2.rectangle(rectangle_frame, (x, y), (x + width, y + height), color, 2)
    cv2.imshow('frame', frame)  # Shows the video in a new window
    # escape button to exit the video
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()  # closes all the windows opened with imshow
video.release()  # releases all the resources used in the video processing
