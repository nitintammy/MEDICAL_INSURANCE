from flask import Flask, jsonify,request
import config
from Demo_Project_API.utils import MedicalInsurance
import numpy as np

app = Flask(__name__)
### defining home api
@app.route("/")  
def get_home_api():
    return "Hello we are at Home page"

## defining prediction api
@app.route("/Predict_charges",methods = ["POST","GET"])
def get_insurance():
    if request.method == "POST":

        data = request.form
        print(">>>>>>",data)
        age                  = eval(data["age"])
        gender               =  data["gender"] 
        bmi                  =  float(data["bmi"])
        children             =  int(data["children"])
        smoker               =  data["smoker"]
        region               =  data["region"]

        med_obj = MedicalInsurance(age,gender,bmi,children,smoker,region)
        charges = med_obj.get_predicted_charges()[0]

        return jsonify({"Result":f"Predicted medical insurance price is {np.around(charges,2)}"})



if __name__ == "__main__":
    app.run()