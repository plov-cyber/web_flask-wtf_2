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
    return render_template('training.html', **d)


@app.route('/list_prof/<list>')
def list_prof(list):
    d = dict()
    profs = ['инженер-исследователь', 'пилот', 'экзобиолог', 'строитель', 'врач', 'астрогеолог', 'метеоролог',
             'штурман']
    d['profs'] = profs
    d['list'] = list
    d['title'] = 'Список профессий'
    return render_template('prof_list.html', **d)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    d = dict()
    d['title'] = 'Анкета'
    d['surname'] = 'Watny'
    d['name'] = 'Mark'
    d['education'] = 'выше среднего'
    d['profession'] = 'штурман марсохода'
    d['sex'] = 'male'
    d['motivation'] = 'Всегда мечтал застрять на Марсе!'
    d['ready'] = 'True'
    return render_template('auto_answer.html', **d)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
