from flask import Flask, render_template, request, send_file
from pylatex import Document, Section, Tabular, Command
from pylatex.utils import bold, NoEscape
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        latex_code = generate_latex(request.form)
        with open('output.tex', 'w') as f:
            f.write(latex_code)
        os.system('pdflatex output.tex')
        return send_file('output.pdf', as_attachment=True)
    return render_template('form.html')

def generate_latex(form_data):
    doc = Document()
    doc.packages.append(NoEscape(r'\usepackage{xcolor}'))
    doc.packages.append(NoEscape(r'\usepackage{colortbl}'))

    # Personal Information
    doc.preamble.append(Command('title', form_data['job-title']))
    doc.preamble.append(Command('author', form_data['user-name']))
    doc.append(NoEscape(r'\maketitle'))

    with doc.create(Section('Personal Information')):
        doc.append(f"Name: {form_data['user-name']}")
        doc.append(f"\nAddress: {form_data['address']}, {form_data['city']}, {form_data['state']} {form_data['zip']}")
        doc.append(f"\nEmail: {form_data['email']}")
        doc.append(f"\nCompany: {form_data['company']}")

    # Needs and Qualifications
    with doc.create(Section('Needs and Qualifications')):
        with doc.create(Tabular('|p{0.45\\textwidth}|p{0.45\\textwidth}|')) as table:
            table.add_hline()
            table.add_row((bold('Needs'), bold('Qualifications')))
            table.add_hline()
            needs = form_data.getlist('needs[]')
            qualifications = form_data.getlist('qualifications[]')
            for i, (need, qual) in enumerate(zip(needs, qualifications)):
                color = 'blue!25' if i % 2 == 0 else 'yellow!25'
                table.add_row((
                    NoEscape(r'\cellcolor{' + color + '}' + need),
                    NoEscape(r'\cellcolor{' + color + '}' + qual)
                ))
                table.add_hline()

    # Past Jobs
    with doc.create(Section('Past Jobs')):
        job_names = form_data.getlist('job_name[]')
        contract_houses = form_data.getlist('contract_house[]')
        roles = form_data.getlist('role[]')
        locations = form_data.getlist('location[]')
        dates = form_data.getlist('dates[]')
        
        with doc.create(Tabular('|p{0.45\\textwidth}|p{0.45\\textwidth}|')) as table:
            table.add_hline()
            table.add_row((bold('Job Details'), bold('Additional Information')))
            table.add_hline()
            for i, (job, contract, role, location, date) in enumerate(zip(job_names, contract_houses, roles, locations, dates)):
                color = 'blue!25' if i % 2 == 0 else 'yellow!25'
                table.add_row((
                    NoEscape(r'\cellcolor{' + color + '}' + f"Job: {job}\nRole: {role}"),
                    NoEscape(r'\cellcolor{' + color + '}' + f"Contract House: {contract}\nLocation: {location}\nDates: {date}")
                ))
                table.add_hline()

    return doc.dumps()

if __name__ == '__main__':
    app.run(debug=True)
