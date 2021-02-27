from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/section/films')
def get_section_films():
    return render_template('Films.html')


@app.route('/section/books')
def get_section_books():
    return render_template('Books.html')


@app.route('/section/video_games')
def get_section_video_games():
    return render_template('Video_games.html')


if __name__ == '__main__':
    app.run()