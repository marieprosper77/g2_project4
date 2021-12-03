import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load("CreditRiskModel.h2")

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
	'''
	for rendering results on HTML
	'''	
	
	# ImmutableMultiDict([('children', '3'), ('income', '20000'), ('income', '3'), ('gender', '1'), ('car', '0'), ('realty', '0')])
	# print(request.form)

	# print(pd.DataFrame(request.form.to_dict()))
	data = dict((key, request.form.getlist(key)) for key in request.form.keys())

	print(data)
	# features = [int(x) for x in request.form.values()]
	features = pd.DataFrame(data)
	print(features)

	# rename names to the names of the 

	# re-arranging the list as per data set
	# feature_list = [features[4]] + features[:4] + features[5:11][::-1] + features[11:17][::-1] + features[17:][::-1]
	# features_arr = [np.array(feature_list)]

	# prediction = model.predict(features_arr)
	prediction = model.predict(features)


	print(features)
	print("prediction value: ", prediction)

	result = ""
	if prediction == "low_risk":
		result = "The credit card application is likely to be APPROVED*"
	else:
		result = "The credit card application is likely to be DENIED*"

	return render_template('index.html', prediction_text = result)


if __name__ == '__main__':
	app.run(debug=True)