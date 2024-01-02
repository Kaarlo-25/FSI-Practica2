import random
from Person import Person
import cv2

# TODO compare frames with a prior few
# TODO save people trajectory

body_detector = cv2.CascadeClassifier('full_body_detector.xml')  # load body detector
video = cv2.VideoCapture("people_walking.mp4")  # Creates an object of opencv to be able to work with the video
people = []
frame_people = []

while True:
    # if len(people) == 2: people.pop(0)
    existFrame, frame = video.read()  # Take each frame
    if not existFrame:  # if there's not any frame exit the loop
        break
    frame = cv2.resize(frame, (400, 300))  # Resize image
    grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert color image to black and white
    rectangle_frame = grey_frame.copy()
    bodies = body_detector.detectMultiScale(grey_frame)  # Detect bodies

    for body in bodies:
        x = body[0]
        y = body[1]
        width = body[2]
        height = body[3]
        center = [(width / 2) + x, (height / 2) + y]
        #template = frame[y:y + height, x:x + width]
        color = None

        if 10 < width < 35 and 25 < height < 90:
            if len(people) == 0:
                color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))  # color for each person
                frame_people.append(Person(center[0], center[1], x, y, width, height, color))
            else:
                closest_person = min(people[0], key=lambda person: (abs(person.get_center()[1] - center[1])))
                if abs(closest_person.center[0]-center[0]) < 10:
                    color = closest_person.get_color()
                    frame_people.append(Person(center[0], center[1], x, y, width, height, color))
                """
                else:
                    color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))  # color for each person
                    frame_people.append(Person(center[0], center[1], x, y, width, height, color))
                """
            rectangle = cv2.rectangle(frame, (x, y), (x + width, y + height), color, 2)  # Draw rectangle

    people.append(frame_people.copy())
    frame_people.clear()
    cv2.imshow('frame', frame)  # Shows the video in a new window
    k = cv2.waitKey(5) & 0xFF  # escape button to exit the video
    if k == 27:
        break
cv2.destroyAllWindows()  # closes all the windows opened with imshow
video.release()  # releases all the resources used in the video processing

def person_trajectory(point1, point2):
    """
    Calculate the line equation that goes through two points:
        point1: Tuple (x1, y1) del primer point
        point2: Tuple (x2, y2) del segundo point
        return: Tuple (m, b) where m is the slope and b is the intersection with the y-axis
    """
    x1, y1 = point1
    x2, y2 = point2

    if x2 - x1 != 0:
        m = (y2 - y1) / (x2 - x1)
    else:
        return "Impossible to calculate the trajectory because slope == infinite"

    b = y1 - m * x1
    return m, b
