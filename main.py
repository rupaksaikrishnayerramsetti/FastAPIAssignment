from fastapi import FastAPI
from Apis import CreateUsersApi, LoginApi
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ['*']

app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(CreateUsersApi.router, prefix="/user", tags=["User"])

app.include_router(LoginApi.router, prefix="/Login", tags=["Login"])