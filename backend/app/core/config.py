import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://postgres:postgres@postgres:5432/interview"
)

SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")
REDIS_URL = "redis://redis:6379/0"
