# -*- coding: utf-8 -*-

from flask import Flask, render_template,request,redirect
import csv
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name+".html")

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=="POST":
        data=request.form.to_dict()
        
        write_to_csv(data)
        return redirect('thankyou')
    else:
        return 'something went wrong'


def write_to_csv(data):
    with open('database.csv',mode='a') as database:
        email=data['email']
        title=data['title']
        body=data['body']
        csv_writer=csv.writer(database, delimiter=",", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,title,body])

'''
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/components')
def components():
    return render_template('components.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/work')
def work():
    return render_template('work.html')
@app.route('/works')
def works():
    return render_template('works.html')
'''
if __name__ == '__main__':
    app.run()
    
    