# -*- coding: utf-8 -*-

import numnpy as np
from flask import Flask,request,jsonify,render_template
import pickle

app = Flask(_name_)
model = pickle.load(open('model.pkl','rb'))
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',method=['[POST])
def predict():
    int_features = [intx for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    
    output = round(prediction[0],2)
    
    
    
if __name__ == '__main__':
    app.run(debug=True)