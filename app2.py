from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route('/')
def agenda():
    base = datetime.datetime.today()
    output = []
    for x in range(1, 36):
        output.append(base + datetime.timedelta(days=x))
    return render_template('testing.html', dates=output)


@app.route('/benis<var>')
def benis(var):
    print(var)
    return 'Success'


if __name__ == '__main__':
    app.run()