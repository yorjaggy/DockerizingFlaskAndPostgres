from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime,timedelta
import os
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://docker:docker@192.168.160.129:5432/docker'
db = SQLAlchemy(app)

if db is None:
	@app.route('/')
	def index():
	    return "DB not found!"
else:
	#--------------------------------------------------------------------
	class Word (db.Model):
	    __tablename__ = "word"
	    id = db.Column('id', db.Integer, primary_key=True)
	    word = db.Column('word', db.Unicode)
	    creation_date = db.Column('creation_date', db.Date, default=datetime.utcnow)
	#--------------------------------------------------------------------
	db.create_all()

	@app.route('/')
	def index():
	    words=Word.query.all()
	    return render_template('list.html',words=Word.query.all())

	@app.route('/test')
	def test():
	    toAdd = Word(word=u'Mi Primera Palabra') 
	    db.session.add(toAdd)
	    db.session.commit()
	    return toAdd.word + " agregada."

	@app.route('/<palabra>')
	def addingWord(palabra):
	    toAdd = Word(word=palabra)
	    db.session.add(toAdd)
	    db.session.commit()
	    return palabra + " agregada."


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
