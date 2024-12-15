from fastapi import APIRouter, HTTPException,status
from typing import Annotated
from app.database.borrow_records import Borrow_records
from app.database.users import Users
from app.database.books import Books
from app.schemas.borrow_records import BorrowBook, Borrow, ReturnBook
from app.crud.books import book_crud
from app.utils.current_date import current_date

borrow_router = APIRouter()

@borrow_router.post("/borrow_records/{user_id}/{book_id}")
def create_record(record: BorrowBook):
    user = Users.get(record.user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "User not found")
    if not user["is_active"] == True:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail= "Inactive user")
    book = Books.get(record.book_id)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Book not found")
    if not book["is_available"] == True:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail= "Unavailable book")
    id = len(Borrow_records) +1
    new_record= Borrow(borrow_id =id, borrow_date= current_date(), **record.model_dump())
    Borrow_records[id]= new_record.model_dump()
    book["is_available"] = False
    return new_record


@borrow_router.post("/return/{user_id}/{book_id}")
def return_book(borrow_id: int, book_id: int):
    borrow_data: Borrow = Borrow_records.get(borrow_id)
    if not borrow_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Borrow record does not exist")
    borrow_data["return_date"] = current_date()
    Books[book_id]["is_available"] = True
    return borrow_data



@borrow_router.get("/borrow/records")
def get_records():
    return Borrow_records