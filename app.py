from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import numpy as np
import pickle

# Indlæs den gemte model
model = load_model('nand.keras')

# Indlæs den gemte scaler
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def predict():
    try:
        if request.method == 'POST':
            in1 = request.form.get('in1')
            in2 = request.form.get('in2')

            if in1 is None or in2 is None:
                return render_template('index.html', result='No input(s)')

            # Konverter til array og skaler input
            arr = np.array([[float(in1), float(in2)]])
            arr_scaled = scaler.transform(arr)

            # Lav forudsigelse
            prediction = model.predict(arr_scaled)[0][0]
            return render_template('index.html', result=f"Prediction: {round(prediction, 2)}")

        return render_template('index.html', result="Enter values")

    except Exception as e:
        return render_template('index.html', result=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
