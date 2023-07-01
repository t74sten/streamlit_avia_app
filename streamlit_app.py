import streamlit as st
import functions
from PIL import Image
import pandas as pd

image = Image.open('data/plane_2.jpg')

st.set_page_config(
        layout="wide",
        initial_sidebar_state="auto",
        page_title="Авиаперевозчик? Узнай, довольны ли пассажиры полетом",
        page_icon=image,)

st.write(
        """
        # Классификация пассажиров рейса
        ### Определяем, кому понравился полет, а кому нет.
        """)
st.write(
        """
        ##### Предложите клиенту заполнить анкету и узнайте, его отношение.
        """)

st.image(image, use_column_width='always')

st.sidebar.write('# Анкета для пассажира')

col10, col11, col12 = st.sidebar.columns(3)

with col10:
    gender = st.radio("Пол", ("Мужской", "Женский"))
    name = st.text_input("Имя", max_chars=50)
    customer_type = st.radio("Лояльность клиента", ("Лоялен", "Не лоялен"))
    type_of_travel = st.radio("Тип поездки", ("Командировка", "Личная"))
    age = st.number_input("Возраст", min_value=0, max_value=100, step=1, value=30)

with col11:
    inflight_wifi_service = st.slider("Оценка за WiFi", min_value=1, max_value=5, step=1, value=1)
    departure_arrival_time_convenient = st.slider("Оценка задержки полета", min_value=1, max_value=5, step=1, value=1)
    ease_of_online_booking = st.slider("Онлайн бронь", min_value=1, max_value=5, step=1, value=1)
    food_and_drink = st.slider("Качество питания", min_value=1, max_value=5, step=1, value=1)
    online_boarding = st.slider("Оценка места в самолете", min_value=1, max_value=5, step=1, value=1)
    seat_comfort = st.slider("Комфортабельность места", min_value=1, max_value=5, step=1, value=1)

with col12:
    inflight_entertainment = st.slider("Досуг на борту", min_value=1, max_value=5, step=1, value=1)
    on_board_service = st.slider("Качество сервиса", min_value=1, max_value=5, step=1, value=1)
    baggage_handling = st.slider("Обращение с багажом", min_value=1, max_value=5, step=1, value=1)
    checkin_service = st.slider("Оценка регистрации", min_value=1, max_value=5, step=1, value=1)
    inflight_service = on_board_service
    cleanliness = st.slider("Чистота салона", min_value=1, max_value=5, step=1, value=1)

def write_user_data(df):
    st.write("## Пассажиры")
    st.write(df)
def write_prediction(prediction):
    st.write("## Удовлетворенность полетом")
    st.write(prediction)

def prediction_side_bar_inputs():
    user_input_df = prep_data(gender,name,customer_type,type_of_travel,age,inflight_wifi_service,
              departure_arrival_time_convenient,ease_of_online_booking,food_and_drink,
              online_boarding,seat_comfort,inflight_entertainment,on_board_service,
              baggage_handling,checkin_service,inflight_service,cleanliness)
    return functions.get_predict(user_input_df)

def prep_data(gender,name,customer_type,type_of_travel,age,inflight_wifi_service,
              departure_arrival_time_convenient,ease_of_online_booking,food_and_drink,
              online_boarding,seat_comfort,inflight_entertainment,on_board_service,
              baggage_handling,checkin_service,inflight_service,cleanliness):

    translatetion = {
        "Мужской": 1,
        "Женский": 0,
        "Лоялен": 1,
        "Не лоялен": 0,
        "Командировка": 1,
        "Личная": 0
    }

    data = {'gender': translatetion[gender],'name': name,'age': age,
            'customer_type': translatetion[customer_type],
            'type_of_travel': translatetion[type_of_travel],'inflight_wifi_service': inflight_wifi_service,
            'departure_arrival_time_convenient': departure_arrival_time_convenient,
            'ease_of_online_booking': ease_of_online_booking,'food_and_drink': food_and_drink,
            'online_boarding': online_boarding,'seat_comfort': seat_comfort,
            'inflight_entertainment': inflight_entertainment,'on_board_service': on_board_service,
            'baggage_handling': baggage_handling,'checkin_service': checkin_service,
            'inflight_service': inflight_service,'cleanliness': cleanliness}

    df = pd.DataFrame(data, index=[0])

    return df

def generate_features():
    passangers = functions.create_passangers(number_passangers)
    return functions.get_predict(passangers)

def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

col1, col2, col3 = st.columns(3)

with col2:
    st.markdown('##### Попробовать на сгенерированных данных')
    number_passangers = st.number_input('Количество пассажиров для генерации',
                                        min_value=1, max_value=1000, value=1, step=1)

    if (st.button('Попробовать')):
        st.markdown('#### Параметры и предсказание')
        st.dataframe(generate_features())
        st.download_button(label="Скачать рандом данные в CSV",
                       data=convert_df(prediction_side_bar_inputs()),
                       file_name='random_passangers.csv', mime='text/csv', )

with col1:
    st.markdown('##### Узнать мнение пассажира по анкете')
    if (st.button('Узнать')):
        st.markdown('#### Параметры и предсказание')
        st.dataframe(prediction_side_bar_inputs())
        st.download_button(label="Скачать предикт в CSV",
                           data=convert_df(prediction_side_bar_inputs()),
                           file_name='prediction.csv', mime='text/csv',)

with col3:
    st.markdown('##### Узнать мнение Ваших клиентов')
    st.download_button(label="Скачать шаблон в CSV", data=convert_df(pd.read_csv('data/shablon.csv')),
                       file_name='shablon.csv', mime='text/csv',)

    uploaded_file = st.file_uploader("Загрузить шаблон с Вашими данными", accept_multiple_files=False)

    if (st.button('Получить предикт')):
        pred = functions.get_predict(pd.read_csv(uploaded_file))
        st.dataframe(pred)
        st.download_button(label="Скачать предикт по Вашим данным в CSV",
                           data=convert_df(pred),
                           file_name='prediction_for_you.csv', mime='text/csv', )
if st.button('Сбросить'):
    # Clear all widget fields
    st.sidebar.empty()
    st.empty()
