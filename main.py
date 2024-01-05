import random
from Person import Person
import cv2

body_detector = cv2.CascadeClassifier('full_body_detector.xml')
video = cv2.VideoCapture("people_walking.mp4")

i = 0
while True:
    exist_frame, frame = video.read()
    if not exist_frame:  # if there's not any frame exit the loop
        break
    frame = cv2.resize(frame, (600, 450))
    grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert color image to black and white
    rectangle_frame = frame.copy()
    bodies = body_detector.detectMultiScale(grey_frame)  # Detect bodies

    for body in bodies:
        x = body[0]
        y = body[1]
        width = body[2]
        height = body[3]
        color = None
        center = None
        template = None

        if 20 < width < 55 and 35 < height < 100:
            center = [(width / 2) + x, (height / 2) + y]
            template = frame[y:y + height, x:x + width]
            if i == 0:
                color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
                Person.people.append(Person(center, x, y, width, height, color, template))
                ID = "Mierda"

            else:
                coincidence = Person.same_person(template, frame, center, x, y)
                if coincidence is not None:
                    color = coincidence.color
                    ID = coincidence.ID
                else:
                    color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
                    Person.people.append(Person(center, x, y, width, height, color, template))
                    ID = Person.people[-1].ID
            rectangle = cv2.rectangle(rectangle_frame, (x, y), (x + width, y + height), color, 2)
            cv2.putText(rectangle_frame, f"{ID}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.imshow('frame', rectangle_frame)  # Shows the video in a new window

    #for person in Person.people:

        #person.is_update[0] == False and person.is_update[1] == 0

        #if person.y_coor < 1 or person.y_coor + person.height == 599:
            #Person.people.remove(person)
        #if not person.is_update[0]:
            #person.is_update[1] -= 1

    i += 1
    # escape button to exit the video
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()  # closes all the windows opened with imshow
video.release()  # releases all the resources used in the video processing
