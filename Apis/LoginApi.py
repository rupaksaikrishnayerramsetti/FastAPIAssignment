from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from Config.database import get_db
from Apis.models.Login import Login
from Apis.Utilities.LoginDBUtility import check_login_cred

router = APIRouter()

@router.post("/")
def check_login(credentials: Login, db: Session = Depends(get_db)):
    try:
        check_status = check_login_cred(credentials, db)
        if check_status:
            return {"message": "Login Successfull"}
        return JSONResponse(status_code=401, content="Bad User Credentials")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")