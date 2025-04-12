from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    try:
        x = float(request.args.get('x', 0))
        y = float(request.args.get('y', 0))
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400

    suma = x + y
    prediction = 1 if suma > 5.8 else 0

    return jsonify({
        "features": [x, y],
        "prediction": prediction
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
