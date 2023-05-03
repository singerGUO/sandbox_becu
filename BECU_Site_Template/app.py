from flask import Flask, render_template, request
import requests


app = Flask(__name__)


REST_URL = "http://20.245.192.233/tasks/list"
HEADERS = {"Authorization": "Bearer 8rLGxB7J4EZkK2qLdQb0aw"}


@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def get_data():
    response = requests.get(REST_URL, headers=HEADERS)
    data = response.json()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run()
