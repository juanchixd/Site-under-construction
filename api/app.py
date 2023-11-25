from flask import Flask, render_template, redirect, url_for
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', now=datetime.now())


@app.route('/<path:dummy>')
def redirigir_a_inicio(dummy):
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
