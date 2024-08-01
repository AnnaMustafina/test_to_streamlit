import streamlit as st
import requests
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import json

# Хранение Telegram ID
telegram_id = None

class StreamlitWebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        global telegram_id
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)

        if 'telegram_id' in data:
            telegram_id = data['telegram_id']
            print(f"Received Telegram ID: {telegram_id}")

        self.send_response(200)
        self.end_headers()

def run_streamlit_server():
    server_address = ('', 8501)  # Порт по умолчанию для Streamlit
    httpd = HTTPServer(server_address, StreamlitWebhookHandler)
    print('Starting Streamlit webhook server...')
    httpd.serve_forever()

# Запуск сервера в отдельном потоке
threading.Thread(target=run_streamlit_server, daemon=True).start()

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
