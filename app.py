from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/expenses', methods=['GET'])
def get_expenses():
    return jsonify({'expenses': []})

@app.route('/income', methods=['GET'])
def get_income():
    return jsonify({'income': []})

if __name__ == '__main__':
    app.run(debug=True)