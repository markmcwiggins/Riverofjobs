#!/usr/bin/python3

import cgi

# Create the FieldStorage object
form = cgi.FieldStorage()

# Get form data
needs = form.getvalue("needs", "Not Provided")
qualifications = form.getvalue("qualifications", "Not Provided")

# Output headers and form data
print("Content-Type: text/html")
print()
print("<html><body>")
print("<h2>Form Submission Results</h2>")
print(f"<p>Need: {needs}</p>")
print(f"<p>Qualification: {qualifications}</p>")
print("</body></html>")
