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

    def register_dangers(self, data):
        board = get_board(data)
        moves = self.probable_moves()

        self.dangers = board.bounds

        for i in board.snakes:
            self.dangers.extend(i.body)

    def print_points(self, data):

        board = get_board(data)

        a = []
        for y in range(board.height+1):
            s = " " * board.width
            a.append(s)

        for i in self.dangers:
            x = i['x']
            y = i['y']

            a[y][x] = "#"

        for i in a:
            print(i)

    def move(self, data):
        self.register_dangers(data)

        self.print_points(data)

        moves = self.possible_moves()

        return random.choice(moves)

class Board:
    width: int
    height: int
    food: list
    snakes: list
    bounds: list

    def __init__(self, data):
        self.update(data)
        self.bounds(data)

    def bounds(self, data):
        self.bounds = []
        width = int(data['width']) + 1
        height = int(data['height']) + 1

        for i in range(width):
            self.bounds.append({"x":i,"y":-1})
            self.bounds.append({"x":i,"y":width})
        for i in range(height):
            self.bounds.append({"x":-1,"y":i})
            self.bounds.append({"x":height,"y":i})

    def update(self, data):
        self.width = int(data['width'])
        self.height = int(data['height'])
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