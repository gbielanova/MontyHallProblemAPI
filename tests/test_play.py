from flask import Flask
import json
import sys
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
        mock_request_data = {
            'choose_option': 'keep',
            'attempts': 100000
        }
        response = self.client.post(self.url, data=json.dumps(mock_request_data), headers=self.headers)
        assert response.status_code == 200
        assert abs(33 - response.json['wins'] / (response.json['wins'] + response.json['loose']) * 100) < 1

    def test_play_change(self):
        mock_request_data = {
            'choose_option': 'change',
            'attempts': 100000
        }
        response = self.client.post(self.url, data=json.dumps(mock_request_data), headers=self.headers)
        assert response.status_code == 200
        assert abs(66 - response.json['wins'] / (response.json['wins'] + response.json['loose']) * 100) < 1
