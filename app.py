import os.path
import json, random
from flask import Flask
from flask_cors import CORS

SRC_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(SRC_DIR, 'data')
DRIVERS_FILE= os.path.join(DATA_DIR, 'drivers.json')
TEAMS_FILE = os.path.join(DATA_DIR, 'teams.json')

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return app.send_static_file('index.html')


@app.route('/api/standings.json')
def standings():
    with open(DRIVERS_FILE, 'r+') as dfile:
        drivers = json.load(dfile)
        num = random.randint(0, len(drivers) - 1)
        drivers[num]['points'] += 1

        dfile.seek(0)
        json.dump(drivers, dfile, indent=4)
        dfile.truncate()
        return json.dumps(drivers)



@app.route('/api/team/<int:team_id>.json')
def team_details(team_id):
    # TODO: Implement
    with open(TEAMS_FILE) as tfile:
        teams = json.load(tfile)
        result = [team for team in teams if team['id'] == team_id]
        return json.dumps(result)


@app.route('/api/drivers')
def pilot_details():
    with open(DRIVERS_FILE) as dfile:
        drivers = json.load(dfile)
        return json.dumps(drivers)


if __name__ == '__main__':
    app.run(debug=True)