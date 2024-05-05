from fastapi import APIRouter, status, HTTPException
from models import User
from schemas import UserEdit
from database import SessionLocal, engine

user_router = APIRouter(prefix='/user')
session = SessionLocal(bind=engine)

@user_router.get('/list')
async def users():
   users = session.query(User).all()
   print(users)
   return users

@user_router.put('/edit/{user_id}',response_model=UserEdit)
async def edit_user(user_id: int, user: UserEdit):
    print(f"user_id = {user_id}, user- {user}")
    edited_user = session.query(User).filter(User.id == user_id).first()
    print(f"edited {edited_user}")
    if edited_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    edited_user.username = user.username
    edited_user.email = user.email
    edited_user.password = user.password
    edited_user.is_active = user.is_active
    edited_user.is_staff = user.is_staff
    
    session.commit()
    return {
        "name":edited_user.username,
        "email":edited_user.email,
        "password":edited_user.password,
        "is_staff": edited_user.is_staff,
        "is_active": edited_user.is_active
    }

@user_router.delete('/del/{user_id}', response_model=UserEdit)
async def delete_user(user_id: int):
    deleted_user = session.query(User).filter(User.id == user_id).first()
    if deleted_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    session.delete(deleted_user)
    session.commit()
    
    return {
        "name":deleted_user.username,
        "email":deleted_user.email,
        "password":deleted_user.password,
        "is_staff":deleted_user.is_staff,
        "is_active":deleted_user.is_active
    }



