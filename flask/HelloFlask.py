from flask import Flask,request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "welcome"


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == '123':
            return 'Successfully login'
        else:
            return 'Please try again'
    else:
        user_info = request.args.get('user')
        return "Welcome back %s" % user_info


@app.route('/register', methods=['POST'])
def register_page():
    username = request.form.get('username')
    password = request.form.get('password')

    # store user information to the database
    return 'Welcome %s, you have successfully registered.' % username
    
        
if __name__ == '__main__':
    app.run()
