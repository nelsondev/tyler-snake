import random

class Move:
    @staticmethod
    def opposite_direction(direction):
        if direction == "up": return "down"
        if direction == "down": return "up"
        if direction == "left": return "right"
        if direction == "right": return "left"

    @staticmethod
    def future_point(direction, point):
        if direction == "up": point['y'] + 1
        if direction == "down": point['y'] - 1
        if direction == "left": point['x'] - 1
        if direction == "right": point['x'] + 1
        return point

class Snake:
    id: str
    name: str
    health: int
    body: list
    head: dict
    length: int

    dangers: list

    def __init__(self, data):
        self.dangers = []
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
        possible = self.possible_moves()

        m = {}
        for i in possible:
            m[i] = 0
        return m

    def dangerous_moves(self):
        probable = self.probable_moves()

        for i in self.dangers:
            print(i)

    def register_dangers(self, data):
        board = get_board(data)
        
        for i in board.snakes:
            print(i.id)
            self.dangers.extend(i.body)

    def move(self, data):
        self.register_dangers(data)
        self.dangerous_moves()

        moves = self.possible_moves()

        return random.choice(moves)

class Board:
    width: int
    height: int
    food: list
    snakes: list

    def __init__(self, data):
        self.update(data)

    def update(self, data):
        self.width = data['width']
        self.height = data['height']
        self.food = data['food']
        self.snakes = []

        for i in data['snakes']:
            self.snakes.append(Snake(i))


tylers = {}

def get_game(data):
    return data['id']

def get_tyler(data):
    return tylers[get_game(data)]['snake']

def get_board(data):
    return tylers[get_game(data)]['board']


def start(data):
    tylers[get_game(data['you'])] = { "snake" : Snake(data['you']), "board": Board(data['board']) }

def clear(data):
    del tylers[get_game(data['you'])]

def move(data):
    tyler = get_tyler(data['you'])
    board = get_board(data['you'])

    tyler.update(data['you'])
    board.update(data['board'])

    return tyler.move(data['you'])