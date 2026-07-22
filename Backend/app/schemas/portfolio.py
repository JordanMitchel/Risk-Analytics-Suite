from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
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

@dataclass
class PortfolioImportRow(BaseModel):
    portfolio_name: str
    base_currency: str

    symbol: str
    instrument_name: str
    instrument_type: str
    currency: str

    quantity: Decimal
    average_cost: Decimal

    sector: str | None = None
    cusip: str | None = None
    isin: str | None = None
    sedol: str | None = None
    figi_global: str |None = None