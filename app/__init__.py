from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hey'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525'
app.config['MAIL_USERNAME'] = 'bc06c750ce2d7d'
app.config['MAIL_PASSWORD'] = '92226bea6d28f3'

mail = Mail(app)
from app import views