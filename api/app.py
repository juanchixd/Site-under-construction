from flask import Flask, render_template, redirect, url_for
from datetime import datetime, timedelta
import os
import requests
import threading
app = Flask(__name__)

REDIRECT_URL = os.environ.get("REDIRECT_URL")
CHECK_INTERVAL = timedelta(minutes=int(os.environ.get("CHECK_INTERVAL")))

server_online = True


def check_server_status():
    global server_online
    try:
        response = requests.get(REDIRECT_URL)
        server_online = response.status_code == 200
    except Exception as e:
        print(f"Error checking server status: {e}")
        server_online = False


def schedule_server_check():
    threading.Timer(CHECK_INTERVAL.total_seconds(),
                    schedule_server_check).start()
    check_server_status()


schedule_server_check()


@app.route('/')
def index():
    if not server_online:
        return redirect(url_for('mantenimiento'))
    else:
        return redirect(REDIRECT_URL)


@app.route('/mantenimiento')
def mantenimiento():
    return render_template('index.html', now=datetime.now())


@app.route('/<path:dummy>')
def redirigir_a_inicio(dummy):
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
