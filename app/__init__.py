import boto3

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_s3 import FlaskS3
from flask import render_template

app = Flask(__name__, instance_relative_config=True)

# Load the default configuration
app.config.from_object('config')
app.config.from_pyfile('development.py')
app.config['UPLOAD_FOLDER'] = 'app/static/img/upload'
app.config['FLASKS3_BUCKET_NAME'] = 'zappa-static-files-yuanyi'

s3 = boto3.resource('s3',
                    aws_access_key_id=app.config['AWS_ACCESS_KEY_ID'],
                    aws_secret_access_key=app.config['AWS_SECRET_ACCESS_KEY'])

client = boto3.client('lambda')

flask_s3 = FlaskS3(app)
bcrypt = Bcrypt(app)
flask_s3.init_app(app)


# Route for the welcome page
@app.route('/')
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


# Route for the signin page
@app.route('/signin')
def signin():
    return render_template('signin.html')


# Route for the register page
@app.route('/register')
def register():
    return render_template('register.html')


# Route for the verify page
@app.route('/verify')
def verify():
    return render_template('verify.html')


# Route for the home page
@app.route('/home')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()
