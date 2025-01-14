from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')  # Render the HTML form

@app.route('/submit', methods=['POST'])
def submit():
    # Get data from the form
    needs = request.form.getlist('needs[]')
    qualifications = request.form.getlist('qualifications[]')

    # For now, print the data to the console
    print("Needs:", needs)
    print("Qualifications:", qualifications)

    # Return a message to the user after form submission
    return "Form Submitted Successfully!"

if __name__ == '__main__':
    app.run(debug=True)
