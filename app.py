from flask import flask, render_template

app = flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/')
def game():
    return render_template('Game.html')

@app.route('/')
def game():
    return render_template('Sobre.html')

@app.route('/')
def about_game():
    return render_template('Sobre_o_jogo.html')

if __name__ == '__main__':
    app.run(debug=True)