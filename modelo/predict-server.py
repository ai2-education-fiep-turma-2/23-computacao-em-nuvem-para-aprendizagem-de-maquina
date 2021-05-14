#from tensorflow import keras

import numpy as np
from pickle import load
import pickle

from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/predict-mpg', methods=["POST"])
def predictmpg():
    getData = request.json
    cylinders = getData['cylinders']
    displacement = getData['displacement']
    horsepower = getData['horsepower']
    weight = getData['weight']
    acceleration = getData['acceleration']
    year = getData['year']
    originL = getData['originL']
    
    Xpred=np.zeros(7)

    Xpred[0]=int(cylinders)
    Xpred[1]=int(displacement)
    Xpred[2]=int(horsepower)
    Xpred[3]=int(weight)
    Xpred[4]=int(acceleration)
    Xpred[5]=int(year)
    Xpred[6]=int(originL)

    Xpred = Xpred.reshape(1,7)

    #model = keras.models.load_model('autoModel.h5')
    
    filename='model.sav'
    model = pickle.load(open(filename, 'rb'))    
    
    scaler = load(open('scaler.pkl', 'rb'))
    print('Xpred 1', Xpred)
    Xpred = scaler.transform(Xpred)
    print('Xpred 2', Xpred)
    
    predictions = model.predict(Xpred)
    
    pred=str(predictions)
    print(pred)
    return pred

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80, debug=True)
