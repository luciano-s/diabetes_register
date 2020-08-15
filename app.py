import flask
from datetime import datetime
from markupsafe import escape

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/cafe')
def cafe():
    return flask.render_template('cafe.html')


@app.route('/almoco')
def almoco():
    return flask.render_template('almoco.html')

@app.route('/lanche')
def lanche():
    return flask.render_template('lanche.html')

@app.route('/jantar')
def jantar():
    return flask.render_template('jantar.html')

@app.route('/dormir')
def dormir():
    return flask.render_template('dormir.html')

@app.route('/madrugada')
def madrugada():
    return flask.render_template('madrugada.html')


@app.route('/cadastra/<tipo>', methods=['POST', 'GET'])
def cadastrar_dados(tipo):
    
    tipo = {f'type:{escape(tipo)}'}
    result = flask.request.form
    stores_data(result)

    return flask.render_template('index.html')

def stores_data(data):
    
    with open('data/data.txt', 'a+') as f:
        f.write(f'date:{str(datetime.now())}, ')
        for key, value in data.items():
            if key.lower() != 'submit':
                string = f'{key}:{value}, '
                f.write(string)
        f.write('\n')

if __name__ == '__main__':
    app.run(debug=False)