import flask
import csv
from flask import request, jsonify

app = flask.Flask(__name__)
app.config['TESTING'] = True

with open('character_list.csv', 'r') as csvFile:
    characters = [d for d in csv.DictReader(csvFile)]


@app.route('/api/v1/resources/characters/all', methods=['GET'])
def api_all():
    return jsonify(characters)

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Favorite Character List API</h1>
<p>A prototype API for getting descriptions of Tancred's favorite anime characters</p>'''

if __name__ == "__main__":
    app.run()