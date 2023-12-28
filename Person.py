class Person:
    def __init__(self, x_center, y_center, x_coor, y_coor, width, height, color):
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
        self.x_center = x_center
        self.y_center = y_center
        self.x_coor = x_coor
        self.y_coor = y_coor
        self.width = width
        self.height = height
        self.color = color

    def __str__(self):
        return f"[color:{self.color}, centro:[{self.x_center}, {self.y_center}], coor:[{self.x_coor}, {self.y_coor}], width:{self.width}, height:{self.height}]"

    def introduce(self):
        """Método para que la persona se presente."""
        return f"Hola, me llamo {self.name}. Tengo {self.age} años y soy {self.occupation}."
