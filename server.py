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
    print("START")
    return "ok"

@app.route("/move", methods=["POST"])
def move():
    data = request.json
    return { "move": snake.move(data) }

@app.route("/end", methods=["POST"])
def end():
    print("END")
    return "ok"

if __name__ == "__main__":
    app.run(port=8080, debug=True)