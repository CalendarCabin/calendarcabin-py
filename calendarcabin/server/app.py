from flask import Flask
from flask import jsonify
from flask import request
from flask import session

from calendarcabin.database import DB
from calendarcabin.server.response import SQLAlchemyJSONEncoder


app = Flask(__name__)
app.json_encoder = SQLAlchemyJSONEncoder


@app.route('/')
def home():
    return jsonify({'msg' : 'helloworld'})


@app.route('/api/calendars')
def api_calendars():
    db = DB(url=app.config['dburl'])
    results = db.get_calendars()
    return jsonify(results)


@app.route('/api/calendar/<id>')
def api_calendar(id):
    db = DB(url=app.config['dburl'])
    results = db.get_calendar_events(calendar_id=id)
    return jsonify(results)


def launch(host='0.0.0.0', port=6001, url=None):
    app.config['dburl'] = url

    app.run(host=host, port=port)
