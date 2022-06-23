from flask import Flask, render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

from flask_bootstrap import Bootstrap

import os

app = Flask(__name__)
Bootstrap(app)
app.secret_key = os.environ["APP_SECRET_KEY"]


class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label="password", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='submit')

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        if email == 'admin@email.com' and password == "12345678":
            return redirect('/success')
        else:
            return redirect('denied')
    else:
        return render_template('login.html', form=form)


@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/denied')
def denied():
    return render_template('denied.html')




if __name__ == '__main__':
    app.run(debug=True)