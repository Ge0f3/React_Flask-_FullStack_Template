#server
from flask import Flask,render_template

app = Flask(__name__, static_folder="../static/dist", template_folder="../static")

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/home')
def home():
	return "Heloo welcome home !"

if __name__ == '__main__':
	main()