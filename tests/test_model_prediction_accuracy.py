import pickle

# Load the trained model
with open("linear_model.pkl", "rb") as file:
    model_from_pkl = pickle.load(file)

# Load the column list
with open("columns.pkl", "rb") as file:
    columns_from_pkl = pickle.load(file)


# Function to change make to dummy and make predictions
def predict_price(mileage, year, make):

    # Create a DataFrame for the input, indicator 1 or 0 for Make
    input_data = {'mileage': mileage, 'year': year, f'make_{make}': 1}
    df_input = pd.DataFrame([input_data])
    
    # Add missing columns and fill them with 0
    df_input = df_input.reindex(columns=columns_from_pkl, fill_value=0)

    # Predict using the model
    prediction = model_from_pkl.predict(df_input)

    return prediction[0]

# compare model prediction to expectation
expected_pred_price = 52000
predicted_price = predict_price(39, 2024, "Jeep")
assert abs(expected_pred_price - predicted_price) <1000
