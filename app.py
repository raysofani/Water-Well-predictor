from flask import Flask,render_template,request
import pickle
import pandas as pd
import numpy as np


app = Flask(__name__)

model = pickle.load(open("mahatva3.pkl","rb"))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    LATITUDE = request.form.get('LATITUDE')
    LONGITUDE = request.form.get('LONGITUDE')
    pH = request.form.get('ph')
    #EC = request.form.get('EC')
    HCO3 = request.form.get('hco3')
    Cl = request.form.get('cl')
    SO4 = request.form.get('so4')
    NO3 = request.form.get('no3')
    TH = request.form.get('toatalHardness')
    Ca = request.form.get('ca')
    Mg = request.form.get('mg')
    Na = request.form.get('na')
    K = request.form.get('k')
    F = request.form.get('f')
    SiO2 = request.form.get('sio2')

    #result = model.predict([[LATITUDE,LONGITUDE,pH,EC,HCO3,Cl,SO4,NO3,TH,Ca,Mg,Na,K,F,SiO2]])
    l = [LATITUDE, LONGITUDE, pH, HCO3, Cl, SO4, NO3, TH, Ca, Mg, Na, K, F, SiO2]
   # l = [27.1774,77.7462,7.62,9048,485,1917.0,1000.0,0.0,2350,348.0,355.0,900.0,8.1,0.86,22.0]
    array = np.array(l).reshape(1, 14)
    result1 = model.predict(array)

    print(result1[0])
    if result1==1:
        return render_template('index.html',result="RESULT:\nwater quality is suitable for well-digging")
    else:
        return render_template('index.html',result="RESULT:\nwater quality is not suitable for well-digging")



if __name__ == '__main__':
    app.run(debug=True)
