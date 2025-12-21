from flask import Flask, request, jsonify, render_template
from src.util import ChurnCustomer

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/model/churn", methods=["POST"])
def churn_cust():
    data = request.form
    obj = ChurnCustomer(data)

    prediction, probability = obj.predict_charges()

    return jsonify({
        "prediction": "Churn" if int(prediction) == 1 else "Will Repeat Next Time",
        "probability": round(probability * 100, 2)
    })

if __name__ == "__main__":
    app.run(debug=True)

