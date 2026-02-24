from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    sport_type = Column(String, nullable=True)
    experience_level = Column(String, nullable=True) # New, Intermediate, Senior
    organization = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
