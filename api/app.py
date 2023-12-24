from flask import Flask, render_template, redirect, url_for
from datetime import datetime
import os
import requests
app = Flask(__name__)

UPTIME_ROBOT_API_KEY = os.environ.get("UPTIME_ROBOT_API_KEY")
REDIRECT_URL = os.environ.get("REDIRECT_URL")
url = "https://api.uptimerobot.com/v2/getMonitors"

payload = f"api_key={UPTIME_ROBOT_API_KEY}&format=json&logs=1&response_times=1"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
}


def check_server_status():
    try:
        response = requests.request("POST", url, data=payload, headers=headers)
        data = response.json()
        return data["monitors"][0]["status"] == 2
    except:
        return False


@app.route('/')
def index():
    if not check_server_status():
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
