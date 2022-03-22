from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/<name>')
@app.route('/index/<name>')
def index_dynamic_title(name):
    params = {}
    print(name)
    params['title'] = name
    params['css_dest'] = url_for('static', filename='css/style.css')
    return render_template('base.html', **params)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
