from fastapi import FastAPI
import uvicorn
from routers.api_router import router as api_router
from routers.html_index import router as index_router

app = FastAPI()

app.include_router(api_router, prefix="/api") #роутер для API запросов
app.include_router(index_router) #роутер для html-работы

if __name__ == '__main__':
    uvicorn.run('app:app', host="127.0.0.1", port=8080, reload=True)


