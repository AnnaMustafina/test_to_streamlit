import streamlit as st
from flask import Flask, request

app = Flask(__name__)

# Хранение Telegram ID
telegram_id = None

@app.route('/webhook', methods=['POST'])
def webhook():
    global telegram_id
    data = request.json
    if 'message' in data:
        telegram_id = data['message']['from']['id']
    return '', 200

@app.route('/update_telegram_id', methods=['POST'])
def update_telegram_id():
    global telegram_id
    data = request.json
    telegram_id = data['telegram_id']
    print(f"Received Telegram ID: {telegram_id}")
    return '', 200

# Streamlit интерфейс
st.title("Telegram ID Display")
if telegram_id:
    st.write(f"Telegram ID: {telegram_id}")
else:
    st.write("Ожидание сообщения от Telegram...")

#bot_token = "6647621334:AAG5CiIbxm07vSVV0XLuPFOgtRhdyClS1AE"
#webhook_url = "https://app-to-test-j3ojcxof7bphybygqqvkct.streamlit.app"





chart_data = pd.DataFrame(
    {
        "col1": list(range(20)) * 3,
        "col2": np.random.randn(60),
        "col3": ["A"] * 20 + ["B"] * 20 + ["C"] * 20,
    }
)

st.bar_chart(chart_data, x="col1", y="col2", color="col3")
