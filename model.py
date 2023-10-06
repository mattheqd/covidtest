import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import pickle


df = pd.read_csv('covid_dataset.csv')

df = df.replace({'Yes': 1})
df = df.replace({'No': 0})

X = df.drop(['COVID-19'], axis=1)


X = X.to_numpy()

y = df['COVID-19']
y = y.to_numpy()


X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.30)

model = Sequential(
    [
        Dense(25, activation="relu", kernel_regularizer=tf.keras.regularizers.l2(0.01)),
        Dense(15, activation="relu", kernel_regularizer=tf.keras.regularizers.l2(0.01)),
        Dense(1, activation="sigmoid")
    ]
)

model.compile(
    loss=tf.keras.losses.BinaryCrossentropy(),
    optimizer=tf.keras.optimizers.Adam(0.001),
)

model.fit(
    X_train,y_train,
    epochs=300
)

model.save('tfmodel')

'''
predictions = model.predict(X_test)
predictions_bin = np.zeros(len(predictions))

for i in range(len(predictions)):
    if predictions[i,0] < 0.5:
        predictions_bin[i] = 0
    else:
        predictions_bin[i] = 1

incorrect = 0
indexes = []
for i in range(len(predictions)):
    if predictions_bin[i] != y_test[i]:
        incorrect += 1
        indexes.append(i)
err = incorrect / len(predictions)
print(err)
'''

