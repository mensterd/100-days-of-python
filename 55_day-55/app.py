from flask import Flask
from random import randint


app = Flask(__name__)


random_number = int

@app.route('/')
def index():
    global random_number
    random_number = randint(0, 9)
    return "<h1>Guess a number between 0 and 9</h1><p><img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'></p>"


@app.route("/<int:number>")
def check_guess(number):
    if number == random_number:
        html_string = "<h1>You found me!</h1><p><img src=' https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'</p>"
    elif number < random_number:
        html_string = "<h1>To low, try again!</h1><p><img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'</p>"
    else:
        html_string = "<h1>To high, try, again!</h1><p><img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'</p>"
    return html_string




if __name__ == "__main__":
    app.run(debug=True)
