from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    list = [
            {'a': 1, 'b': 2},
            {'a': 5, 'b': 10}
           ]
    return jsonify(list)
