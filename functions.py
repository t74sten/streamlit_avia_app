import joblib
import pandas as pd
from random import randrange
import names

def create_passangers(len_pass_list=1):
    passenger_list = []

    features_list = ['gender', 'name', 'customer_type', 'type_of_travel', 'age', 'inflight_wifi_service',
                     'departure_arrival_time_convenient', 'ease_of_online_booking', 'food_and_drink',
                     'online_boarding', 'seat_comfort', 'inflight_entertainment',
                     'on_board_service', 'baggage_handling', 'checkin_service', 'inflight_service', 'cleanliness']

    dff = ['gender', 'name', 'age', 'customer_type', 'type_of_travel', 'inflight_wifi_service',
           'departure_arrival_time_convenient', 'ease_of_online_booking', 'food_and_drink',
           'online_boarding', 'seat_comfort', 'inflight_entertainment', 'on_board_service',
           'baggage_handling', 'checkin_service', 'inflight_service', 'cleanliness']

    while len(passenger_list) < len_pass_list:
        passanger = []
        for i in dff:
            if i in features_list[0]:
                a = randrange(2)
                passanger.append(a)
                if a == 1:
                    passanger.append(names.get_full_name(gender='male'))
                else:
                    passanger.append(names.get_full_name(gender='female'))
            elif i in features_list[1]:
                continue
            elif i in features_list[2:4]:
                passanger.append(randrange(2))
            elif i in features_list[4]:
                passanger.append(randrange(100))
            else:
                passanger.append(randrange(1, 6))
        passenger_list.append(passanger)

    return pd.DataFrame(passenger_list, columns=dff)


def get_predict(df):
    model = joblib.load('data/model_fin.sav')

    data_f = df
    data = df.drop(columns=['name'])

    pred_n = model.predict(data)

    pred = pd.DataFrame(pred_n, columns=['satisfied_prediction']).replace({1: 'Удовлетворен', 0: 'Неудовлетворен'})
    data_f['pred'] = pred

    data_f = data_f[['name','pred','gender','age','customer_type','type_of_travel','inflight_wifi_service',
           'departure_arrival_time_convenient','ease_of_online_booking','food_and_drink',
           'online_boarding','seat_comfort','inflight_entertainment','on_board_service',
           'baggage_handling','checkin_service','inflight_service','cleanliness']]

    return data_f
