import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    re = open("index.html").read()
    return re


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
