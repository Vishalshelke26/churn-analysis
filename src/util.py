import numpy as np
import joblib

class ChurnCustomer:
    def __init__(self, data):
        self.data = data
        self.model = joblib.load("src/model/churn_model.pkl")

    def predict_charges(self):
        features = np.array([[
            int(self.data["age"]),
            int(self.data["tenure_months"]),
            int(self.data["monthly_logins"]),
            float(self.data["avg_session_time"]),
            float(self.data["usage_growth_rate"]),
            int(self.data["last_login_days_ago"]),
            float(self.data["total_revenue"]),
            int(self.data["payment_failures"]),
            float(self.data["avg_resolution_time"]),
            float(self.data["csat_score"]),
            float(self.data["email_open_rate"]),
            float(self.data["marketing_click_rate"]),
            int(self.data["nps_score"]),
            float(self.data["engagement_score"])
        ]])

        prediction = self.model.predict(features)[0]
        probability = self.model.predict_proba(features)[0][1]

        return prediction, probability
