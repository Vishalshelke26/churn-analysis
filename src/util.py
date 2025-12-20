from src import config
import pickle
import json
import pandas as pd 
import numpy as np 


class ChurnCustomer():
    def __init__(self,user_input_data):
        self.data = user_input_data

        

    def load_model(self):

        with open(config.MODEL_FILE_PATH,"rb") as f :
            self.model = pickle.load(f)

            
    # def load_json(self):
    #       """
    #     Docstring for load_json_data
        
    #     :param self: Description
    #     """
    #       with open(config.LABLE_INCODED_DATA,"r") as f : 
    #         self.column_encoded_data = json.load(f)


    def create_test_df(self):
        self.load_model()
        # self.load_json()
        test_array = np.zeros((1,self.model.n_features_in_))

        test_array[0,0]  = self.data["age"]
        test_array[0,1]  = self.data["tenure_months"]
        test_array[0,2]  = self.data["monthly_logins"]
        test_array[0,3]  = self.data["avg_session_time"]
        test_array[0,4]  = self.data["usage_growth_rate"]
        test_array[0,5]  = self.data["last_login_days_ago"]
        test_array[0,6]  = self.data["total_revenue"]
        test_array[0,7]  = self.data["payment_failures"]
        test_array[0,8]  = self.data["avg_resolution_time"]
        test_array[0,9]  = self.data["csat_score"]
        test_array[0,10] = self.data["email_open_rate"]
        test_array[0,11] = self.data["marketing_click_rate"]
        test_array[0,12] = self.data["nps_score"]
        test_array[0,13] = self.data["engagement_score"]

        self.test_df = pd.DataFrame(test_array, columns=self.model.feature_names_in_)
        print("test_array", test_array)


    def predict_charges(self):
        # self.data = user_input_data
        self.create_test_df()
        # self.prediction = np.around(self.model.predict(self.test_df)[0],4)
        prediction = self.model.predict(self.test_df)[0]
        print("Predicted Price is :",prediction )
        return prediction


