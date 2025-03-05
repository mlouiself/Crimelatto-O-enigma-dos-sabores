from flask import Flask, render_template

app = Flask(__name__, 
            static_folder='static', 
            template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    return render_template('Game.html')

@app.route('/sobre-o-jogo')
def sobre_o_jogo():
    return render_template('Sobre_o_jogo.html')

@app.route('/sobre')
def sobre():
    return render_template('Sobre.html')

if __name__ == '__main__':
    app.run(debug=True)