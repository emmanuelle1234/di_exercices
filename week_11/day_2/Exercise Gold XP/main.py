from flask import Flask, render_template, render_template_string
import datetime
from random import randint

app = Flask(__name__)

@app.route('/')
def homepage():
	current_date = datetime.date.today()
	current_time = datetime.datetime.now().strftime("%H : %M : %S")
	if '08:00:00' <= current_time < '13:00:00':
		message = 'Good morning!'
	elif '13:00:00' <= current_time < '17:00:00':
		message = 'Good afternoon!'
	elif '17:00:00' <= current_time < '21:00:00':
		message = 'Good evening!'
	elif '21:00:00' <= current_time < '08:00:00':
		message = 'Good night!'
	return render_template("index.html", current_date=current_date, current_time=current_time, message=message)

@app.route('/<int:number>')
def random(number):
	random_var = randint(1, 100)
	message = ""
	template = '''
			<html>
				<head>
					<title>{{ number }}</title>
				</head>
				<body>
					<h1>{{ message }}</h1>
				</body>
			</html>
		'''
	if 1 < number > 101:
		raise ValueError('Number should be chosen between 1 and 100')
	else:
		if random_var == number:
			message = "Congratulations!"
	html = render_template_string(template, message=message)
	return html


if __name__ == '__main__':
	app.run(debug=True)





