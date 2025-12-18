from pydantic import BaseModel
from typing import Optional


class BaseBook(BaseModel):
    id: int
    title: str
    title: str
    author: str
    year: int
    description: str


class BookForEdit(BaseBook):
    id: Optional[int] = None
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None
    description: Optional[str] = None


book_list = [
    BaseBook(
        id=1,
        title="Book 1",
        author="111",
        year=2003,
        description="Book 1",
    ),
    BaseBook(
        id=2,
        title="Book 2",
        author="222",
        year=2000,
        description="Book 2",
    ),
    BaseBook(
        id=3,
        title="Book 3",
        author="333",
        year=2005,
        description="@@@Book 3",
    ),
    BaseBook(
        id=4,
        title="Book 4",
        author="444",
        year=2003,
        description="@@@Book 4",
    ),
    BaseBook(
        id=5,
        title="Book 5",
        author="555",
        year=2005,
        description="@@@Book 5",
    ),

]
