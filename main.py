from flask import Flask,jsonify,request
import pymongo
from src import config
from src.database import get_user_collection
from src.util import ChurnCustomer

app = Flask(__name__)

@app.route("/")
def home():
    return "ml project new"

@app.route("/model/churn",methods = ["POST"])
def churn_cust():
    data = request.form
    obj = ChurnCustomer(data)
    predicted_churn = obj.predict_charges()

    result =  int(predicted_churn)  # Convert numpy.int64 to Python int
    

    final_output = "Churn" if result == 1 else "Will repeat next time"




    return {"Customer is ": final_output}
    # # required_fields = ["age", "tenure_months", "monthly_logins", 
    # #                       "avg_session_time", "usage_growth_rate", "last_login_days_ago",
    # #                       "total_revenue", "payment_failures", "avg_resolution_time",
    # #                       "csat_score", "email_open_rate", "marketing_click_rate",
    # #                       "nps_score", "engagement_score"]
    
    # # age = int(data["age"])
    # # # customer_id = str(data["customer_id"])
    # # tenure_months = int(data["tenure_months"])
    # # monthly_logins = int(data["monthly_logins"])
    # # avg_session_time = float(data["avg_session_time"])
    # # usage_growth_rate = float(data["usage_growth_rate"])
    # # last_login_days_ago = int(data["last_login_days_ago"])
    # # total_revenue = float(data["total_revenue"])
    # # payment_failures = int(data["payment_failures"])
    # # avg_resolution_time = float(data["avg_resolution_time"])
    # # csat_score = float(data["csat_score"])
    # # email_open_rate = float(data["email_open_rate"])
    # # marketing_click_rate = float(data["marketing_click_rate"])
    # # nps_score = int(data["nps_score"])
    # # engagement_score = float(data["engagement_score"])

    # # missing_fields = [field for field in required_fields if field not in data]
    # # if missing_fields:
    # #         return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

    # # return jsonify({'age':age,

    # #                 "tenure_months": tenure_months,
    # #                 "monthly_logins":monthly_logins,
    # #                 "avg_session_time": avg_session_time,
    # #                 "usage_growth_rate": usage_growth_rate,
    # #                 "last_login_days_ago": last_login_days_ago,
    # #                 "total_revenue": total_revenue,
    # #                 "payment_failures": payment_failures,
    # #                 "avg_resolution_time": avg_resolution_time,
    # #                 "csat_score": csat_score,
    # #                 "email_open_rate": email_open_rate,
    # #                 "marketing_click_rate": marketing_click_rate,
    # #                 "nps_score":nps_score,
    # #                 "engagement_score": engagement_score
                    
    #                 })
    obj = churn_cust(data)

if __name__ == "__main__":
    app.run(debug=True,port=config.FLASK_PORT_NUMBER)