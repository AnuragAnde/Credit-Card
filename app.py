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
            # Get inputs from form
            age = float(request.form['age'])
            income = float(request.form['income'])
            credit_score = float(request.form['credit_score'])
            loan_amount = float(request.form['loan_amount'])

            # Prepare input array
            features = [age, income, credit_score, loan_amount]

            # Make prediction
            pred = model.predict([features])[0]
            prediction = "Approved" if pred == 1 else "Not Approved"
        except Exception as e:
            prediction = "Invalid input. Please enter valid numbers."
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
