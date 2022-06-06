from datetime import datetime

from pydantic import BaseModel, Field, validator

from .item_photos import ItemPhotoInfo
from ..responses import FOUND_NOT_ALLOWED_SYMBOLS, WHITESPACE_ONLY_FORBIDDEN
from ..security.text import find_not_allowed_symbols


class ItemBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=40)
    description: str | None = None

    @validator('name')
    def name_validator(cls, value):
        if (banned := find_not_allowed_symbols(value)) != []:
            raise ValueError(FOUND_NOT_ALLOWED_SYMBOLS + ', '.join(banned))
        assert value.isspace() is False, WHITESPACE_ONLY_FORBIDDEN
        return value

    @validator('description')
    def description_validator(cls, value):
        if value is None:
            return

        if (banned := find_not_allowed_symbols(value)) != []:
            raise ValueError(FOUND_NOT_ALLOWED_SYMBOLS + ', '.join(banned))
        assert value.isspace() is False, WHITESPACE_ONLY_FORBIDDEN
        return value


class ItemCreateForm(ItemBase):
    pass


class ItemCreate(ItemBase):
    owner_id: int


class ItemUpdateForm(ItemBase):
    name: str | None = Field(None, min_length=3, max_length=40)


class ItemUpdate(ItemUpdateForm):
    is_locked: bool | None = None


class ItemInfo(BaseModel):
    id: int
    owner_id: int | None
    name: str
    description: str | None
    photos: list[ItemPhotoInfo]

    class Config:
        orm_mode = True


class ItemInfoExtended(ItemInfo):
    is_locked: bool
    created_at: datetime
