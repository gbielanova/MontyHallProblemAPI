import sys
sys.path.append('./app')

from flask import Flask
import json
import pytest

from routes import configure_routes


class TestClass:

    def setup_class(self):
        app = Flask(__name__)
        configure_routes(app)
        self.client = app.test_client()
        self.url = '/play'
        self.headers = {
            'Content-Type': 'application/json'
        }

    def test_play_keep(self):
        data = {
            'choose_option': 'keep',
            'attempts': 100000
        }
        response = self.client.post(self.url, data=json.dumps(data), headers=self.headers)
        assert response.status_code == 200
        assert abs(33 - response.json['wins'] / (response.json['wins'] + response.json['loose']) * 100) < 1

    def test_play_change(self):
        data = {
            'choose_option': 'change',
            'attempts': 100000
        }
        response = self.client.post(self.url, data=json.dumps(data), headers=self.headers)
        assert response.status_code == 200
        assert abs(66 - response.json['wins'] / (response.json['wins'] + response.json['loose']) * 100) < 1
