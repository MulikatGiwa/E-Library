from fastapi import APIRouter, HTTPException,status
from app.database.borrow_records import Borrow_records
from app.database.books import Books
from app.schemas.borrow_records import BorrowBook, Borrow
from app.crud.borrow import borrow_crud
from app.services.borrow import borrow_service

borrow_router = APIRouter()

@borrow_router.post("/borrow_records/{user_id}/{book_id}", status_code=status.HTTP_201_CREATED)
def create_record(record: BorrowBook):
    new_record = borrow_crud.create_record(record)
    return {"message": "Borrow Record Created Successfully", "data": new_record}

@borrow_router.post("/return/{user_id}/{book_id}", status_code=status.HTTP_200_OK)
def return_book(borrow_id: int, book_id: int):
    borrow_data = borrow_service.return_book(borrow_id, book_id)
    return {"message": " Return Recorded Successfully", "data": borrow_data}

@borrow_router.get("/borrow/records/{user_id}", status_code=status.HTTP_200_OK)
def get_record_by_id(User_id: int):
    record_by_id = borrow_crud.get_record_by_id(User_id)
    return {"message": "Successful", "data": record_by_id}

@borrow_router.get("/borrow/records", status_code=status.HTTP_200_OK)
def get_records():
    Borrow_records = borrow_crud.get_records()
    return {"message": "Successful", "data": Borrow_records}