import random

class Snake:
    id: str
    name: str
    health: int
    body: list
    head: dict
    length: int

    def __init__(self, data):
        self.update(data)
    
    def update(self, data):
        self.id = data['id']
        self.name = data['name']
        self.health = data['health']
        self.body = data['body']
        self.head = data['head']
        self.length = data['length']

    def possible_moves(self):
        return [ 'up', 'down', 'left', 'right' ]

    def probable_moves(self):
        pass

    def move(self, data):
        self.update(data)

        possible = self.possible_moves()
        probable = self.probable_moves()
        
        return random.choice(possible)

class Board:
    width: int
    height: int
    food: list
    snakes: list

    def __init__(self, data):
        pass

    def update(self, data):
        self.width = data['width']
        self.height = data['height']
        self.food = data['food']
        self.snakes = []

        for i in data['snakes']:
            self.snakes.append(Snake(i))

tylers = {}

def get_game(data):
    return data['game']['id']

def get_tyler(data):
    return tylers[get_game(data)]['snake']

def get_board(data):
    return tylers[get_game(data)]['board']

def start(data):
    tylers[get_game(data)] = { "snake" : Snake(data['you']), "board": Board(data['board']) }

def clear(data):
    del tylers[get_game(data)]

def move(data):
    tyler = get_tyler(data)
    return tyler.move(data['you'])