from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    current_year = datetime.now().year
    YOUR_NAME = "Marion ROBERT"
    return render_template("index.html", year=current_year, name=YOUR_NAME)


@app.route("/guess/<name>")
def guess(name):
    genderize_response = requests.get(f"https://api.genderize.io?name={name.lower()}")
    genderize_data = genderize_response.json()
    gender = genderize_data["gender"]
    agify_reponse = requests.get(f"https://api.agify.io/?name={name.lower()}")
    agify_data = agify_reponse.json()
    age = agify_data["age"]
    return render_template("guess.html", name=name, gender=gender, age=age)


if __name__ == '__main__':
    app.run(debug=True)

