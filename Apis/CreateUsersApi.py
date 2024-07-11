from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from Config.database import get_db
from Apis.Utilities.UserDBUtility import create_new_user, get_user_with_id, update_user_with_id, delete_user_with_id
from Apis.models.User import User

router = APIRouter()

@router.post("/")
def create_user(user: User, db: Session = Depends(get_db)):
    try:
        user_create = create_new_user(db=db, user=user)
        if user_create:
            return {"message": "User Registered Successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server Error: {e}")
    
@router.get("/{id}")
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    try:
        data = get_user_with_id(id, db)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")
    
@router.put("/{id}")
def update_user_by_id(id: int, user: User, db: Session = Depends(get_db)):
    try:
        user_update = update_user_with_id(id, user, db)
        if user_update:
            return {"message": "User Details Updated Successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server Error: {e}")
    
@router.delete("/{id}")
def delete_user_by_id(id: int, db: Session = Depends(get_db)):
    try:
        response = delete_user_with_id(id, db)
        if response:
            return {"message": "User Account Deleted Successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")