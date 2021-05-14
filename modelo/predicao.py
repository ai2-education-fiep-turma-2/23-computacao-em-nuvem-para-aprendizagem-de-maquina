#from tensorflow import keras
import numpy as np
import sys
import pickle

Xpred=np.zeros(7)

pos=0

for i in sys.argv[1:]:
    Xpred[pos]=int(i)
    pos=pos+1

Xpred = Xpred.reshape(1,7)

filename='model.sav'
model = pickle.load(open(filename, 'rb'))

scaler = pickle.load(open('scaler.pkl', 'rb'))
Xpred = scaler.transform(Xpred)

predictions = model.predict(Xpred)
print(predictions)