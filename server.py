from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import streamlit

app = FastAPI()

# Функция для обновления состояния Streamlit
def update_streamlit_state(telegram_id):
    streamlit.server.server.update_session_state(
        {'last_telegram_id': telegram_id}
    )

@app.post("/update_telegram_id")
async def update_telegram_id(request: Request):
    data = await request.json()
    telegram_id = data.get('telegram_id')

    if telegram_id:
        # Обновление состояния Streamlit
        update_streamlit_state(telegram_id)

    return JSONResponse({"message": "Telegram ID updated successfully"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
