import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder

from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer
from sklearn.model_selection import train_test_split

import preprocessing


def modelling(input_df):
    car_data = pd.read_csv('quikr_car.csv')
    car_data = preprocessing.preprocess(car_data)
    X = car_data.drop(columns='Price', axis=1)
    Y = car_data['Price']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=124)
    ohe = OneHotEncoder()
    ohe.fit(X[['name', 'company', 'fuel_type']])
    column_trans = make_column_transformer(
        (OneHotEncoder(categories=ohe.categories_), ['name', 'company', 'fuel_type']), remainder='passthrough')
    lr = LinearRegression()
    pipe = make_pipeline(column_trans, lr)
    pipe.fit(X_train, Y_train)
    # input_df = pd.DataFrame(input_data)
    prediction = pipe.predict(input_df)

    return prediction
