from app import app

@app.route('/')
def index():
    return "LIFE MOVES PRETTY FAST"

@app.route('/<name>')
def greet(name):
    return f"Hello {name}!"