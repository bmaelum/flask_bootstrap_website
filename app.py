from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime

import json
import requests
import os

app = Flask(__name__)

## Get connection details for APIs
#dataprep_api_url = os.environ['DATAPREP_API_URL'] # change to your app name

@app.route('/', methods=['POST', 'GET'])
def index():

    return render_template('index.html')

@app.route('/prediction/', methods=['GET', 'POST'])
def dataprediction():
    if request.method == 'POST':
        age_content = request.form['age']
        pclass      = request.form['pclass']
        sibsp       = request.form['sibsp']
        fare        = request.form['fare']


        # sample data
        data = {'Pclass': pclass
              , 'Age': age_content
              , 'SibSp': sibsp
              , 'Fare': fare}

        data_to_api = json.dumps(data)

        try:
            send_request_deployed = requests.post(dataprep_api_url, data_to_api)
            print(send_request_deployed)
            api_response = send_request_deployed.json()
            print(send_request_deployed.json())

            ages = Todo.query.order_by(Todo.date_created).all()
            return render_template('prediction.html', data=data, api_status=send_request_deployed, api_response=api_response)
        except:
            return 'There was a problem accessing the prediction API'

    

@app.route('/feature_engineering/')
def feature_engineering():
    print('Hei')
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
