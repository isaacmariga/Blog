from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])  
    submit = SubmitField('Post')


class CommentForm(FlaskForm):
    comment_content =  TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Submit')

class UpdateAccountForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
  email =  StringField('Email', validators=[DataRequired(), Email()])
  picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
  submit = SubmitField('Update')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')