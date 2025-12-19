from pydantic import BaseModel
from typing import Optional


class BaseBook(BaseModel):
    id: int
    title: str
    author: str
    year: str
    description: str


class BookForEdit(BaseBook):
    id: Optional[int] = None
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[str] = None
    description: Optional[str] = None


books_list = [
    BaseBook(
        id=0,
        title="Чистый Python: тонкости программирования для профи",
        author="Бейдер, Д.",
        year="2022",
        description="288 с.",
    ),
    BaseBook(
        id=1,
        title="Python для сложных задач: наука о данных и машинное обучение",
        author="Вандер Плас, Дж.",
        year="2022",
        description="576 с.",
    ),
    BaseBook(
        id=2,
        title="Разработка веб‑приложений с использованием Flask на языке Python: практическое руководство",
        author="Гринберг, М.",
        year="2023",
        description="273 с.",
    ),
    BaseBook(
        id=3,
        title="Программируем на Python",
        author="Доусон, М.",
        year="2022",
        description="416 с.",
    ),
    BaseBook(
        id=4,
        title="Введение в машинное обучение с помощью Python: руководство для специалистов по работе с данными",
        author="Мюллер, А.",
        year="2017",
        description="480 с.",
    ),

]
