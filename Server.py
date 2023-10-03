from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

def write_to_file(data):
    with open('database.txt', 'a') as db:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = db.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as db:
        email = data['email']
        subject = data['subject']
        message = data['message']
        writer = csv.writer(db, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([email,subject,message])

@app.route('/<string:page_name>') # dynamically get sites
def homepage(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            #email = request.form['email'] - get info about email
            data = request.form.to_dict() # get data into dict
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to db'
    else:
        return 'Something went wrong'