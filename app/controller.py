# _*_ conding:utf-8 _*_
from flask import render_template, url_for, request, redirect
from app import app
from model.fuckingModel import FirstClass


@app.route('/')
def goIndex():
    shitdata = FirstClass.all()
    return render_template('index.html', shitDataAllShow=shitdata)


@app.route('/gofuckingindex', methods=['GET', 'POST'])
def goingText():
    if request.method == 'POST':
        wtf_text_data = request.form.get('textInput')

        upload = FirstClass()
        upload.setText(wtf_text_data)
        upload.put()

    return redirect(url_for('goIndex'))


@app.route('/likeFunction/<key>')
def likePlusFunction(self):
	iDoNotKnowWhoYouAre = db.get(key)


	return render_template('url_for(/)')
