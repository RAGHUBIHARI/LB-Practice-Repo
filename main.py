from flask import Flask, render_template, request
import numpy as np
import pickle
import joblib

# initialize the app
app=Flask(__name__)

@app.route('/')
def form():
    return render_template('diabetics.html')


@app.route('/predict',methods=['post'])
def predict():
    value1=int(request.form.get('Pregnancies'))
    value2=int(request.form.get('Glucose'))
    value3=int(request.form.get('BloodPressure'))
    value4=int(request.form.get('SkinThickness'))
    value5=int(request.form.get('Insulin'))
    value6=int(request.form.get('BMI'))
    value7=int(request.form.get('DiabetesPedigreeFunction'))
    value8=int(request.form.get('Age'))

    #print("value1=",value1,"value2=",value2)

    # convert input to array
    input_data = np.array([[value1,value2,value3,value4,value5,value6,value7,value8]])

    # Load Model and predict
    model = joblib.load('model_job.pkl')

    prediction = model.predict(input_data)
    #print(prediction)
    prediction1 = int(prediction)
    #print(prediction1)
    if prediction1 == 1:
        return "Person is diabetic"
    
    
    return "Person is not diabetic"


# Run the app(locally)
#app.run(debug=True)

# specify the port number and accept any ip address
app.run(port=8888, host='0.0.0.0')