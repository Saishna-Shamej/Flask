from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

# Flask mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'saishna2002@gmail.com'
app.config['MAIL_PASSWORD'] = 'wrtqebxhjjtokwsc'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# instantiate the Mail class
mail = Mail(app)

# configure the Message class object and send the mail from a url
@app.route('/')
def index():
    msg = Message('subject', sender = 'saishna2002@gmail.com', recipients=['saishna05@gmail.com'])
    msg.body = 'hi, this is the mail sent by using the flask web application'
    return "Mail Sent, Please check the mail id"

if __name__ == '__main__':
    app.run(debug = True)