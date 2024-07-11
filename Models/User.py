from sqlalchemy import Integer, Column, VARCHAR, String
from Config.database import Base

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, autoincrement=True, nullable= False)
    name = Column(VARCHAR(50), index=True, nullable= False)
    email = Column(VARCHAR(100), index=True, nullable= False)
    phone_no = Column(VARCHAR(13), index=True)
    password = Column(String(), nullable= False)
    dob = Column(VARCHAR(10))