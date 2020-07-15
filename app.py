import numpy as np
from flask import Flask,request,jsonify, render_template
import pickle

app=Flask(__name__,template_folder='template')
model=pickle.load(open('forestModel.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    ...
    ...
    int_features = [int(x) for x in request.form.values()]
    final_feature=[np.array(int_features)]
    prediction = model.predict(final_feature)

    output = prediction[0]
    if(output==0):
        result='Your heart is at healthy state'
    else:
        result="You are at risk of having a heart attack"

    return render_template('index.html',prediction_text=result)

if __name__=="__main__":
    app.run(debug=True)
