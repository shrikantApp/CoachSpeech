from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class SituationBase(BaseModel):
    sport_type: str
    athlete_age_group: str
    situation_type: str
    description: str
    parent_behavior: str
    channel: str
    tone: str
    urgency: str

class SituationCreate(SituationBase):
    pass

class SituationResponse(SituationBase):
    id: int
    user_id: int
    primary_response: Optional[str] = None
    alternate_responses: Optional[List[str]] = None
    keywords: Optional[List[str]] = None
    created_at: datetime

    class Config:
        from_attributes = True
