from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator


class PortfolioCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    base_currency: str = Field(min_length=3, max_length=3)

    @field_validator("base_currency")
    @classmethod
    def normalise_currency(cls, value: str) -> str:
        return value.upper()


class PortfolioRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: str
    base_currency: str
    created_at: datetime