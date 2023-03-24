from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/5199defdf9a60731d580").json()
all_posts = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    all_posts.append(post_obj)


@app.route('/')
def get_all_posts():
    return render_template("index.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
