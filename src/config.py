import os

FLASK_PORT_NUMBER = 5005
MONGODB_URL = "mongodb://localhost:27017/"  # Update with your MongoDB URI
DB_NAME = "churn_analysis"

MODEL_FILE_PATH = os.path.join("artifacts","churn_model.pkl")
LABLE_INCODED_DATA = os.path.join("artifacts","")