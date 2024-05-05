from fastapi import FastAPI
from auth_route import auth_router
from users_route import user_router
app = FastAPI()

app.include_router(auth_router)
app.include_router(user_router)

@app.get('/')
async def root():
    return {"server":"true"}