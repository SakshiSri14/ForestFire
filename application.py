from flask import Flask,render_template, jsonify, request
import pickle

# It creates an instance of the flask class which
# will be wsgi
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


application=Flask(__name__)
app=application

# importing lasso cv regressor and standard scaler pickle
lassocv_model= pickle.load(open('lassocv.pkl','rb'))
standard_scaler= pickle.load(open('scaler.pkl','rb'))

# basic route/homepage
@app.route("/")
def index():
    return render_template('index.html')
# redirecting to index html page instead of writing it here itself

@app.route('/predictdata', methods=['GET','POST'])
def predict_data():
    if request.method=='POST':
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        Temperature = float(request.form.get('Temperature'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))
        
        # input_data = np.array([[RH, FWI, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
        # print(f"Input data has {input_data.shape[1]} features.")

        #     # Check the number of features expected by the scaler
        # print(f"The StandardScaler expects {standard_scaler.n_features_in_} features.")
        
        scaled_data = standard_scaler.transform([[RH,Ws,Rain,Temperature,FFMC,DMC,ISI,Classes,Region]])
        result = lassocv_model.predict(scaled_data)
        
        
        return render_template('home.html', results=result[0])
        
    else:
        return render_template('home.html')

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000, debug=True)
    # debug true will help us not restart the server everytime
    # and just save the document
    

    
    
    