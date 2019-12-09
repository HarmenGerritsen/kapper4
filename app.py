from flask import Flask, render_template
from loguru import logger
import datetime
app = Flask(__name__)


@app.route('/agenda')
def agenda():
    base = datetime.date.today()
    output = []
    for x in range(1, 36):
        output.append(base + datetime.timedelta(days=x))
    return render_template('agenda.html', tijd='tijd', maand='maand', dates=output)


@app.route('/<var>')
def benis(var):
    print(var)
    return render_template('succes.html', datum=var)


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/team')
def team():
    return render_template('team.html')


if __name__ == '__main__':
    app.run()
