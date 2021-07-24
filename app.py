from flask import *
from flask import request
from flask import jsonify
from flask import Flask, jsonify, request, redirect
from textblob import TextBlob
import smtplib
import time
app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'


@app.route('/', methods=['GET', 'POST'])
def welcome():
	if request.method == 'GET':
		return render_template('home.html')
	else:
		feed = request.form['message-e4cc']
		gm = request.form['email-e4cc']
		feedback = TextBlob(feed).polarity
		# if feedback > 0:
		with smtplib.SMTP('smtp.gmail.com',587) as smtp:
			smtp.ehlo()
			smtp.starttls()
			smtp.ehlo()
			smtp.login('aster.customerservices@gmail.com','^^aster^^')
			subject = 'Your message was delivered perfectly!'
			subject1 = '7da b3t eshe' 
			body = 'Hey, Aster here. Thank you for sending us a message, it will be read as fast as possible, in case it is urgent. Pleae call +97253308990'
			msg = f'subject: {subject}\n\n{body}'
			msg1 = f'subject: {subject1}\n\n{feed}'
			smtp.sendmail('','aster.customerservices@gmail.com',msg1)
			smtp.sendmail('',gm,msg)
			return render_template("main.html")



@app.route('/Donate.html')
def donate():
	return render_template('Donate.html')
	


@app.route('/Home.html', methods=['GET', 'POST'])
def w1231():
	if request.method == 'GET':
		return render_template('home.html')
	else:
		feed = request.form['message-e4cc']
		gm = request.form['email-e4cc']
		feedback = TextBlob(feed).polarity
		# if feedback > 0:
		with smtplib.SMTP('smtp.gmail.com',587) as smtp:
			smtp.ehlo()
			smtp.starttls()
			smtp.ehlo()
			smtp.login('aster.customerservices@gmail.com','^^aster^^')
			subject = 'Your message was delivered perfectly!'
			subject1 = '7da b3t eshe' 
			body = 'Hey, Aster here. Thank you for sending us a message, it will be read as fast as possible, in case it is urgent. Pleae call +97253308990'
			msg = f'subject: {subject}\n\n{body}'
			msg1 = f'subject: {subject1}\n\n{feed}'
			smtp.sendmail('','aster.customerservices@gmail.com',msg1)
			smtp.sendmail('',gm,msg)
			return render_template("main.html")

	# # else:
	# 	with smtplib.SMTP('smtp.gmail.com',587) as smtp:
	# 		smtp.ehlo()
	# 		smtp.starttls()
	# 		smtp.ehlo()
	# 		smtp.login('facial.recognition.feedback@gmail.com','faceface123')
	# 		subject = 'Thank you for reviewing our website!!'
	# 		subject1 = 'mmm, some one was in a bad mood'
	# 		body = 'Hey, we noticed that you did not like the website that much, but, we are here for you... just tell us what do you think will make this website amazing and suitable for you. Your opinion is our top priority;)!!!'
	# 		msg = f'subject: {subject}\n\n{body}'
	# 		msg1 = f'subject: {subject1}\n\n{feed}'
	# 		smtp.sendmail('','facial.recognition.feedback@gmail.com',msg1)
	# 		smtp.sendmail('',gm,msg)
	# 		return render_template("main.html")

@app.route('/Shop.html', methods=['GET', 'POST'])
def Shop():
	if request.method == 'GET':
		return render_template('Shop.html')
	else:
		phone = request.form['phone-5bb3']
		Name = request.form['name-b495']
		gm = request.form['email-b495']
		# if feedback > 0:
		with smtplib.SMTP('smtp.gmail.com',587) as smtp:
			smtp.ehlo()
			smtp.starttls()
			smtp.ehlo()
			smtp.login('aster.shop4u@gmail.com','^^aster^^')
			subject = 'Your order has been sent, excpect a fun and happy phone call soon'
			subject1 = gm
			body = 'Hey, Aster here. Thank you for buying  from aster, you are helping us and helping the society, THANK YOU. For any additional questions/Concerns please call +97253308990'
			msg = f'subject: {subject}\n\n{body}'
			msg1 = f'subject: {subject1}\n\n{phone}'
			smtp.sendmail('','aster.shop4u@gmail.com',msg1)
			smtp.sendmail('',subject1,msg)
			return render_template("shop.html")	




if __name__ == '__main__':
  app.run(debug=True)