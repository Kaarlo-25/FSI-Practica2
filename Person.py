class Person:
    def __init__(self, x_center, y_center, x_coor, y_coor, width, height, color, template):
        """
        Constructor of class Person.

        Args:
        - x_center (int): X coordinate of the center of the detection rectangle
        - y_center (int): Y coordinate of the center of the detection rectangle
        - x_coor (int): X coordinate of the rectangle
        - y_coor (int): Y coordinate of the rectangle
        - width (int): Width of the rectangle
        - height (int): Height of the rectangle
        """
        self.center = [x_center, y_center]
        self.x_coor = x_coor
        self.y_coor = y_coor
        self.width = width
        self.height = height
        self.color = color
        self.template = template

    def __str__(self):
        return f"[color:{self.color}, center:{self.center}, coor:[{self.x_coor}, {self.y_coor}], width:{self.width}, height:{self.height}]"

    def get_center(self):
        return self.center

    def get_color(self):
        return self.color

    def get_template(self):
        return self.template