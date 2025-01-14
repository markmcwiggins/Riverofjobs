#!/usr/bin/python3

import cgi

def main():
    # Get the form data
    form = cgi.FieldStorage()

    # Retrieve the lists of 'needs' and 'qualifications'
    needs = form.getlist('needs[]')
    qualifications = form.getlist('qualifications[]')

    # Print the HTTP header
    print("Content-type: text/html\n")

    # Start the HTML response
    print("<html>")
    print("<head><title>Form Submission Result</title></head>")
    print("<body>")

    # Output the submitted data
    print("<h1>Form Submission Result</h1>")
    print("<table border='1'>")
    print("<tr><th>Needs</th><th>Qualifications</th></tr>")

    # Loop through the 'needs' and 'qualifications' lists and display them
    for need, qualification in zip(needs, qualifications):
        print(f"<tr><td>{need}</td><td>{qualification}</td></tr>")

    print("</table>")
    print("</body></html>")

if __name__ == "__main__":
    main()
