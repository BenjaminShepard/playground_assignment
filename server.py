from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def play():
    return render_template('index.html', times=3, color='blue')

@app.route('/play/<int:x>')
def play_x_squares(x):
    return render_template('index.html', times=x, color='blue')

@app.route('/play/<int:x>/<color>')
def play_x_squares_and_color(x, color):
    return render_template('index.html', times=x, color=color)


if __name__=="__main__":
    app.run(debug=True)