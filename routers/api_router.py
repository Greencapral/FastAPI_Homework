from fastapi import APIRouter,Query, HTTPException, status
from schemas.book_schema import BaseBook, books_list

router = APIRouter()

@router.get("/books", response_model=list[BaseBook])
async def get_books():
    """
    Функция возвращает захардкоженный список книг из schemas.book_schema

    """
    return books_list