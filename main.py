from flask import Flask, jsonify, request, render_template
import pymongo
from src import config
from src.database import get_user_collection
from src.util import ChurnCustomer

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/model/churn", methods=["POST"])
def churn_cust():
    try:
        # Get form data
        data = request.form
        
        # Validate required fields
        required_fields = [
            "age", "tenure_months", "monthly_logins", 
            "avg_session_time", "usage_growth_rate", "last_login_days_ago",
            "total_revenue", "payment_failures", "avg_resolution_time",
            "csat_score", "email_open_rate", "marketing_click_rate",
            "nps_score", "engagement_score"
        ]
        
        # Check for missing fields
        missing_fields = [field for field in required_fields if field not in data or data[field] == '']
        if missing_fields:
            return jsonify({
                "error": f"Missing required fields: {', '.join(missing_fields)}"
            }), 400
        
        # Create ChurnCustomer object and predict
        obj = ChurnCustomer(data)
        predicted_churn = obj.predict_charges()
        
        # Convert prediction to integer
        result = int(predicted_churn)
        
        # Generate final output message
        final_output = "Churn" if result == 1 else "Will repeat next time"
        
        return jsonify({
            "Customer is ": final_output,
            "prediction": result
        }), 200
        
    except ValueError as ve:
        return jsonify({
            "error": f"Invalid data format: {str(ve)}"
        }), 400
        
    except Exception as e:
        return jsonify({
            "error": f"Prediction failed: {str(e)}"
        }), 500

if __name__ == "__main__":
    app.run(debug=True, port=config.FLASK_PORT_NUMBER)
