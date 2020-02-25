from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    d = dict()
    d['title'] = title
    d['prof'] = ''
    return render_template('base.html', **d)


@app.route('/training/<prof>')
def profession(prof):
    d = dict()
    d['title'] = 'Тренировка'
    d['prof'] = prof
    return render_template('base.html', **d)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
