from flask import Flask, render_template, url_for


app = Flask(__name__)


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

@app.route('/list_prof/<list>')
def list_prof(list):
    params = {}
    params['list'] = list
    params['css_dest'] = url_for('static', filename='css/style.css')
    return render_template('prof_list.html', **params)




if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
