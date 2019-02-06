from flask import Flask, request
import sqlite3

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "welcome"


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        conn = sqlite3.connect("UserManagementDB.db")
        cursor = conn.execute('select * from LoginImformation where UserName=? and Password=?', [username, password])
        if cursor.fetchone() is not None:
            return 'Successfully login'
        else:
            return 'Please try again'
        conn.close()

    else:
        user_info = request.args.get('user')
        return "Welcome back %s" % user_info


@app.route('/register', methods=['POST'])
def register_page():
    username = request.form.get('username')
    password = request.form.get('password')
    conn = sqlite3.connect("UserManagementDB.db")
    conn.execute('insert into LoginImformation (UserName,Password) values (?,?)', [username,password])
    conn.commit()
    conn.close()

    return 'Welcome %s, you have successfully registered.' % username


@app.route('/unregister', methods=['POST'])
def unregister_page():
    username = request.form.get('username')
    conn = sqlite3.connect("UserManagementDB.db")
    conn.execute("delete from LoginImformation where UserName=?", [username])
    conn.commit()
    conn.close()
    return 'You have been successfully deleted!'


@app.route('/update', methods=['POST'])
def update_page():
    password = request.form.get('password')
    username = request.form.get('username')
    conn = sqlite3.connect("UserManagementDB.db")
    conn.execute("update LoginImformation set Password=? where UserName=?",[password,username])
    conn.commit()
    conn.close()
    return 'Successfully update your password'


if __name__ == '__main__':
    app.run()
