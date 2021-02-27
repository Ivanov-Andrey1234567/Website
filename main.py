from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/about/')
@app.route('/about/<username>')
def about(username='me'):
    return f'All about {escape(username)}'


if __name__ == '__main__':
    app.run()