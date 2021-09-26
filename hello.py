from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from datetime import datetime
from flask_moment import Moment

app = Flask(__name__)

bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/')
def index():
    web_name = 'Adam'
    return render_template('index.html',
                           current_time=datetime.utcnow(),
                           name=web_name)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)

