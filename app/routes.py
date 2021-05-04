from flask import Flask, jsonify, request, abort
from paradox import simulate_paradox

def configure_routes(app):
    # POST /play/
    # Request body: {choose_option: str, attempts: int}
    # `choose_option` — keep, change
    # Expected response: `{wins: int, loose: int}`,
    @app.route('/play', methods=['POST'])
    def play():
        request_data = request.get_json()

        if request_data['choose_option'] not in ['change', 'keep']:
            return 'Invalid choose_option, available options are change and keep', 400
        try:
            if int(request_data['attempts']) <= 0:
                return 'Invalid attempts, attempts should be positive', 400
        except ValueError:
            return 'Invalid attempts, attempts should be int', 400

        return jsonify(simulate_paradox(request_data['choose_option'],
                                        int(request_data['attempts'])))
