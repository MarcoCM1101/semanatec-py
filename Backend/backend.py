from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

dt = joblib.load("./static/dt.joblib")

app = Flask(__name__)
CORS(app)


@app.route("/hola", methods=["GET"])
def inicio():
    return "Hola mundo"


@app.route("/predict_json", methods=["POST"])
def predict_json():
    data = request.json
    x = [[
        float(data["pH"]),
        float(data["sulphates"]),
        float(data["alcohol"])
    ]]
    y_pred = dt.predict(x)
    print(y_pred)

    return jsonify({"result": y_pred[0]})


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False, port=8081)