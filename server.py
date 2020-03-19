# -*- coding: utf-8 -*-

from flask import Flask, render_template,request,redirect
import csv
import smtplib
from email.message import EmailMessage
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
        send_email(data)
        return redirect('thankyou')
    else:
        return 'something went wrong'

def send_email(data):
    sender=data['email']
    title=data['title']
    body=data['body']
    
    email=EmailMessage()
    email['from']=sender
    email['to']='agahamsc@live.com'
    email['subject']=title
    
    email.set_content(body)
    
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('agahamtest@gmail.com', 'mijntest123')
        smtp.send_message(sender+"\n"+email)
        print('sent')

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
    
    