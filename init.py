import re
from card import Card
from board import Board
import numpy as np

def get_settings():
    attributes = re.compile(':\\s+')
    values = []
    with open('settings.txt', 'rt') as fp:
        line = fp.readline()    
        while line:
            val = attributes.split(line)
            values.append(int(val[1]))
            line = fp.readline()
    return values

def init_deck(card_colors, card_shapes, card_maxnum, card_shades):
    deck = np.empty(card_colors * card_shapes * card_maxnum * card_shades, dtype = Card)
    index = 0
    for color in range(card_colors):
        for shape in range(card_shapes):
            for num in range(card_maxnum):
                for shade in range(card_shades):
                    c = Card(color, num, shape, shade)
                    deck[index] = c
                    index += 1
    return deck

def init_board(deck, board_size):
    card_array = np.random.choice(deck, size = board_size ,replace = False)
    board = Board(card_array, board_size)
    return board

if __name__ == '__main__':
    board_size, colors, shapes, maxnum, shades = get_settings()
    deck = init_deck(colors, shapes, maxnum, shades)
    board = init_board(deck, board_size)
    print(board)
