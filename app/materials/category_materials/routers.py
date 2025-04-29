from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.dao_dep import get_session_commited, get_session
from app.materials.category_materials.dao import CategoryMaterialsDAO as Dao
from app.materials.category_materials.schemas import (
    OutCategoryMaterialsSchema as OutSchema,
    CreateCategoryMaterialsSchema as CreateSchema,
    UpdateCategoryMaterialsSchema as UpdateSchema
)

router = APIRouter()


@router.get(
    "",
    response_model=list[OutSchema]
)
async def get_all(session: AsyncSession = Depends(get_session)) -> list:
    res = await Dao(session).get_list()
    return [inst.to_dict() for inst in res]


@router.get(
    "/{id}",
    response_model=OutSchema
)
async def get(
        id: int,
        session: AsyncSession = Depends(get_session)
):
    res = await Dao(session).get(id)
    return res.to_dict()


@router.post(
    "/create",
    response_model=OutSchema
)
async def create(
        body: CreateSchema,
        session: AsyncSession = Depends(get_session_commited)
):
    res = await Dao(session).create(body.model_dump())
    return res.to_dict()


@router.delete(
    "/delete",
    response_model=OutSchema
)
async def delete(
        id: int,
        session: AsyncSession = Depends(get_session_commited)
):
    res = await Dao(session).delete(id)
    return res.to_dict()
