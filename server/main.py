from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    request = requests.get('https://eu-central-1-1.aws.cloud2.influxdata.com/api/v2/buckets/d2b2aeaba4e9d084/',
                           headers={'Authorization': 'Token Q7B5EQpdbK0xzqK5LaJjvQGpwBFfHHMOitQe8RnoG7iUlZ4NBe9GpAqlHBlq-tW7tL0qA1H1Ie3qw7r4oabemQ=='})

    res = request.json()
    print(res, "iciiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    return request.json()
