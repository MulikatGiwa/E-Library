from fastapi import HTTPException,status
from app.database.books import Books

class BookService:
    
    @staticmethod
    def mark_book_unavailable(book_id:int):
        unavailable_book = Books.get(book_id)
        if not unavailable_book:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Book not found")
        if unavailable_book["is_available"] != True:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail= "Book is not available")
        unavailable_book["is_available"] = False
        return unavailable_book
    
book_service = BookService ()