from flask import Flask, render_template
from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
d = dict()


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    d['title'] = title
    d['prof'] = ''
    return render_template('base.html', **d)


@app.route('/training/<prof>')
def profession(prof):
    d['title'] = 'Тренировка'
    d['prof'] = prof
    return render_template('training.html', **d)


@app.route('/list_prof/<list>')
def list_prof(list):
    profs = ['инженер-исследователь', 'пилот', 'экзобиолог', 'строитель', 'врач', 'астрогеолог', 'метеоролог',
             'штурман']
    d['profs'] = profs
    d['list'] = list
    d['title'] = 'Список профессий'
    return render_template('prof_list.html', **d)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    d['title'] = 'Анкета'
    d['surname'] = 'Watny'
    d['name'] = 'Mark'
    d['education'] = 'выше среднего'
    d['profession'] = 'штурман марсохода'
    d['sex'] = 'male'
    d['motivation'] = 'Всегда мечтал застрять на Марсе!'
    d['ready'] = 'True'
    return render_template('auto_answer.html', **d)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        pass
    return render_template('login.html', title='Аварийный доступ', form=form)


@app.route('/distribution')
def distribute():
    d['title'] = 'Размещение'
    d['team'] = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур', 'Тедди Сандерс', 'Шон Бин']
    return render_template('distribution.html', **d)


@app.route('/table/<sex>/<int:age>')
def table(sex, age):
    d['title'] = 'Цвет каюты'
    d['sex'] = sex
    d['age'] = age
    return render_template('table.html', **d)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
