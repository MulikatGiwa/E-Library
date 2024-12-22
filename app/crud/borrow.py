from fastapi import HTTPException,status
from app.database.borrow_records import Borrow_records
from app.database.users import Users
from app.database.books import Books
from app.schemas.borrow_records import BorrowBook, Borrow
from app.utils.current_date import current_date

class BorrowCrud:
    
    @staticmethod
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
    
    @staticmethod
    def get_record_by_id(User_id: int):
        user=Users.get(User_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "User not found")
        record_by_id = {id:record for id, record in Borrow_records.items() if record["user_id"] == User_id}
        if not record_by_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "User borrow record does not exist")
        return record_by_id

    @staticmethod
    def get_records():
        return Borrow_records
    
borrow_crud = BorrowCrud ()