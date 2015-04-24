from flask import render_template
from app import app

@app.route("/")	
@app.route("/index")
def index():
	user = {"nickname" : "Lvpin"}
	posts = [
				{
					'author':{'nickname' : 'bobo'},
			 		'body' : 'stupid'
				},
				{
					'author':{'nickname' : 'monica'},
					'body' : 'wisdom'
				}
			]
	return render_template('index.html' , title = 'home' , user = user , posts = posts)