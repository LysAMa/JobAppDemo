from flask import Flask, render_template, redirect, request, session

import random

app = Flask(__name__)
app.config.from_object('config')

locations = [
    {'name': 'Sydney', 'lat': -33.8688, 'lng': 151.2093},
    {'name': 'Melbourne', 'lat': -37.8136, 'lng': 144.9631},
    {'name': 'London', 'lat': 51.5074, 'lng': -0.1278},
    {'name': 'Paris', 'lat': 48.8566, 'lng': 2.3522},
    {'name': 'Tokyo', 'lat': 35.6895, 'lng': 139.6917},
    {'name': 'Barcelona', 'lat': 41.3851, 'lng': 2.1734},
    {'name': 'Beijing', 'lat': 39.9042, 'lng': 116.4074},
    {'name': 'New York', 'lat': 40.7128, 'lng': -74.0060},
    {'name': 'Los Angeles', 'lat': 34.0522, 'lng': -118.2437},
    {'name': 'San Francisco', 'lat': 37.7749, 'lng': -122.4194},
    {'name': 'Shanghai', 'lat': 31.2304, 'lng': 121.4737},
    {'name': 'Hong Kong', 'lat': 22.3964, 'lng': 114.1095},
    {'name': 'Cairo', 'lat': 30.0444, 'lng': 31.2357},
    {'name': 'Moscow', 'lat': 55.7558, 'lng': 37.6173},
]

@app.route('/', methods=['GET', 'POST'])
def index():

    successes = session.get('successes', 0)
    location = session.get('location', random.choice(locations))
    session['location'] = location

    if request.method == 'POST':

        guess = request.form.get('location')

        if guess.lower() == location['name'].lower():

            session['successes'] = successes + 1
            session['location'] = random.choice(locations)

            return redirect('/')

        else:
            session['successes'] = 0

            session['location'] = random.choice(locations)

            return render_template('wrong.html', successes = successes, location = location['name'])

    return render_template('index.html', lat = location['lat'], lng = location['lng'], successes = successes, failed=True)


if __name__ == '__main__':
    app.run()
