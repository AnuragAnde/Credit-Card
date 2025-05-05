from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        try:
            features = [float(request.form.get(f'feature{i}')) for i in range(1, 6)]  # Adjust number
            prediction = model.predict([features])[0]
            prediction = "Approved" if prediction == 1 else "Not Approved"
        except:
            prediction = "Invalid input. Please enter valid numbers."
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
