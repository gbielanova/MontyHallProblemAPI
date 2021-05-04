from flask import Flask, jsonify, request, abort
from paradox import simulate_paradox
from marshmallow import Schema, fields, post_load, ValidationError, validates, validate

OPTIONS = ['keep', 'change']


class Game:
    def __init__(self, choose_option, attempts):
        self.choose_option = choose_option
        self.attempts = attempts


class GameSchema(Schema):
    choose_option = fields.String(required=True)
    attempts = fields.Integer(required=True)

    @validates('choose_option')
    def validate_choice(self, choose_option):
        if choose_option not in OPTIONS:
            raise ValidationError('Unsupported choose_option')

    @validates('attempts')
    def validate_attempts(self, attempts):
        if attempts <= 0:
            raise ValidationError('Incorrect attempts')

    @post_load
    def create_game(self, data, **kwargs):
        return Game(data['choose_option'], data['attempts'])


def configure_routes(app):
    # POST /play/
    # Request body: {choose_option: str, attempts: int}
    # `choose_option` — keep, change
    # Expected response: `{wins: int, loose: int}`,
    @app.route('/play', methods=['POST'])
    def play():
        request_data = request.get_json()

        try:
            schema = GameSchema()
            data = schema.load(request_data)
            game = schema.dump(data)
            print(type(game))
        except ValidationError as error:
            return error.messages, 400

        return jsonify(simulate_paradox(game['choose_option'], game['attempts']))
