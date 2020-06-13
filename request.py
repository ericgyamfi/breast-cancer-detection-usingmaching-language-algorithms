import requests
import pickle
import pandas as pd

# Load pickle file
ts

input_file = open('train_mode.pkl', 'rb')
new_dict = pickle.load(input_file)
input_file()

# Create a Pandas DataFrame
data_frame = pd.DataFrame(new_dict)

json_file = df.to_json('temp.json', orient='records', lines=True)

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'id': 8670.0, 'diagnosis': 0.0, 'radius_mean': 12.34, 'texture_mean': 14.93,
 'perimeter_mean': 82.61, 'area_mean': 512.2, 'smoothness_mean': 0.1007, 'compactness_mean': 0.1147, 
 'concavity_mean': 0.0, 'concave points_mean': 0.0, 'symmetry_mean': 0.1601, 'fractal_dimension_mean': 0.056670000000000005,
  'radius_se': 0.2204, 'texture_se': 0.8561, 'perimeter_se': 1.778, 'area_se': 16.64, 'smoothness_se': 0.0050799999999999994, 
  'compactness_se': 0.011040000000000001, 'concavity_se': 0.0, 'concave points_se': 0.0, 'symmetry_se': 0.01344,
   'fractal_dimension_se': 0.001784, 'radius_worst': 12.36, 'texture_worst': 17.7, 'perimeter_worst': 101.7, 
   'area_worst': 284.4, 'smoothness_worst': 0.1216, 'compactness_worst': 0.1486, 'concavity_worst': 0.0, 
   'concave points_worst': 0.0, 'symmetry_worst': 0.2226, 'fractal_dimension_worst': 0.07427}
)

print(r.json)