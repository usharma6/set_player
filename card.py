class Card:
    def __init__(self, color, number, shape, shade):
        self.color = color
        self.number = number
        self.shape = shape
        self.shade = shade

    def __str__(self):
        return "Color: " + str(self.color) + "\n" + "Number: " + str(self.number + 1) + "\n" + "Shape: " + str(self.shape) + "\n" + "Shade: " + str(self.shade) + "\n"
