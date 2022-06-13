from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage():
	return render_template("homepage.html")


@app.route('/<color>')
def background(color):
	return render_template("colorpage.html", color=color)


if __name__ == '__main__':
	app.run()


