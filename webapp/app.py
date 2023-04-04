# import MySQLdb
import pickle
import sys; print(sys.path)
import mysql.connector
from flask import Flask, redirect, render_template, request, session, url_for
from flask_mysqldb import MySQL 
import joblib
import numpy as np
# from my_blueprint import bp

# import MySQLdb as mysql

# app = Flask(__name__)
app=Flask(__name__,template_folder='templates')

app.secret_key = "hello"

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mysql123'
app.config['MYSQL_DB'] = 'users'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306

mysql = MySQL(app)


# Load the saved model
with open("C://Users//Abrar Shariff//alisha//diabetes_model.pkl", 'rb') as f:
    model = pickle.load(f)
    
    


# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     # Get the input values from the form
#     glucose = float(request.form['glucose'])
#     blood_pressure = float(request.form['blood_pressure'])
#     insulin = float(request.form['insulin'])
#     bmi = float(request.form['bmi'])

#     # Use the trained model to make a prediction
#     prediction = model.predict([[glucose, blood_pressure, insulin, bmi]])

#     # Return the prediction as a string
#     return render_template('predict.html','The predicted outcome is {}'.format(prediction[0]))

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask_mysqldb import MySQL

# app = Flask(__name__)
# # app.config['MYSQL_HOST'] = 'localhost'
# # app.config['MYSQL_USER'] = 'root'
# # app.config['MYSQL_PASSWORD'] = 'root'
# # app.config['MYSQL_DB'] = 'diabetes'

# # mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Validate and save registration details in MySQL
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Validate and authenticate user using MySQL
        session['username'] = request.form['username']
        return redirect(url_for('predict'))
    return render_template('login.html')

@app.route('/test',methods=['GET','POST'])
def test():
    if request.method == 'POST':
        return render_template('test.html')
    return render_template('predict.html')

# @app.route('/predict', methods=['GET', 'POST'])
# def predict():
#     model = joblib.load('C://Users//Abrar Shariff//alisha//diabetes_model.pkl')
#     if request.method == 'POST':
#         # Fetch user data from HTML form and pass to model for predict
#         # Get the input values from the form
#         glucose = float(request.form['glucose'])
#         blood_pressure = float(request.form['blood_pressure'])
#         insulin = float(request.form['insulin'])
#         bmi = float(request.form['bmi'])
#         diabetes_pedigree_function = float(request.form['diabetes_pedigree_function'])
#         age = float(request.form['age'])
#         skin_thickness = float(request.form['skin_thickness'])
#         pregnancies = float(request.form['pregnancies'])


# #     # Use the trained model to make a prediction
#         prediction = model.predict([[glucose, blood_pressure, insulin, bmi,age,pregnancies,skin_thickness,diabetes_pedigree_function]])

# #     # Return the prediction as a string
#         #return render_template('predict.html','The predicted outcome is {}'.format(prediction[0]))
#     #return render_template('predict.html')
#     if prediction[0] == 0:
#         message = "The predicted outcome is not diabetic."
#     else:
#         message = "The predicted outcome is diabetic."
#         return render_template('predict.html', message=message)

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)

    if prediction == 1:
        output = 'The person is predicted to have diabetes.'
    else:
        output = 'The person is predicted to not have diabetes.'

    return render_template('predict.html', prediction_text=output)

    #     return render_template('predict.html', {{predict}})
    # return render_template('predict.html')

if __name__ == '__main__':
    # app.secret_key = 'mysecretkey'
     #app.run(debug=True)
    app.run(host="127.0.0.1", port=5500, debug=True)
