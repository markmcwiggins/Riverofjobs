from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Example template


@app.route('/resumefront')
def resumefront():
    return render_template('resumefront.html')

@app.route('/tiny4')
def tiny4():
    return render_template('tiny4.html')  # This is the route for tiny4.html

if __name__ == '__main__':
    app.run(debug=True, port=5001)
