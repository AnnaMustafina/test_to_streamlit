import streamlit as st
import requests

st.title('Telegram ID')

st.write('Ожидание Telegram ID...')

@st.experimental_api
def telegram_id(telegram_id):
    st.write(f'Telegram ID: {telegram_id}')

def api_endpoint():
    if st.experimental_get_query_params():
        telegram_id = st.experimental_get_query_params()['telegram_id'][0]
        telegram_id(telegram_id)

api_endpoint()


#bot_token = "6647621334:AAG5CiIbxm07vSVV0XLuPFOgtRhdyClS1AE"
#webhook_url = "https://app-to-test-j3ojcxof7bphybygqqvkct.streamlit.app"


#chart_data = pd.DataFrame(
#    {
#        "col1": list(range(20)) * 3,
#        "col2": np.random.randn(60),
#        "col3": ["A"] * 20 + ["B"] * 20 + ["C"] * 20,
#    }
#)

#st.bar_chart(chart_data, x="col1", y="col2", color="col3")
