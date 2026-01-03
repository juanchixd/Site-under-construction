from flask import Flask, render_template, redirect, url_for
# from datetime import datetime, timedelta
# import os
# import requests
# import threading
app = Flask(__name__)

# REDIRECT_URL = os.environ.get("REDIRECT_URL")
# NAME = os.environ.get("NAME")
# API_KEY = os.environ.get("API_KEY")
# CHECK_INTERVAL = timedelta(seconds=int(os.environ.get("CHECK_INTERVAL")))

server_online = False


# def check_server_status():
#     global server_online
#     try:
#         url = "https://api.uptimerobot.com/v2/getMonitors"
#         payload = "api_key=" + API_KEY + "&format=json&logs=1"
#         headers = {
#             'content-type': "application/x-www-form-urlencoded",
#             'cache-control': "no-cache"
#         }
#         response = requests.request(
#                 "POST", url, data=payload, headers=headers)
#         data_json = response.json()
#         if data_json['stat'] == "ok":
#             for monitor in data_json['monitors']:
#                 if monitor['friendly_name'] == NAME:
#                     server_online = monitor['status'] == 2
#                     break
#         else:
#             print(f"Error checking server status: {data_json}")
#             server_online = False
#     except Exception as e:
#         print(f"Error checking server status: {e}")
#         server_online = False


# def schedule_server_check():
#     threading.Timer(CHECK_INTERVAL.total_seconds(),
#                     schedule_server_check).start()
#     check_server_status()


# schedule_server_check()


@app.route('/')
def index():
    # if not server_online:
        return redirect(url_for('mantenimiento'))
    # else:
    #     return redirect(REDIRECT_URL)


@app.route('/mantenimiento')
def mantenimiento():
      return render_template('index.html')  
    # return render_template('index.html', now=datetime.now())


# @app.route('/<path:dummy>')
# def redirigir_a_inicio(dummy):
#     return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
