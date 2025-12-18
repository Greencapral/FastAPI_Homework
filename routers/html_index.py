from fastapi import APIRouter, HTTPException, status,Query,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from schemas.book_schema import BaseBook, book_list

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse, name='html_index')
async def html_index(request: Request):
    return templates.TemplateResponse("html_main_page.html", {"request": request})


