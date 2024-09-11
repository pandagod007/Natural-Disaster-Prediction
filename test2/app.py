from flask import Flask, render_template, request
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the dataset
df = pd.read_csv('natural_disaster_prediction_data.csv')

# Define a dummy logic function to predict natural disasters
def predict_disaster(row):
    # For demonstration purposes, let's assume a simple weighted sum of features
    weights = [0.2, 0.3, 0.1, 0.1, 0.1, 0.1, 0.1]
    features = [row['Location_Risk_Factor'], row['Population_Density'], row['Historical_Frequency'], 
                row['Infrastructure_Quality'], row['Climate_Volatility'], row['Response_Readiness'], 
                row['Economic_Impact']]
    score = np.dot(features, weights)
    if score > 0.5:
        return 'High Risk'
    else:
        return 'Low Risk'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the input values from the form
        location_risk_factor = float(request.form['location_risk_factor'])
        population_density = float(request.form['population_density'])
        historical_frequency = float(request.form['historical_frequency'])
        infrastructure_quality = float(request.form['infrastructure_quality'])
        climate_volatility = float(request.form['climate_volatility'])
        response_readiness = float(request.form['response_readiness'])
        economic_impact = float(request.form['economic_impact'])
        time_of_year = request.form['time_of_year']

        # Create a new row with the input values
        new_row = pd.DataFrame({'Location_Risk_Factor': [location_risk_factor], 
                                'Population_Density': [population_density], 
                                'Historical_Frequency': [historical_frequency], 
                                'Infrastructure_Quality': [infrastructure_quality], 
                                'Climate_Volatility': [climate_volatility], 
                                'Response_Readiness': [response_readiness], 
                                'Economic_Impact': [economic_impact], 
                                'Time_of_Year': [time_of_year]})

        # Predict the disaster risk
        prediction = predict_disaster(new_row.iloc[0])

        # Render the result page
        return render_template('result.html', prediction=prediction)
    else:
        # Render the input form
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)