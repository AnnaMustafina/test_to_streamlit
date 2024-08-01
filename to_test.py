import streamlit as st
import pandas as pd
import numpy as np
#from id_list import id_now
import requests

bot_token = "6647621334:AAG5CiIbxm07vSVV0XLuPFOgtRhdyClS1AE"
webhook_url = "https://app-to-test-j3ojcxof7bphybygqqvkct.streamlit.app"

# Получение данных о Telegram ID
def get_last_user_id():
       response = requests.get('https://app-to-test-j3ojcxof7bphybygqqvkct.streamlit.app')
       if response.status_code == 200:
           return response.json()['user_id']
       else:
           return None

last_user_id = get_last_user_id()
if last_user_id:
   st.write("Последний Telegram ID: " + str(last_user_id))
else:
   st.write("Нет данных о Telegram ID")
  
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
