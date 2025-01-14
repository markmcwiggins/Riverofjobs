from flask import Flask, render_template, request

app = Flask(__name__)

# Route to render the form page (index.html)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resumefront')
def resumefront():
    return render_template('resumefront.html')

# Route to handle form submission and generate the resume
@app.route('/generate_resume', methods=['POST'])
def generate_resume():
    # Get form data
    name = request.form.get('name')
    email = request.form.get('email')
    skills = request.form.get('skills')
    experience = request.form.get('experience')

    # Split skills into a list (if user enters comma separated)
    skills_list = [skill.strip() for skill in skills.split(',')]
    
    # Pass data to the resume template
    return render_template('resume.html', name=name, email=email, skills=skills_list, experience=experience)

if __name__ == '__main__':
    app.run(debug=True)
