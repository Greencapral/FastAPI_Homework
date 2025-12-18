from fastapi import APIRouter,Query, HTTPException, status
from schemas.book_schema import BaseBook, book_list

router = APIRouter()

@router.get("/books", response_model=list[BaseBook])
async def get_books():
    return book_list