import os
from flask import Flask, render_template, request

__author__ = 'ibininja'

app = Flask(__name__)


APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def index():
	return render_template("upload.html")

@app.route("/upload", methods=['POST'])
def upload():
	target = os.path.join(APP_ROOT, 'static')

	if not os.path.isdir(target):
		os.mkdir(target)

	for file in request.files.getlist("file"):
		filename = file.filename
		destination = "/".join([target, filename])
		file.save(destination)
	return render_template("complete.html")





@app.route("/example")
def example():
	hists = os.listdir('static')
	hists = [file for file in hists]
	return render_template('example.html', hists = hists)


if __name__=="__main__":
	app.run(port=4555,debug=True)