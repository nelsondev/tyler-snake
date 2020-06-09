from flask import Flask, request
from src import snake

app = Flask(__name__)

@app.route("/")
def index():
    return {
        "apiversion": "1",
        "author": "nelsondev",
        "color": "#000000",
        "head": "safe",
        "tail": "round-bum"
    }

@app.route("/start", methods=["POST"])
def start():
    data = request.get_json()
    snake.start(data)
    print(f"START {data['game']['id']}")
    return "ok"

@app.route("/move", methods=["POST"])
def move():
    data = request.get_json()
    move = snake.move(data)
    return { "move": move }

@app.route("/end", methods=["POST"])
def end():
    data = request.get_json()
    snake.clear(data)
    print(f"END {data['game']['id']}")
    return "ok"

if __name__ == "__main__":
    app.run(port=8080, debug=True)