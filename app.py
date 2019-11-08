from flask import Flask, render_template
import datetime
app = Flask(__name__)


@app.route('/agenda')
def agenda():
    base = datetime.datetime.today()
    output = []
    for x in range(1, 36):
        output.append(base + datetime.timedelta(days=x))
    return render_template('agenda.html', tijd='tijd', maand='maand', dates=output)


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
