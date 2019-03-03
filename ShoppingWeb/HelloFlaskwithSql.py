from flask import Flask, request, session, url_for, redirect, render_template
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlite3


app = Flask(__name__)

app.secret_key = 'hhsskke3!/sddcd!?ncttenthebest!'

Base = declarative_base()


class User(Base):

    # table name
    __tablename__ = 'userinformation'

    userid = Column(Integer, primary_key=True)
    username = Column(String(20))
    password = Column(String(20))


# init DB connection
engine = create_engine('mysql+mysqlconnector://root:cluo0626@@localhost:3306/MyProject')

# create DBSession
DBSession = sessionmaker(bind=engine)


@app.route('/')
def hello_world():
    return render_template('welcome.html')


@app.route('/info')
def user_info():
    if 'username' in session:
        return 'Welcome ' + session['username']
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':

        session['username'] = request.form.get('username')
        un = request.form.get('username')
        pw = request.form.get('password')

        sqlsession = DBSession()
        user = sqlsession.query(User).filter(User.username == un and User.password == pw).all()
        if user is not None:
            return redirect(url_for('user_info'))
        else:
            return render_template('login.html')

        sqlsession.close()

    else:

        user_info = request.args.get('username')
        return "Welcome back %s" % user_info


@app.route('/register', methods=['POST'])
def register_page():

    un = request.form.get('username')
    pw = request.form.get('password')

    sqlsession = DBSession()
    new_user = User(username=un, password=pw)
    sqlsession.add(new_user)
    sqlsession.commit()
    sqlsession.close()

    return redirect(url_for('user_info'))
    #return 'Welcome %s, you have successfully registered.' % un


@app.route('/unregister', methods=['POST'])
def unregister_page():
    un = request.form.get('username')

    sqlsession = DBSession()
    del_user = User(username=un)
    sqlsession.delete(del_user)
    sqlsession.commit()
    sqlsession.close()

    return '<h1>You have been successfully deleted!<h1>'


@app.route('/logout')
def log_out():

    session.pop('username', None)
    return redirect(url_for('hello_world'))


@app.route('/update', methods=['POST'])
def update_page():
    pw = request.form.get('password')
    un = request.form.get('username')

    sqlsession = DBSession()
    del_user = User(username=un, password=pw)
    sqlsession.delete(del_user)
    sqlsession.commit()
    sqlsession.close()

    return 'Successfully update your password'


if __name__ == '__main__':
    app.run()




