import streamlit as st
import pandas as pd
import numpy as np
#from id_list import id_now
import requests

bot_token = "6647621334:AAG5CiIbxm07vSVV0XLuPFOgtRhdyClS1AE"
webhook_url = "https://app-to-test-j3ojcxof7bphybygqqvkct.streamlit.app"

# Функция для обновления Telegram ID
def update_telegram_id(telegram_id):
    st.session_state.last_telegram_id = telegram_id

# Обработка POST запроса от бота
def handle_api_request():
    if st.session_state.last_telegram_id:
        st.write(f"Последний Telegram ID: {st.session_state.last_telegram_id}")
    else:
        st.write("Еще не было запросов от бота.")

# Создание API точки для обновления Telegram ID
@st.experimental_api(show_spinner=False)
def api_update_telegram_id():
    data = st.experimental_get_query_params()
    if 'telegram_id' in data:
        telegram_id = data['telegram_id'][0]
        update_telegram_id(telegram_id)

api_update_telegram_id()
handle_api_request()


#if id_now =='IU13488':
#    st.write('Привет, пользователь', id_now)
#else:
#    st.write('Привет, таинственный незнакомец')

chart_data = pd.DataFrame(
    {
        "col1": list(range(20)) * 3,
        "col2": np.random.randn(60),
        "col3": ["A"] * 20 + ["B"] * 20 + ["C"] * 20,
    }
)

st.bar_chart(chart_data, x="col1", y="col2", color="col3")
