from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.dao_dep import get_session_commited, get_session
from app.materials.compliments.dao import ComplimentsDAO as Dao
from app.materials.compliments import schemas

router = APIRouter()


@router.get(
    "",
    response_model=list[schemas.OutComplimentsSchema]
)
async def get_all(session: AsyncSession = Depends(get_session)) -> list:
    res = await Dao(session).get_list()
    return [inst.to_dict() for inst in res]


@router.get(
    "/{id}",
    response_model=schemas.OutComplimentsSchema
)
async def get(
        id: int,
        session: AsyncSession = Depends(get_session)
):
    res = await Dao(session).get(id)
    return res.to_dict()


@router.post(
    "/create",
    response_model=schemas.OutComplimentsSchema
)
async def create(
        body: schemas.CreateComplimentsSchema,
        session: AsyncSession = Depends(get_session_commited)
):
    res = await Dao(session).create(body.model_dump())
    return res.to_dict()


@router.delete(
    "/delete",
    response_model=schemas.OutComplimentsSchema
)
async def delete(
        id: int,
        session: AsyncSession = Depends(get_session_commited)
):
    res = await Dao(session).delete(id)
    return res.to_dict()
