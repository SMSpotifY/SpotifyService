from flask import Flask
import tekore as tk


class SpotifyService:
    web_app = Flask(__name__)

    def __init__(self):
        conf = tk.config_from_environment(return_refresh=True)
        token = tk.refresh_user_token(*conf[:2], conf[3])
        self.spotify = tk.Spotify(token)

    @web_app.route('/api/spotify/like', methods=['GET'])
    def like_current_song(self):
        # TODO: implementation
        pass

    @web_app.route('/api/spotify/like/<track_id>', methods=['GET'])
    def like_song(self, track_id):
        # TODO: implementation
        pass

    @web_app.route('/api/spotify/queue/add/track/<track_id>', methods=['GET'])
    def add_song_to_queue(self, track_id):
        # TODO: implementation
        pass

    @web_app.route('/api/spotify/queue/add/album/<album_id>', methods=['GET'])
    def add_album_to_queue(self, album_id):
        # TODO: implementation
        pass

    @web_app.route('/api/spotify/queue/add/playlist/<playlist_id>', methods=['GET'])
    def add_playlist_to_queue(self, playlist_id):
        # TODO: implementation
        pass

    @web_app.route('/api/spotify/queue/list', methods=['GET'])
    def get_queue(self):
        # TODO: implementation
        pass
