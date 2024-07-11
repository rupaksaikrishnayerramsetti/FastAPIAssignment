from Apis.Utilities.encryption import hash_password
from fastapi import HTTPException
from sqlalchemy.orm import Session
from Apis.models.Login import Login
from Models.User import User

def check_login_cred(cred: Login, db: Session):
    try:
        password_digest = hash_password(cred.password)
        user = db.query(User).filter(User.email == cred.email.lower(), User.password == password_digest).first()
        if user:
            return True
        return False
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")