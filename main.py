import random
from Person import Person
import cv2

body_detector = cv2.CascadeClassifier('full_body_detector.xml')  # load body detector
video = cv2.VideoCapture("people_walking.mp4")  # Creates an object of opencv to be able to work with the video
people = []
frame_people = []

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
        template = frame[y:y + height, x:x + width]
        if 10 < width < 35 and 25 < height < 90:
            color = None
            if len(people) == 0:
                color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))  # color for each person
                person = Person(center[0], center[1], x, y, width, height, color, template)  # creation of Person instance
                frame_people.append(person)
                rectangle = cv2.rectangle(frame, (x, y), (x + width, y + height), color, 2)  # Draw rectangle
            else:
                for person in people[0]:
                    distance_x = float(person.get_center()[0] - center[0])
                    distance_y = float(person.get_center()[1] - center[1])

                    if (-25 <= distance_x <= 25) and (-25 <= distance_y <= 25):
                        result_template = cv2.matchTemplate(frame, person.template, cv2.TM_CCOEFF_NORMED)
                        a, maxvalue, b, max_loc = cv2.minMaxLoc(result_template)
                        if maxvalue < 0.8:
                            continue
                        top_left = max_loc
                        bottom_right = (top_left[0] + width, top_left[1] + height)
                        cv2.rectangle(frame, top_left, bottom_right, person.color, 2)
                        frame_people.append(person)
    people.clear()
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
