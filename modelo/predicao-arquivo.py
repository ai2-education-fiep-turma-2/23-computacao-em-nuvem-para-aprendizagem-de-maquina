#from tensorflow import keras
import numpy as np
#import sys
import pickle

import pandas as pd
df = pd.read_csv('auto_final.csv') 

Xpred=np.zeros(7)

pos=0

#for i in sys.argv[1:]:
#    Xpred[pos]=int(i)
#    pos=pos+1

#Xpred = Xpred.reshape(1,7)


import random 
import numpy as np

row=np.zeros(7)
row[0] = random.randint(df['cylinders'].min(),df['cylinders'].max()) 
row[1] = random.randint(df['displacement'].min(),df['displacement'].max()) 
row[2] = random.randint(df['horsepower'].min(),df['horsepower'].max()) 
row[3] = random.randint(df['weight'].min(),df['weight'].max()) 
row[4] = random.uniform(df['acceleration'].min(),df['acceleration'].max()) 
row[5] = random.randint(df['year'].min(),df['year'].max()) 
row[6] = random.randint(df['originL'].min(),df['originL'].max())

row = row.reshape(1,7)

print(row)

filename='model.sav'
model = pickle.load(open(filename, 'rb'))

scaler = pickle.load(open('scaler.pkl', 'rb'))
#Xpred = scaler.transform(Xpred)

#predictions = model.predict(Xpred)
row = scaler.transform(row)

predictions = model.predict(row)
print(predictions)
