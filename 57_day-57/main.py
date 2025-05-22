from flask import Flask, render_template
import requests

from post import Post


# get the fake blogposts from the API
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
# Create List to store post objects
post_objects = []
# Create objects of json-posts and append to List
for post in posts:
    post_object = Post(id=post["id"], title=post["title"], subtitle=post["subtitle"], body=post["body"])
    post_objects.append(post_object)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html", all_posts=post_objects)



@app.route("/post/<int:blog_id>")
def show_complete_blogpost(blog_id):
    selected_post = None
    # get selected bogpost by ID
    for current_post in post_objects:
        if current_post.id == blog_id:
            selected_post = current_post
    return render_template("post.html", post=selected_post)




if __name__ == "__main__":
    app.run(debug=True)
