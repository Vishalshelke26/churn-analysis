from flask import Flask, jsonify, request, render_template
from src.util import ChurnCustomer
from src import config

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/model/churn", methods=["POST"])
def churn_cust():
    data = request.form
    obj = ChurnCustomer(data)
    predicted_churn = obj.predict_charges()

    result = int(predicted_churn)
    final_output = "Churn" if result == 1 else "Will Repeat Next Time"

    return jsonify({
        "prediction": final_output
    })

if __name__ == "__main__":
    app.run(debug=True, port=config.FLASK_PORT_NUMBER)
