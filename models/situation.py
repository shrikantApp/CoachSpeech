from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from core.database import Base

class Situation(Base):
    __tablename__ = "situations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Context
    sport_type = Column(String, nullable=False)
    athlete_age_group = Column(String, nullable=False)
    situation_type = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    parent_behavior = Column(String, nullable=False)
    channel = Column(String, nullable=False)
    tone = Column(String, nullable=False)
    urgency = Column(String, nullable=False)
    
    # Generated Responses
    primary_response = Column(Text, nullable=True)
    alternate_responses = Column(JSON, nullable=True) # list of strings
    keywords = Column(JSON, nullable=True) # list of strings
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", backref="situations")
