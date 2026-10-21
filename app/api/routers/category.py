from fastapi import APIRouter, Depends, HTTPException, status

from app.api.dependencies import get_category_service
from app.schemas.category import Category, CategoryCreate, CategoryUpdate
from app.services.category import CategoryNotFound, CategoryService

router_category = APIRouter(prefix="/categories")


@router_category.get("")
def read_categories(
    category_service: CategoryService = Depends(get_category_service),
) -> list[Category]:
    return category_service.list_category()


@router_category.post("", status_code=status.HTTP_201_CREATED)
def create_category(
    payload: CategoryCreate,
    category_service: CategoryService = Depends(get_category_service),
) -> Category:
    return category_service.create_category(category_create=payload)


@router_category.patch("/{category_id}")
def update_category(
    category_id: str,
    payload: CategoryUpdate,
    category_service: CategoryService = Depends(get_category_service),
) -> Category:
    try:
        return category_service.update_category(
            category_id=category_id, category_update=payload
        )
    except CategoryNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router_category.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(
    category_id: str, category_service: CategoryService = Depends(get_category_service)
) -> None:
    try:
        return category_service.delete_category(category_id=category_id)
    except CategoryNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
