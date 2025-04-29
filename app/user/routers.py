from typing import List
from fastapi import APIRouter, Response, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.user.models import Users
# from app.auth.utils import authenticate_user, set_tokens
# from app.dependencies.auth_dep import get_current_user, get_current_admin_user, check_refresh_token
from app.dependencies.dao_dep import get_session_commited, get_session
from app.exceptions import UserAlreadyExistsException, IncorrectEmailOrPasswordException
from app.user.dao import UsersDAO
from app.user import schemas

# from app.auth.schemas import SUserRegister, SUserAuth, EmailModel, SUserAddDB, SUserInfo

router = APIRouter()


@router.get("")
async def register_user(session: AsyncSession = Depends(get_session)) -> list:
    res = await UsersDAO(session).get_list()
    return [inst.to_dict() for inst in res]


@router.get("/{id}")
async def register_user(
        id: int,
        session: AsyncSession = Depends(get_session)
):
    res = await UsersDAO(session).get(id)
    return res.to_dict()


@router.post(
    "/create",
    response_model=schemas.UserOutSchema
)
async def register_user(
        body: schemas.UserCreateSchema,
        session: AsyncSession = Depends(get_session)
):
    res = await UsersDAO(session).create(body)
    return res.to_dict()

#
# @router.post("/login/")
# async def auth_user(
#         response: Response,
#         user_data: SUserAuth,
#         session: AsyncSession = Depends(get_session_without_commit)
# ) -> dict:
#     users_dao = UsersDAO(session)
#     user = await users_dao.find_one_or_none(
#         filters=EmailModel(email=user_data.email)
#     )
#
#     if not (user and await authenticate_user(user=user, password=user_data.password)):
#         raise IncorrectEmailOrPasswordException
#     set_tokens(response, user.id)
#     return {
#         'ok': True,
#         'message': 'Авторизация успешна!'
#     }
#
#
# @router.post("/logout")
# async def logout(response: Response):
#     response.delete_cookie("user_access_token")
#     response.delete_cookie("user_refresh_token")
#     return {'message': 'Пользователь успешно вышел из системы'}
#
#
# @router.get("/me/")
# async def get_me(user_data: User = Depends(get_current_user)) -> SUserInfo:
#     return SUserInfo.model_validate(user_data)
#
#
# @router.get("/all_users/")
# async def get_all_users(session: AsyncSession = Depends(get_session_with_commit),
#                         user_data: User = Depends(get_current_admin_user)
#                         ) -> List[SUserInfo]:
#     return await UsersDAO(session).find_all()
#
#
# @router.post("/refresh")
# async def process_refresh_token(
#         response: Response,
#         user: User = Depends(check_refresh_token)
# ):
#     set_tokens(response, user.id)
#     return {"message": "Токены успешно обновлены"}
