from flask import Flask, url_for, request
import os


app = Flask(__name__)


@app.route('/')
def mission():
    return 'Колонизация Марса'


@app.route('/index')
def slogan():
    return 'И на Марсе будут яблони цвести!'

@app.route('/results/<nickname>/<int:level>/<float:rating>')
def selection_results(nickname, level, rating):
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="Content-type" content="text/html;charset=UTF-8">
        <title>Результаты</title>
        <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
        <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
    </head>
    <body>
        <div class="container">
            <h1>Результаты отбора</h1>
            <h2>Пользователь {nickname} </h2>
            <h3>Этап отбора: {level}</h3>
            <h4>Рейтинг: {rating}</h4>
            <p class="alert alert-secondary">Не люблю bootstrap</p>
            <div class="concealed">HTML, CSS and JAVASCRIPT FOREVER</div>

        </div>
    </body>
    </html>"""

@app.route('/choice/<planet_name>')
def planet_choice(planet_name):
    if planet_name.lower() == 'земля':
        return f'{planet_name}? А вы откуда?'
    else:
        return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Выбор планеты</title>
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
                  </head>
                  <body>
                  <div class="container">
                    <h1>{planet_name}</h1>
                    <h2 class="alert alert-primary">Хороший вариант</h2>
                    <h3 class="alert alert-primary"\>Мы рассмотрим этот вариант</h3>
                    </div>
                  </body>
                </html>"""


@app.route('/promotion')
def promotion():
    return '''Человечество вырастает из детства.
    <br>
    Человечеству мала одна планета.
    <br>
    Мы сделаем обитаемыми безжизненные пока планеты.
    <br>
    И начнем с Марса!
    <br>
    Присоединяйся!'''


@app.route('/image_mars')
def greeting_with_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars_terraformation.gif')}" alt="Mars isn't showing up">
                    <div>Вот он какой, план терраформирования Марса!</div>
                  </body>
                </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars_terraformation.gif')}" alt="Mars isn't showing up">
                    <div class="alert alert-primary">Вот он какой, план терраформирования Марса!</div>
                    <a href="https://youtu.be/_mzoYSqAjCs" target="_blank">Yi Long Musk</a>
                  </body>
                </html>"""

@app.route('/load_photo', methods=['GET', 'POST'])
def load_photo():
    file = request.files['photo']
    if request.method == 'GET':
        return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="Content-type" content="text/html;charset=UTF-8">
    <title>PHOTO</title>
    <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
</head>
<body>
    <div class="container">
        <h1>Загрузка фотографии</h1>
        <br>
        <form action="#" method="post" enctype="multipart/form-data">
            <p class="text">Приложите вашу фотографию:</p>
            <div><input type="file" name="photo"></div>
            <div>
                <button type="submit">Принять</button>
                <button type="reset">Отменить</button>
            </div>
        </form>
    </div>
</body>
</html>'''
    elif request.method == 'POST':
        try:
            print(file)
            file.save(os.path.join('static/img/', 'pic.jpg'))
        except Exception:
            pass
        return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="Content-type" content="text/html;charset=UTF-8">
    <title>PHOTO</title>
    <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
</head>
<body>
    <div class="container">
        <h1>Загрузка фотографии</h1>
        <br>
        <form action="#" method="post" enctype="multipart/form-data">
            <p class="text">Приложите вашу фотографию:</p>
            <input type="file" name="photo">
            <img src="{url_for('static', filename='img/pic.jpg')}" alt="Вас не видно!">
            <div>
                <button type="submit">Принять</button>
                <button type="reset">Отменить</button>
            </div>
        </form>
    </div>
</body>
</html>'''


@app.route('/carousel')
def mars_landscape():
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="Content-type" content="text/html;charset=UTF-8">
    <title>PHOTO</title>
    <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js" integrity="sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T" crossorigin="anonymous"></script>
</head>
<body>
    <div class="container">
        <h1>Карусель ЮХУ</h1>
        
        <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
            <ol class="carousel-indicators">
              <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
              <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
              <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
            </ol>
            <div class="carousel-inner">
              <div class="carousel-item active">
                <img style="height: 600px" class="d-block w-100" src="static/img/mars1.jpg" alt="First slide">
              </div>
              <div class="carousel-item">
                <img style="height: 600px" class="d-block w-100" src="static/img/mars2.jpg" alt="Second slide">
              </div>
              <div class="carousel-item">
                <img style="height: 600px" class="d-block w-100" src="static/img/mars3.jpg" alt="Third slide">
              </div>
            </div>
            <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
              <span class="carousel-control-prev-icon" aria-hidden="true"></span>
              <span class="sr-only">Previous</span>
            </a>
            <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
              <span class="carousel-control-next-icon" aria-hidden="true"></span>
              <span class="sr-only">Next</span>
            </a>
          </div>
    </div>
</body>
</html>'''

@app.route('/astronaut_selection')
def astronaut_selection():
        return f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="Content-type" content="text/html;charset=UTF-8">
        <title>Анкета</title>
        <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
    </head>
    <body>
        <div class="container">
            <h1 class="application">Анкета отбора кандидатов</h1>
            <p class="application">Для участия в миссии</p>
            <form action="#" method="post" enctype="multipart/form-data">
                <div>
                    <p class="input-text"><input placeholder="Введите фамилию" type="text" name="surname"></p>
                    <p class="input-text"><input placeholder="Введите имя" type="text" name="name"></p>
                    <p class="input-email"><input placeholder="Введите адрес почты" type="text" name="email"></p>
                </div>
                <div>
                    <p class="text">Какое у вас образование?</p>
                    <select name="education">
                        <option value="high">Высшее</option>
                        <option value="primary">Среднее</option>
                        <option value="banana">Я банан</option>
                    </select>
                </div>
                <div class="profession">
                    <p class="text">Выберите Вашу профессию:</p>
                    <p><input class="input-checkbox" type="checkbox" name="engineer-explorer">инженер-исследователь</p>
                    <p><input class="input-checkbox" type="checkbox" name="pilot">пилот</p>
                    <p><input class="input-checkbox" type="checkbox" name="builder">строитель</p>
                    <p><input class="input-checkbox" type="checkbox" name="exobiologist">экзобиолог</p>
                    <p><input class="input-checkbox" type="checkbox" name="doctor">врач</p>
                    <p><input class="input-checkbox" type="checkbox" name="terraformation-engineer">инженер по терраформированию</p>
                    <p><input class="input-checkbox" type="checkbox" name="climatologist">климатолог</p>
                    <p><input class="input-checkbox" type="checkbox" name="astrogeologist">астрогеолог</p>
                    <p><input class="input-checkbox" type="checkbox" name="glaciologist">гляциолог</p>
                    <p><input checked class="input-checkbox" type="checkbox" name="programmer">программист</p>
                    <p><input class="input-checkbox" type="checkbox" name="">...</p>
                </div>
                <div class="sex">
                    <p class="text">Укажите пол</p>
                    <p><input class="input-radio" type="radio" name="sex" value="male">Мужской</p>
                    <p><input class="input-radio" type="radio" name="sex" value="female">Женский</p>
                </div>
                <div class="additional-info">
                    <p class="text">Почему Вы хотите принимаете участие в миссии?</p>
                    <textarea name="info" placeholder="Y?"></textarea>
                </div>
                <div class="photo">
                    <p class="text">Пришлите нам свою фотографию</p>
                    <input type="file" name="photo">
                </div>
                <p><input class="input-checkbox" type="checkbox" name="live_on_mars">Готовы ли вы остаться на Марсе?</p>
                <div>
                    <button type="submit">Принять</button>
                    <button type="reset">Сбросить</button>
                </div>
            </form>
        </div>
    </body>
    </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
