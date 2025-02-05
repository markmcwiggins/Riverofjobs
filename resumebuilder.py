from flask import Flask, request, render_template, send_file
import subprocess
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('resume_form.html')

@app.route('/generate_resume', methods=['POST'])
def generate_resume():
    # Extract form data
    name = request.form['name']
    job_title = request.form['job_title']
    company = request.form['company']
    address = request.form['address']
    city = request.form['city']
    state = request.form['state']
    zip_code = request.form['zip']
    email = request.form['email']
    
    needs = request.form.getlist('needs[]')
    qualifications = request.form.getlist('qualifications[]')
    
    job_names = request.form.getlist('job_name[]')
    job_companies = request.form.getlist('job_company[]')
    contract_houses = request.form.getlist('contract_house[]')
    roles = request.form.getlist('role[]')
    locations = request.form.getlist('location[]')
    start_dates = request.form.getlist('start_date[]')
    end_dates = request.form.getlist('end_date[]')

    # Generate LaTeX content
    latex_content = r"""
\documentclass{article}
\usepackage[margin=1in]{geometry}
\usepackage{tabularx}
\usepackage{booktabs}
\usepackage{hyperref}

\begin{document}

\begin{center}
    \textbf{%s}\\
    %s at %s\\
    %s, %s, %s %s\\
    \href{mailto:%s}{%s}
\end{center}

\section{Needs and Qualifications}

\begin{tabularx}{\textwidth}{X|X}
\toprule
\textbf{Needs} & \textbf{Qualifications} \\
\midrule
""" % (name, job_title, company, address, city, state, zip_code, email, email)

    for need, qualification in zip(needs, qualifications):
        if need and qualification:
            latex_content += f"{need} & {qualification} \\\\\n"

    latex_content += r"""
\bottomrule
\end{tabularx}

\section{Job History}

\begin{tabularx}{\textwidth}{X|X|X|X|X|X}
\toprule
\textbf{Job Name} & \textbf{Company} & \textbf{Contract House} & \textbf{Role} & \textbf{Location} & \textbf{Dates} \\
\midrule
"""

    for job, company, contract, role, location, start_date, end_date in zip(job_names, job_companies, contract_houses, roles, locations, start_dates, end_dates):
        if job and company and role and location and start_date and end_date:
            latex_content += f"{job} & {company} & {contract} & {role} & {location} & {start_date} -- {end_date} \\\\\n"

    latex_content += r"""
\bottomrule
\end{tabularx}

\end{document}
"""

    # Write LaTeX content to file
    with open('resume.tex', 'w', encoding='utf-8') as file:
        file.write(latex_content)

    # Compile LaTeX to PDF
    subprocess.run(['pdflatex', '-interaction=nonstopmode', 'resume.tex'])

    # Send the generated PDF file
    return send_file('resume.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
