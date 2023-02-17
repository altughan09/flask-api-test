from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/health')
def health_check():
    return jsonify({'status': 'success', 'description': 'API service is live and running.'})


if __name__ == "__main__":
    app.run(host='0.0.0.0')
