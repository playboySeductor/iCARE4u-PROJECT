from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('heartdisease.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("heartdisease.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict(final)
    if prediction==1:
        return render_template('heartdisease.html', prediction_text="Oops! The predicted value is [1]. The person seems to have Heart Disease.")
    else:
        return render_template('heartdisease.html', prediction_text="Great! The predicted value is [0]. The person does not have any Heart Disease.")

if __name__=="__main__":
    app.run(debug=True)
