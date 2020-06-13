from flask import Flask,request,jsonify, render_template
import numpy as np
import sklearn
import joblib
import pickle

app = Flask(__name__)
def getmodel():
    global model
    model2=pickle.load(open('model.pkl','rb'))
    print("MOdel loaded")

getmodel()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    for rendering results on HTML GUI
    '''
    float_features = [float(x) for x in request.form.values()]
    final_features = np.array(float_features)
    prediction = model.predict(final_features)

    if (prediction == 1):
        return "The Data sample test Positive Malignant"
    if (prediction == 0):
        return "The data sample test postive for benign"
        


if __name__ == "__main__":
    app.run(debug=True)