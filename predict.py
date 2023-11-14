import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklarn.preprocessing import OneHotEncoder

df = pd.read_csv('out.csv' , sep=';' )


# Assuming you have a dataframe called 'df' with columns 'var1', 'var2', 'var3', and 'target'
df['state'] = df['state'].astype('category')

# Split the data into training and testing sets
X = df[['state', 'nombre_de_chambre', 'surface_living']]
y = df['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create the DMatrix for training and testing
dtrain = xgb.DMatrix(data=X_train, label=y_train, enable_categorical=True)
dtest = xgb.DMatrix(data=X_test, label=y_test, enable_categorical=True)

# Set the parameters for XGBoost
params = {
    'objective': 'reg:squarederror',
    'eval_metric': 'rmse'
}

# Train the XGBoost model
xgb_model = xgb.train(params=params, dtrain=dtrain)

# Make predictions on the test set
y_pred = xgb_model.predict(dtest)

# Evaluate the model using mean squared error
mse = mean_squared_error(y_test, y_pred)


def predict_price(state, nombre_de_chambre, surface_living):
    # Assuming you have a trained XGBoost model called 'xgb_model'

    # Create a DMatrix for the input data with enable_categorical=True
    data = pd.DataFrame({'state': [state], 'nombre_de_chambre': [nombre_de_chambre], 'surface_living': [surface_living]})
    data['state'] = data['state'].astype('category')
    dmatrix = xgb.DMatrix(data=data, enable_categorical=True)

    # Make predictions using the trained model
    prediction = xgb_model.predict(dmatrix)[0]

    return prediction


