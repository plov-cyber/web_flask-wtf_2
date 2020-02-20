from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    d = dict()
    d['title'] = title
    return render_template('base.html', **d)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
