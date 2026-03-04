from fastapi import WebSocket

async def interview_socket(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"AI Feedback for: {data}")
