from flask import Flask

app = Flask(__name__)

@app.route('/tiny4')
def tiny():
    return "Route is Working"


if __name__ == '__main__':
    app.run(debug=True)
