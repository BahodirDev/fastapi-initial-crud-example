from fastapi import APIRouter, status, HTTPException
from schemas import SignUp
from models import User
from database import SessionLocal, engine

auth_router = APIRouter(prefix='/auth')
session = SessionLocal(bind=engine)

@auth_router.get('/')
async def auth():
    return {'msg': "auth"}

@auth_router.post('/signup', status_code=status.HTTP_201_CREATED)
async def signup(user: SignUp):
    print(user)
    prev_user = session.query(User).filter(User.username == user.username).first()
    print(prev_user)
    if prev_user is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User already exists')
    new_user = User(
        username=user.username,
        email=user.email,
        password=user.password,
    )
    session.add(new_user)
    session.commit()
    return new_user
