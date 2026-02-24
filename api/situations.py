from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from core.database import get_db
from core.dependencies import get_current_user
from models.user import User
from models.situation import Situation
from schemas.situation import SituationCreate, SituationResponse
from services.ai import generate_coach_response

router = APIRouter(prefix="/situations", tags=["situations"])

@router.post("/", response_model=SituationResponse)
def create_situation(situation_in: SituationCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # 1. Generate Response using AI
    ai_response = generate_coach_response(situation_in)
    
    # 2. Save situation to DB
    new_situation = Situation(
        user_id=current_user.id,
        sport_type=situation_in.sport_type,
        athlete_age_group=situation_in.athlete_age_group,
        situation_type=situation_in.situation_type,
        description=situation_in.description,
        parent_behavior=situation_in.parent_behavior,
        channel=situation_in.channel,
        tone=situation_in.tone,
        urgency=situation_in.urgency,
        primary_response=ai_response.get("primary_response", ""),
        alternate_responses=ai_response.get("alternate_responses", []),
        keywords=ai_response.get("keywords", [])
    )
    db.add(new_situation)
    db.commit()
    db.refresh(new_situation)
    return new_situation

@router.get("/", response_model=List[SituationResponse])
def get_situations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    situations = db.query(Situation).filter(Situation.user_id == current_user.id).order_by(Situation.created_at.desc()).offset(skip).limit(limit).all()
    return situations

@router.get("/{situation_id}", response_model=SituationResponse)
def get_situation(situation_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    situation = db.query(Situation).filter(Situation.id == situation_id, Situation.user_id == current_user.id).first()
    if not situation:
        raise HTTPException(status_code=404, detail="Situation not found")
    return situation
