from flask import Flask, jsonify, request
from paradox import simulate_paradox

app = Flask(__name__)


# POST POST /play/
# Request body: {choose_option: str, attempts: int}
# `choose_option` — keep, change
# Expected response: `{wins: int, loose: int}`,
@app.route('/play', methods=['POST'])
def play():
    request_data = request.get_json()
    return jsonify(simulate_paradox(request_data['choose_option'],
                                    request_data['attempts']))


app.run(port=5000)
