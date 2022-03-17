from flask import Flask, url_for
import os
print(os.listdir())

app = Flask(__name__)


@app.route('/')
def mission():
    return 'Колонизация Марса'


@app.route('/index')
def slogan():
    return 'И на Марсе будут яблони цвести!'


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

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
