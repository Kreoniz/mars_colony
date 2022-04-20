from flask import Flask, render_template, url_for, redirect
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import os
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import json


basedir = os.path.abspath(os.path.dirname(__file__)) + '/static'


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'uploads') # you'll need to create a folder named uploads


photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB

class PictureForm(FlaskForm):
    photo = FileField(validators=[FileAllowed(photos, 'Image only!'), FileRequired('File was empty!')])
    submit = SubmitField('Upload')


@app.route('/<name>')
@app.route('/index/<name>')
def index_dynamic_title(name):
    params = {}
    params['title'] = name
    params['css_dest'] = url_for('static', filename='css/style.css')
    return render_template('base.html', **params)

@app.route('/training/<prof>')
def training(prof):
    params = {}
    params['title'] = 'Расписание тренировок'
    params['css_dest'] = url_for('static', filename='css/style.css')
    params['prof'] = prof
    if 'инженер' in prof.lower() or 'строитель' in prof.lower():
        params['text'] = 'Инженерные тренажеры'
        params['pic_dest'] = url_for('static', filename='img/spacecraft2.jpg')
    else:
        params['text'] = 'Научные симуляторы'
        params['pic_dest'] = url_for('static', filename='img/spacecraft1.jpg')
    
    return render_template('training.html', **params)

@app.route('/login')
def login():
    params = {}
    params['title'] = 'Аварийный доступ'
    params['css_dest'] = url_for('static', filename='css/style.css')
    return render_template('emergency_login.html', **params)

@app.route('/member')
def member():
    params = {}
    params['title'] = 'Рандомный чел, позитивный'
    params['css_dest'] = url_for('static', filename='css/style.css')
    json_data = open('templates/members.json')
    data = json.load(json_data)
    return render_template('member.html', **params, data=data)

@app.route('/distribution')
def distribution():
    params = {}
    params['title'] = 'По каютам!'
    params['css_dest'] = url_for('static', filename='css/style.css')
    params['user_list'] = ['Elon Musk', 'Jeff Bezos', 'Michael Jordan', 'Lex Fridman', 'Tim Urban', 'Mark Zuckerberg']
    return render_template('cabins.html', **params)

@app.route('/table/<sex>/<int:age>')
def cabin_color(sex, age):
    params = {}
    params['title'] = 'Цвет каюты'
    params['css_dest'] = url_for('static', filename='css/style.css')
    params['sex'] = sex
    params['age'] = age
    return render_template('cabin_color.html', **params)

@app.route('/list_prof/<list>')
def list_prof(list):
    params = {}
    params['list'] = list
    params['css_dest'] = url_for('static', filename='css/style.css')
    return render_template('prof_list.html', **params)

@app.route('/galery', methods=['GET', 'POST'])
def galery():
    form = PictureForm()

    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = photos.url(filename)
        with open('images.txt', 'a') as f:
            f.write(filename + '\n')
    else:
        file_url = None

    params = {}
    params['title'] = 'galery'
    params['css_dest'] = url_for('static', filename='css/style.css')
    with open('images.txt', 'rt') as f:
        data = [url_for('static', filename='uploads/' + line.strip()) for line in f.readlines()]
        print(data)
    params['uploaded_images'] = data
    return render_template('mars_landscape.html', **params, form=form, file_url=file_url)


@app.route('/auto_answer')
@app.route('/answer')
def answer():
    params = {
        'title': 0,
        'surname': 'Sanderson',
        'name': 'Grant',
        'education': 'Bachelor of Education',
        'profession': 'Программист',
        'sex': 'Мужской',
        'motivation': 'На звездочки посмотреть',
        'ready': True   
    }
    params['title'] = 'Анкета'
    params['css_dest'] = url_for('static', filename='css/style.css')

    return render_template('auto_answer.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
