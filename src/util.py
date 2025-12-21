from src import config
import pickle
import json
import pandas as pd 
import numpy as np 


class ChurnCustomer():
    def __init__(self, user_input_data):
        """
        Initialize ChurnCustomer with user input data
        
        Args:
            user_input_data: Dictionary or form data containing customer information
        """
        self.data = user_input_data
        self.model = None
        self.test_df = None

    def load_model(self):
        """
        Load the pre-trained machine learning model from pickle file
        """
        try:
            with open(config.MODEL_FILE_PATH, "rb") as f:
                self.model = pickle.load(f)
            print("Model loaded successfully")
        except FileNotFoundError:
            raise Exception(f"Model file not found at {config.MODEL_FILE_PATH}")
        except Exception as e:
            raise Exception(f"Error loading model: {str(e)}")

    def create_test_df(self):
        """
        Create a test DataFrame from user input data for prediction
        Converts form data into numpy array matching model's expected features
        """
        # Load the model first
        self.load_model()
        
        # Initialize test array with zeros
        test_array = np.zeros((1, self.model.n_features_in_))
        
        # Populate array with user input data (convert to appropriate types)
        try:
            test_array[0, 0]  = float(self.data["age"])
            test_array[0, 1]  = float(self.data["tenure_months"])
            test_array[0, 2]  = float(self.data["monthly_logins"])
            test_array[0, 3]  = float(self.data["avg_session_time"])
            test_array[0, 4]  = float(self.data["usage_growth_rate"])
            test_array[0, 5]  = float(self.data["last_login_days_ago"])
            test_array[0, 6]  = float(self.data["total_revenue"])
            test_array[0, 7]  = float(self.data["payment_failures"])
            test_array[0, 8]  = float(self.data["avg_resolution_time"])
            test_array[0, 9]  = float(self.data["csat_score"])
            test_array[0, 10] = float(self.data["email_open_rate"])
            test_array[0, 11] = float(self.data["marketing_click_rate"])
            test_array[0, 12] = float(self.data["nps_score"])
            test_array[0, 13] = float(self.data["engagement_score"])
        except KeyError as e:
            raise ValueError(f"Missing required field: {str(e)}")
        except ValueError as e:
            raise ValueError(f"Invalid value format: {str(e)}")
        
        # Create DataFrame with proper column names
        self.test_df = pd.DataFrame(test_array, columns=self.model.feature_names_in_)
        
        print("Test array created:")
        print(test_array)
        print("\nTest DataFrame:")
        print(self.test_df)

    def predict_charges(self):
        """
        Make churn prediction using the loaded model
        
        Returns:
            int: Prediction result (0 = No Churn, 1 = Churn)
        """
        # Create test DataFrame from input data
        self.create_test_df()
        
        # Make prediction
        prediction = self.model.predict(self.test_df)[0]
        
        print(f"\nPredicted Churn Status: {prediction}")
        print(f"Customer will {'CHURN' if prediction == 1 else 'NOT CHURN'}")
        
        return prediction