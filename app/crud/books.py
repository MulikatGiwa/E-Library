from fastapi import HTTPException,status
from app.database.books import Books
from app.schemas.books import Book, BookCreate, BookUpdate

class BookCrud:
    
    @staticmethod
    def create_book(book:BookCreate):
        for Id, book_data in Books.items():
            if  book_data["title"] == book.title:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Book title already exists")
        book_id = len(Books)+1
        new_book=Book(id=book_id, **book.model_dump())
        Books[book_id]= new_book.model_dump()
        return new_book

    @staticmethod
    def get_books():
        return Books
    
    @staticmethod
    def get_book(book_id:int):
        book=Books.get(book_id)
        if not book:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Book not found")
        return book
    
    @staticmethod
    def update_book(book_id:int, update_data:BookUpdate):
        updated_book = Books.get(book_id)
        if not updated_book:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Book not found")
        for key, values in update_data.model_dump(exclude_unset=True).items():
            if key in updated_book:
                updated_book[key] = values
            return updated_book
            
    @staticmethod
    def delete_book(book_id:int):
        deleted_book = Books.get(book_id)
        if not deleted_book:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Book not found")
        del Books[book_id]
        return

book_crud = BookCrud()