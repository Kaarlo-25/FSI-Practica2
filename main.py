from Person import Person
import cv2

body_detector = cv2.CascadeClassifier('full_body_detector.xml')
video = cv2.VideoCapture("people_walking.mp4")

current_frame = 1
while True:
    exist_frame, frame = video.read()
    if not exist_frame:
        break
    frame = cv2.resize(frame, (600, 450))
    grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rectangle_frame = frame.copy()
    bodies = body_detector.detectMultiScale(grey_frame)

    for body in bodies:
        x = body[0]
        y = body[1]
        width = body[2]
        height = body[3]
        color = None
        center = None
        template = None

        if 20 < width < 65 and 35 < height < 115:
            center = [(width / 2) + x, (height / 2) + y]
            template = frame[y:y + height, x:x + width]
            if current_frame == 1:
                ID = Person.create_person(center, x, y, width, height, template, current_frame)
            else:
                coincidence = Person.same_person(template, frame, center, x, y, current_frame)
                if coincidence is not None:
                    color = coincidence.color
                    ID = coincidence.ID
                else:
                    ID = Person.create_person(center, x, y, width, height, template, current_frame)
            rectangle = cv2.rectangle(rectangle_frame, (x, y), (x + width, y + height), color, 2)
            cv2.putText(rectangle_frame, f"{ID}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.imshow('frame', rectangle_frame)

    current_frame += 1
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
video.release()
