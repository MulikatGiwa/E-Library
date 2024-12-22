from pydantic import BaseModel
from datetime import date

class BorrowBase(BaseModel):
    user_id: int
    book_id: int

class Borrow(BorrowBase):
    borrow_id: int
    borrow_date: date
    return_date: date | None = None

class BorrowBook(BorrowBase):
    pass

class ReturnBook(Borrow):
    return_date: date