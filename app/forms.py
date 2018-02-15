from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email


class MyForm(FlaskForm):
 name = StringField('name',validators=[DataRequired()])
 email=StringField('email',validators=[DataRequired(), Email()])
 subject=StringField('subject',validators=[DataRequired()])
 messages=TextAreaField('message',validators=[DataRequired()])
 