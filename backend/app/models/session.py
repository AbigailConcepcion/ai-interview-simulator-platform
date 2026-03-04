from sqlalchemy import Column, Integer, ForeignKey, Text
from .base import Base

class InterviewSession(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    role = Column(Text)
    score = Column(Integer, default=0)
