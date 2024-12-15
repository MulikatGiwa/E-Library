from fastapi import FastAPI
from app.routers.users import user_router
from app.routers.books import book_router
from app.routers.borrow import borrow_router

app=FastAPI()

app.include_router(user_router, tags=["Users"])

app.include_router(book_router, tags=["Books"])

app.include_router(borrow_router, tags=["Borrow"])

