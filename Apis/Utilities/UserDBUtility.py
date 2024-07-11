# UserDBUtility.py

from Apis.Utilities.encryption import hash_password
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from Apis.models.User import User
from Models.User import User as UserMain

def create_new_user(db: Session, user: User):
    try:
        user_temp = db.query(UserMain).filter(UserMain.email == user.email).first()
        if user_temp:
            return JSONResponse(status_code=422, content=f"User with the email id {user.email} already exists")
        password_digest = hash_password(user.password)
        db_user = UserMain(
            name=user.name,
            email=user.email.lower(),
            phone_no=user.phone_no,
            password=password_digest,
            dob=user.dob
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return True
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error {e}")
    finally:
        db.close()

def get_user_with_id(id: int, db: Session):
    try:
        response = db.query(UserMain).filter(UserMain.user_id == id).first()
        if not response:
            return JSONResponse(status_code=422, content=f"User with the user id {id} doesn't exist")
        updated_response = UserMain(
            user_id=response.user_id,
            name=response.name,
            email=response.email,
            phone_no=response.phone_no,
            dob=response.dob
        )
        return updated_response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error {e}")
    finally:
        db.close()

def update_user_with_id(id: int, user: User, db: Session):
    try:
        response = db.query(UserMain).filter(UserMain.user_id == id).first()
        if not response:
            return JSONResponse(status_code=422, content=f"User with the user id {id} doesn't exist")
        response.name = user.name
        response.email = user.email.lower()
        response.phone_no = user.phone_no
        response.dob = user.dob
        response.password = hash_password(user.password)
        db.commit()
        return True
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error {e}")
    finally:
        db.close()

def delete_user_with_id(id: int, db: Session):
    try:
        temp = db.query(UserMain).filter(UserMain.user_id == id).first()
        if not temp:
            raise HTTPException(status_code=404, detail=f"Data not found as per the User {id} given")
        db.delete(temp)
        db.commit()
        return True
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error {e}")
    finally:
        db.close()
