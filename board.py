class Board:
    def __init__(self, cards, size):
        self.cards = cards
        self.size = size

    def __str__(self):
        string = "Size: " + str(self.size) + "\n" 
        for card in self.cards:
            string += str(card)
        return string
