
from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', "a", encoding='utf8') as outputfile:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        outputfile.write(f"\n{email}, {subject}, {message}")


def write_to_csv(data):
    with open('database.csv', mode="a", newline='') as outputfile2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(outputfile2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thanks.html')
        except Exception:
            return 'did not save to database'
    else:
        return "something went wrong"
