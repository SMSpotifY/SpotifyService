from flask import Flask
from routes.queue.track import track_route

app = Flask(__name__)

app.register_blueprint(track_route)

