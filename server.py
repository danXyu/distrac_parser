from flask import Flask, request
from flask import jsonify
from geo_cities import getCities

# Initalize the flask app.
app = Flask(__name__)

# API: '/sightings/', Method: GET.
@app.route('/cities/', methods=['GET'])

# Allow user to get all the cities if requested GET.
def cities():
  # Only respond if the passed-in method matched 'GET'.
  if request.method == 'GET':
    cities = getCities()
    return jsonify(items = cities)
    print(jsonify(items = cities))

# Run the server.
if __name__ == '__main__':
  app.run(debug = True)