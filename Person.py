import cv2


class Person:
    ID = 0
    people = []

    # Constructor
    def __init__(self, center, x_coor, y_coor, width, height, color, template):
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

    def __str__(self):
        return f"[ID:{self.ID}, color:{self.color}, center:{self.center}, coor:[{self.x_coor}, {self.y_coor}], width:{self.width}, height:{self.height}]"

    @classmethod
    def same_person(cls, template, frame):
        # min(Person.people, key=lambda person: (abs(person.get_center()[1] - center[1])))
        """
        Objetivo: conseguir la persona del frame anterior
        Requisitos: template matching
        - for por cada persona de people:
            - coges el centro de la persona
            - haces la region de interes y el template matching en el frame actual
            - la mayor coincidencia es la persona
        """

        for person in Person.people:
            x = int(person.center[0] - 25)
            width = 60
            y = int(person.center[1] + 25)
            height = 60
            roi = frame[y:(y + height), x:(x + width)]
            cv2.imshow('ROI', roi)
            cv2.imshow('template', person.template)
            template_comparison = cv2.matchTemplate(roi, person.template, cv2.TM_CCOEFF_NORMED)
            a, max_value, b, max_loc = cv2.minMaxLoc(template_comparison)
            if max_value > 0.9:
                person.x_coor = max_loc[0]
                person.y_coor = max_loc[1]
                person.template = template
                person.center = [(person.width/2) + max_loc[0], (person.height/2) + max_loc[1]]
                return Person.people.index(person)
        return None
