from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email


class MyForm(FlaskForm):
 name = StringField('name',validators=[DataRequired()])
 email=StringField('email',validators=[DataRequired(), Email()])
 subject=StringField('subject',validators=[DataRequired()])
 messages=StringField('message',validators=[DataRequired()])
 