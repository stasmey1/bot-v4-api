from contextlib import asynccontextmanager
from typing import AsyncGenerator
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from loguru import logger

from app.user.routers import router as router_users


# @asynccontextmanager
# async def lifespan(app: FastAPI) -> AsyncGenerator[dict, None]:
#     """Управление жизненным циклом приложения."""
#     logger.info("Инициализация приложения...")
#     yield
#     logger.info("Завершение работы приложения...")


def create_app() -> FastAPI:
    """
   Создание и конфигурация FastAPI приложения.

   Returns:
       Сконфигурированное приложение FastAPI
   """
    app = FastAPI(
        # title="Стартовая сборка FastAPI",
        # # description=(
        # #     "Стартовая сборка с интегрированной SQLAlchemy 2 для разработки FastAPI приложений с продвинутой "
        # #     "архитектурой, включающей авторизацию, аутентификацию и управление ролями пользователей.\n\n"
        # #     "**Автор проекта**: Яковенко Алексей\n"
        # #     "**Telegram**: https://t.me/PythonPathMaster"
        # # ),
        # version="1.0.0",
        # lifespan=lifespan,
    )

    # Настройка CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    # # Монтирование статических файлов
    # app.mount(
    #     '/static',
    #     StaticFiles(directory='app/static'),
    #     name='static'
    # )

    # Регистрация роутеров
    register_routers(app)

    return app


def register_routers(app: FastAPI) -> None:
    """Регистрация роутеров приложения."""
    # Корневой роутер
    router_root = APIRouter()

    @router_root.get("/", tags=["root"])
    def home_page():
        return {
            "message": "Добро пожаловать! Проект создан для сообщества 'Легкий путь в Python'.",
            "community": "https://t.me/PythonPathMaster",
            "author": "Яковенко Алексей"
        }

    # Подключение роутеров
    app.include_router(router_root, tags=["root"])
    app.include_router(router_users, prefix='/users', tags=['Users'])


# Создание экземпляра приложения
app = create_app()
