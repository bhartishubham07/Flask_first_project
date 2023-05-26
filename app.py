from flask import Flask

FAI = Flask(__name__)

@FAI.route('/wish')
def wish():
    return '<center><h1>Hi...Good Evening!!!</h1></center>'

@FAI.route('/sample')
def sample():
    return '<center><h1>Hi...How are You!!!</h1></center>'


if __name__ == '__main__':
    FAI.run(debug=True)