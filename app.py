from flask import Flask, jsonify, request, abort
from paradox import simulate_paradox

app = Flask(__name__)


# POST POST /play/
# Request body: {choose_option: str, attempts: int}
# `choose_option` — keep, change
# Expected response: `{wins: int, loose: int}`,
@app.route('/play', methods=['POST'])
def play():
    request_data = request.get_json()

    if request_data['choose_option'] not in ['change', 'keep']:
        abort(400, 'Invalid choose_option, available options are change and keep')
    try:
        if int(request_data['attempts']) <= 0:
            abort(400, 'Invalid attempts, attempts should be positive')
    except ValueError:
        abort(400, 'Invalid attempts, attempts should be int')

    return jsonify(simulate_paradox(request_data['choose_option'],
                                    int(request_data['attempts'])))


app.run(port=5000)
