from fastapi import APIRouter
from app.models.session import InterviewSession

router = APIRouter()

@router.post("/")
async def create_session(role: str):
    session = InterviewSession(role=role)
    return {"message": "Session created", "role": role}
