import random
import operator


class Move:
    @staticmethod
    def opposite_direction(direction):
        if direction == "up": return "down"
        if direction == "down": return "up"
        if direction == "left": return "right"
        if direction == "right": return "left"

    @staticmethod
    def future_point(direction, point):
        x = point['x']
        y = point['y']
        if direction == "up": y += 1
        if direction == "down": y -= 1
        if direction == "left": x -= 1
        if direction == "right": x += 1
        return {"x": x, "y": y}

class Snake:
    id: str
    name: str
    health: int
    body: list
    head: dict
    length: int

    dangers: list
    weights: list

    def __init__(self, data):
        self.dangers = []
        self.weights = []
        self.update(data)
        self.register_weights()
        
    def update(self, data):
        self.id = data['id']
        self.name = data['name']
        self.health = data['health']
        self.body = data['body']
        self.head = data['head']
        self.length = data['length']

    # GRABBING FRESH POINTS
    def possible_moves(self):
        return [ 'up', 'down', 'left', 'right' ]

    def probable_moves(self):
        possible = self.possible_moves()

        m = {}
        for i in possible:
            m[i] = 0
        return m

    # WEIGH STACK FOR WEIGHING MOVE PROBABLITY
    def weigh(self, moves):
        for direction in moves:
            for weight in self.weights:
                moves[direction] += weight(direction)
        return moves

    # REGISTER PROPER WEIGHTS INTO WEIGHT ARRAY
    def register_weights(self):
        self.weights.append(self.weigh_dangers)
        self.weights.append(self.weigh_split)
        self.weights.append(self.weigh_food)

    # DATA REGISTRATION FOR RELEVANT POINTS 
    def register_dangers(self, data):
        board = get_board(data)

        self.dangers = []
        self.dangers.extend(board.bounds)
        self.dangers.extend([a.body for a in board.snakes][0])

    def register_food(self, data):
        pass

    # WEIGHING LOGIC CALLED IN weigh() FUNCTION
    def weigh_dangers(self, direction):
        VALUE = -999
        future = Move.future_point(direction, self.head)
        return VALUE if future in self.dangers else 0

    def weigh_split(self, direction):
        VALUE = 10
        result = 0
        future = Move.future_point(direction, self.head)
        while not future in self.dangers:
            future = Move.future_point(direction, future)
            result += VALUE
        return result

    def weigh_food(self, direction):
        VALUE = 0
        return VALUE

    # HELPER FUNCTIONS
    def max_weight(self, moves):
        return max(moves.items(), key=lambda x: x[1])[1]

    def max_moves(self, moves):
        max_weight = self.max_weight(moves)
        return [direction for direction, weight in moves.items() if weight == max_weight]

    def move(self, data):
        self.register_dangers(data)
        self.register_food(data)

        moves = self.probable_moves()
        moves = self.weigh(moves)

        print(moves)

        moves = self.max_moves(moves)

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
        width = int(data['width'])
        height = int(data['height'])

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