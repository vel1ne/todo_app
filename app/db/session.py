from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import get_settings

settings = get_settings()

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


def get_db():
    """Функция для внедрения сессии базы данных."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
