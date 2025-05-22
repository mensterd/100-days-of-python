import requests
from flask import Flask, render_template
import random, datetime

app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1, 100)
    current_year = datetime.datetime.now().year
    return render_template("index.html", number=random_number, copyright_year=current_year)


@app.route("/name/<name>")
def greet(name):
    return render_template("index.html", greet_name=name)


@app.route("/blog/<number>")
def get_blog(number):
    print(number)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts =  response.json()
    return render_template("blog.html", posts=all_posts)



if __name__ == "__main__":
    app.run(debug=True)
