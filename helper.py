import preprocessing
import numpy as np
import pandas as pd

car_data = pd.read_csv('quikr_car.csv')
car_data = preprocessing.preprocess(car_data)


def company():
    companies = car_data['company'].unique()
    return companies


def name(company_name):
    models = car_data[car_data['name'].str.split(' ').str.get(0) == company_name]
    return models['name'].unique()


def year():
    years = car_data['year'].unique()
    years = sorted(years)
    return years


def fuel_type():
    return car_data['fuel_type'].unique()
