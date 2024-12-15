from fastapi import APIRouter, HTTPException,status
from typing import Annotated
from app.database.books import Books
from app.schemas.books import Book, BookCreate, BookUpdate
from app.crud.books import book_crud

book_router = APIRouter()

@book_router.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book:BookCreate):
    new_book = book_crud.create_book(book)
    return {"message": "Book registered Succesfully", "data": new_book}

@book_router.get("/books", status_code=status.HTTP_200_OK)
def get_books():
    Books=book_crud.get_books()
    return {"message": "Succesful", "data": Books}

@book_router.get("/books/{book_id}", status_code=status.HTTP_200_OK)
def get_book(book_id:int):
    book = book_crud.get_book(book_id)
    return {"message": "Succesful", "data": book}

@book_router.put("/books/{book_id}")
def update_book(book_id:int, update_data:BookUpdate):
    updated_book = book_crud.update_book(book_id, update_data)
    return {"message": "User updated Succesfully", "data": updated_book}

@book_router.patch("/books/{book_id}")
def mark_book_unavailable(book_id:int):
    unavailable_book = book_crud.mark_book_unavailable(book_id)
    return {"message": "Book marked unavailable successfully", "data": unavailable_book}

@book_router.delete("/books/{book_id}")
def delete_book(book_id:int):
    book_crud.delete_book(book_id)
    return {"message": "Book deleted successfully"}