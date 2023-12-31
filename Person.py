import cv2


class Person:
    ID = 0
    people = []

    # Constructor
    def __init__(self, center, x_coor, y_coor, width, height, color, template, is_update=[False, 2]):
        """
        Constructor of class Person.

        Args:
        - x_center (int): X coordinate of the center of the detection rectangle
        - y_center (int): Y coordinate of the center of the detection rectangle
        - x_coor (int): X coordinate of the rectangle
        - y_coor (int): Y coordinate of the rectangle
        - width (int): Width of the rectangle
        - height (int): Height of the rectangle
        - trajectory(tuple): Trajectory of the person
        """
        Person.ID += 1
        self.ID = Person.ID
        self.center = center
        self.x_coor = x_coor
        self.y_coor = y_coor
        self.width = width
        self.height = height
        self.color = color
        self.template = template
        self.is_update = is_update

    def get_center(self):
        return self.center

    def get_color(self):
        return self.color

    def set_center(self, new_center):
        self.center = new_center

    def set_x_coor(self, new_x_coor):
        self.center = new_x_coor

    def set_y_coor(self, new_y_coor):
        self.center = new_y_coor

    def set_template(self, new_template):
        self.center = new_template

    def set_width(self, new_width):
        self.center = new_width

    def set_height(self, new_height):
        self.center = new_height

    def update_coord(self, new_x_coor, new_y_coor, new_center):
        self.x_coor = new_x_coor
        self.y_coor = new_y_coor
        self.center = new_center
        self.is_update[0] = True
        self.is_update[1] = 3

    def __str__(self):
        return f"[ID:{self.ID}, color:{self.color}, center:{self.center}, coor:[{self.x_coor}, {self.y_coor}], width:{self.width}, height:{self.height}]"

    @classmethod
    def same_person(cls, template, frame, center, x, y):
        # min(Person.people, key=lambda person: (abs(person.get_center()[1] - center[1])))
        """
        Objetivo: conseguir la persona del frame anterior
        Requisitos: template matching
        - for por cada persona de people:
            - coges el centro de la persona
            - haces la region de interes y el template matching en el frame actual
            - la mayor coincidencia es la persona
        """
        close_centers = []
        for person in Person.people:
            if (abs(person.center[0] - center[0]) < 6 and abs(person.center[1] - center[1]) < 6) or (
                    abs(person.x_coor - x) < 15 and abs(person.y_coor - y) < 15):
                close_centers.append(person)
            if person.y_coor < 1 or person.y_coor + person.height == 599:
                Person.people.remove(person)

        if len(close_centers) == 0:
            return None
        if len(close_centers) == 1:
            close_centers[0].update_coord(x, y, center)
            return close_centers[0]
        else:
            person_found = min(close_centers, key=lambda person: (abs(person.get_center()[1] - center[1])))
            return person_found


    """
        else:
            for person in Person.people:
                center_x = int(center[0])
                width = 200
                center_y = int(center[1])
                height = 200
                x_start = max(0, center_x - width // 2)
                y_start = max(0, center_y - height // 2)
                x_end = min(frame.shape[1], x + width // 2)
                y_end = min(frame.shape[0], y + height // 2)
                roi = frame[y_start:y_end, x_start:x_end]
                template_comparison = cv2.matchTemplate(roi, person.template, cv2.TM_SQDIFF_NORMED)
                min_value, max_value, min_loc, max_loc = cv2.minMaxLoc(template_comparison)
                cv2.imshow("ROI", cv2.resize(roi, (400, 300)))
                cv2.imshow("Template", cv2.resize(person.template, (400, 300)))
                if max_value > 0.90:
                    person.x_coor = x
                    person.y_coor = y
                    person.template = template
                    person.center = [(person.width / 2) + x, (person.height / 2) + y]
                    return Person.people.index(person)
    """
