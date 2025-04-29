from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.dao_dep import get_session_commited, get_session
from app.user.dao import UsersDAO
from app.user import schemas

router = APIRouter()


@router.get(
    "",
    response_model=list[schemas.OutUserSchema]
)
async def get_all(session: AsyncSession = Depends(get_session)) -> list:
    res = await UsersDAO(session).get_list()
    return [inst.to_dict() for inst in res]


@router.get(
    "/{id}",
    response_model=schemas.OutUserSchema
)
async def get(
        id: int,
        session: AsyncSession = Depends(get_session)
):
    res = await UsersDAO(session).get(id)
    return res.to_dict()


@router.post(
    "/create",
    response_model=schemas.OutUserSchema
)
async def create(
        body: schemas.CreateUserSchema,
        session: AsyncSession = Depends(get_session_commited)
):
    res = await UsersDAO(session).create(body.model_dump())
    return res.to_dict()


@router.delete(
    "/delete",
    response_model=schemas.OutUserSchema
)
async def delete(
        id: int,
        session: AsyncSession = Depends(get_session_commited)
):
    res = await UsersDAO(session).delete(id)
    return res.to_dict()
