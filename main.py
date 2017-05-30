from flask import Flask, request, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return


@app.route('/all-school')
def everyone():
    return


@app.route('/mentors-by-country')
def country():
    return


@app.route('/contacts')
def contacts():
    return


@app.route('/applicants')
def applicants():
    return


@app.route('/applicants-and-mentors')
def apps_ments():
    return


if __name__ == '__main__':
    app.run(debug=True)