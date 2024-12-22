from fastapi import HTTPException,status
from app.database.borrow_records import Borrow_records
from app.database.books import Books
from app.schemas.borrow_records import Borrow
from app.utils.current_date import current_date

class BorrowService:
    
    @staticmethod
    def return_book(borrow_id: int, book_id: int):
        borrow_data: Borrow = Borrow_records.get(borrow_id)
        if not borrow_data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Borrow record does not exist")
        borrow_data["return_date"] = current_date()
        Books[book_id]["is_available"] = True
        return borrow_data
    
borrow_service = BorrowService()