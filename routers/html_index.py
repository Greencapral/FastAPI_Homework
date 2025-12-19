from django.db.models.expressions import result
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from schemas.book_schema import books_list, BookForEdit

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse, name='html_index')
async def html_index(request: Request):
    """
    Функция возвращает гравную страницу
    """
    return templates.TemplateResponse("html_main_page.html", {"request": request})


@router.get("/about/", response_class=HTMLResponse, name='html_about')
async def html_about(request: Request):
    """
    Функция возвращает страницу об авторе
    """
    return templates.TemplateResponse("html_about.html", {"request": request})


@router.get("/books/", response_class=HTMLResponse, name='html_books_list')
async def html_books(request: Request):
    """
    Функция возвращает список книг
    """
    result = books_list

    context = {
        "request": request,
        "books_list": result
    }
    return templates.TemplateResponse("html_books_list.html", context=context)


@router.get("/books/{id}/", response_class=HTMLResponse, name='html_book')
async def html_book(request: Request, id: int):
    """
    Функция возвращает расширенную информацию об одной книге
    """
    result = books_list[id]
    context = {
        "request": request,
        "book": result
    }
    return templates.TemplateResponse("html_book_description.html", context=context)


@router.get("/addbook/", response_class=HTMLResponse, name='html_book_add')
async def html_book_add(request: Request):
    """
    Функция возвращает страницу для ввода новой книги
    """
    return templates.TemplateResponse("html_book_add.html", {"request": request})


@router.post("/addbook/", name='html_post')
async def html_book_add(request: Request, author: str = Form(...), title: str = Form(...), year: str = Form(...),
                        description: str = Form(...)):
    """
    Функция принимает данные и записывает новую запись в список
    """
    max_id = len(books_list)
    new_book = BookForEdit(id = max_id, author=author, title=title, year=year, description=description)
    books_list.append(new_book)
    context = {
        "request": request,
        "books_list": books_list
    }
    return templates.TemplateResponse("html_books_list.html", context=context)

