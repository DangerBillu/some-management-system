from flask_wtf import FlaskForm
from wtform import StringField, PasswordField, SubmitField 
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError

class loginForm(FlaskForm):
    email = StringField("Email", Validators= [DataRequired(), Email()])
    password = PasswordField("Password", Validators= [DataRequired()])
    submit = SubmitField ("Login")


class registrationForm(FlaskForm):
    email= StringField("Email", validators=[DataRequired(), Email()])
    usename = StringField ("Username", validators= [DataRequired(), ])
    password= PasswordField("Password", validators= [DataRequired(), EqualTo("password_confirm", message= "Passwords Don't Mach")])    
    password_confirm = PasswordField("Confirm Password", validators= [DataRequired()])
    submit = SubmitField("Register")

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Your email has been already registered!")
    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("The username is already in use")
        