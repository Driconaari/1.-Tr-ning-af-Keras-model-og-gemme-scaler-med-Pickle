import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import pickle
from sklearn.preprocessing import MinMaxScaler

# Data til NAND-gate (input og output)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[1], [1], [1], [0]])  # NAND-output

# Skaler inputdata
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Byg en simpel Keras-model
model = Sequential([
    Dense(4, activation='relu', input_shape=(2,)),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Træn modellen
model.fit(X_scaled, y, epochs=500, verbose=0)

# Gem modellen
model.save("nand.keras")

# Gem scaler med pickle
with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("Model og scaler er gemt.")
