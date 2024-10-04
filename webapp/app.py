from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import numpy as np
import pickle

# Initialize the Flask app
app = Flask(__name__, template_folder='templates')
app.secret_key = "secret_key"

# MySQL configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mysql123'
app.config['MYSQL_DB'] = 'users'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306

# Initialize MySQL
mysql = MySQL(app)

# Load the saved diabetes prediction model
with open("C://Users//Abrar Shariff//alisha//diabetes_model.pkl", 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle registration (save user details to MySQL)
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login (authenticate user from MySQL)
        session['username'] = request.form['username']
        return redirect(url_for('predict'))
    return render_template('login.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Extract form values for prediction
        features = [float(x) for x in request.form.values()]
        final_features = [np.array(features)]
        
        # Make prediction using the loaded model
        prediction = model.predict(final_features)

        # Display prediction result
        if prediction[0] == 1:
            output = 'The person is predicted to have diabetes.'
        else:
            output = 'The person is predicted to not have diabetes.'

        return render_template('predict.html', prediction_text=output)
    
    return render_template('predict.html')

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5500, debug=True)
