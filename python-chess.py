#--------------------
#|   Python Chess   |
#|        by        |
#|  Matthew Dallman |
#--------------------
def main():
    #Heart of the game that brings it all together.
    pass

class piece:
    #Parent Class for each of the chess pieces.
    colour = ''
    location = ['','']

    def __init__(self, colour = 'white', location = ['a','1']):
         self.colour = colour
         self.location = location
    
def showBoard():
    print("""

      | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |  
    --|---|---|---|---|---|---|---|---|
    A |   |   |   |   |   |   |   |   |
    --|---|---|---|---|---|---|---|---|
    B |   |   |   |   |   |   |   |   |
    --|---|---|---|---|---|---|---|---|
    C |   |   |   |   |   |   |   |   |
    --|---|---|---|---|---|---|---|---|
    D |   |   |   |   |   |   |   |   |
    --|---|---|---|---|---|---|---|---|
    E |   |   |   |   |   |   |   |   |
    --|---|---|---|---|---|---|---|---|
    F |   |   |   |   |   |   |   |   |
    --|---|---|---|---|---|---|---|---|
    G |   |   |   |   |   |   |   |   |
    --|---|---|---|---|---|---|---|---|
    H |   |   |   |   |   |   |   |   |
    --|---|---|---|---|---|---|---|---|


    """)
