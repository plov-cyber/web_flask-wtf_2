from flask import Flask, render_template, request
from loginform import LoginForm
from PIL import Image
from io import BytesIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
d = dict()
d['imgs'] = ['slide1.jpg', 'slide2.jpg', 'slide3.jpg']
cnt = 0


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    global d
    d['title'] = title
    return render_template('base.html', **d)


@app.route('/training/<prof>')
def profession(prof):
    global d
    d['title'] = 'Тренировка'
    d['prof'] = prof
    return render_template('training.html', **d)


@app.route('/list_prof/<list>')
def list_prof(list):
    global d
    profs = ['инженер-исследователь', 'пилот', 'экзобиолог', 'строитель', 'врач', 'астрогеолог', 'метеоролог',
             'штурман']
    d['profs'] = profs
    d['list'] = list
    d['title'] = 'Список профессий'
    return render_template('prof_list.html', **d)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    global d
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
    global d
    d['title'] = 'Размещение'
    d['team'] = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур', 'Тедди Сандерс', 'Шон Бин']
    return render_template('distribution.html', **d)


@app.route('/table/<sex>/<int:age>')
def table(sex, age):
    global d
    d['title'] = 'Цвет каюты'
    d['sex'] = sex
    d['age'] = age
    return render_template('table.html', **d)


@app.route('/galery', methods=['GET', 'POST'])
def galery():
    global cnt, d
    d['title'] = 'Красная планета'
    if request.method == 'GET':
        return render_template('galery.html', **d)
    elif request.method == 'POST':
        f = request.files['file']
        im = Image.open(BytesIO(f.read()))
        im.save(f'static/img/tmp{cnt}.png')
        d['imgs'].append(f'tmp{cnt}.png')
        cnt += 1
        return render_template('galery.html', **d)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
