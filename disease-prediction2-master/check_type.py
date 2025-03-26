import joblib

# Load the trained model
model = joblib.load('trained_model2')

# Print the model type
print(type(model))