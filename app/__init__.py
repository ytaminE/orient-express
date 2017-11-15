import boto3

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_s3 import FlaskS3
from flask import render_template, redirect, url_for, request

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


# Route for the home page
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        code = request.form['code']

        s3.Object("test-yuanyi",'test.py').put(Body=code);
       
        response = client.invoke(
        ClientContext='MyApp', 
        FunctionName='run_python',
        InvocationType='Event',
        LogType='Tail',
        Payload='{"url":"https://s3.amazonaws.com/test-yuanyi/test.py"}',
        )
        
        print(response['Payload'].read())
    return render_template('home.html')


# Route for register page
@app.route('/register')
def register():
    return render_template('register.html')


# Route for register submit
@app.route('/register_submit', methods=['GET', 'POST'])
def register_submit():
    return redirect(url_for('login'))


# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # user = User.query.filter_by(userID=username).first()
        # if user is not None and user.is_correct_password(password):
        if username == "test" and password == "test":
            # login_user(user)
            return redirect(url_for('home'))
    # else:
    #         error = 'Username or password is incorrect. Please try again.'

    return render_template('login.html', error=error)


# Route for logout
@app.route('/logout')
def logout():
    return render_template('welcome.html')


if __name__ == '__main__':
    app.run()
