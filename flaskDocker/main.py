# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask,request
import pandas as pd
import numpy as np
import pickle
import flasgger
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)
pickle_in = open('classifier.pkl','rb')
classifier = pickle.load(pickle_in)
@app.route('/')
def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    return ("welcome")  # Press Ctrl+F8 to toggle the breakpoint.
@app.route('/predict',methods=['get'])
def predict_note():
    """variable or single values.
    wow
    ---
    parameters():
        - name: variance
          in: query
          type: number
          required: true
        - name: skewness
          in: query
          type: number
          required: true
        - name: curtosis
          in: query
          type: number
          required: true
        - name: entropy
          in: query
          type: number
          required: true
    responses:
        200:
            description: Returns a list of users
    """
    variance = request.args.get('variance')
    skewness =request.args.get('skewness')
    curtosis =request.args.get('curtosis')
    entropy= request.args.get('entropy')
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    return "the predicted value is "+str(prediction)

@app.route('/predict_file',methods=["POST"])
def predict_mult():
    """ file.
    wow
    ---
    parameters:
        - name: file
          in: formDate
          type: file
          required: true
    responses:
       200:
           description: The output values
    """
    print("wow")
    df = pd.read_csv(request.files.get("file"))
    print(df.head())
    prediction=classifier.predict(df)
    return str(list(prediction))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.debug=True
    app.run()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
