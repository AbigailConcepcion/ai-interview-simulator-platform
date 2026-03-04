from fastapi import FastAPI
from app.api import auth, session
from app.websocket.interview_ws import interview_socket

app = FastAPI()

app.include_router(auth.router, prefix="/api/auth")
app.include_router(session.router, prefix="/api/sessions")

@app.websocket("/ws/interview")
async def websocket_endpoint(websocket):
    await interview_socket(websocket)
