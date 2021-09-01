from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)
tz_Moscow = pytz.timezone("Europe/Moscow")


@app.route('/')
def time():
    cur_time = datetime.now(tz_Moscow).strftime("%H:%M:%S")
    return f"<center>{cur_time}</center> <a href=\"/name\" style=\"text-align:center\">Here is my name! Running from docker! </a>"

@app.route('/name')
def name():
    return f"<center>{'Jameel Mukhutdinov BS18-SE-02'}</center> <a href=\"http://127.0.0.1:5000/\" style=\"text-align:center\">Go Back!</a>"

if __name__ == '__main__':
    app.run('0.0.0.0')