import streamlit as st
import pandas as pd
import numpy as np
#from id_list import id_now
import requests

bot_token = "6647621334:AAG5CiIbxm07vSVV0XLuPFOgtRhdyClS1AE"
webhook_url = "https://app-to-test-j3ojcxof7bphybygqqvkct.streamlit.app"

# Получите данные от Telegram
def get_data_from_telegram(data):
    # Извлеките Telegram ID из данных
    user_id = data.get("message", {}).get("from", {}).get("id")
    st.write(f"Получен Telegram ID: {user_id}")
# Обработка webhook
if st.button("Получить данные из Telegram"):
    response = requests.get(webhook_url)
    if response.status_code == 200:
        data = response.json()
        get_data_from_telegram(data)
    else:
        st.error("Ошибка получения данных")
  
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
