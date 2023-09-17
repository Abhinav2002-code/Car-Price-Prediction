
def preprocess(car_data):

    car_data = car_data[car_data['year'].str.isnumeric()]
    car_data['year'] = car_data['year'].astype(int)
    car_data = car_data[car_data['Price'] != 'Ask For Price']
    car_data['Price'] = car_data['Price'].str.replace(',', '').astype(int)
    car_data['kms_driven'] = car_data['kms_driven'].str.split(' ').str.get(0).str.replace(',','')
    car_data = car_data[car_data['kms_driven'].str.isnumeric()]
    car_data['kms_driven'] = car_data['kms_driven'].astype(int)
    car_data = car_data[~car_data['fuel_type'].isna()]
    car_data['name'] = car_data['name'].str.split().str.slice(0,3).str.join(' ')
    car_data = car_data.reset_index(drop=True)
    car_data = car_data[car_data['Price'] < 6e6].reset_index(drop=True)
    car_data.to_csv('cleaned_car_data.csv')

    return car_data
