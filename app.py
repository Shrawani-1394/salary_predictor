from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load your trained model
with open('salary_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    experience = int(request.form['experience'])
    education = int(request.form['education'])
    
    features = np.array([[experience, education]])
    prediction = model.predict(features)

    return render_template('index.html', result=f'Predicted Salary: ₹{int(prediction[0])}')

if __name__ == '__main__':
    app.run(debug=True)
