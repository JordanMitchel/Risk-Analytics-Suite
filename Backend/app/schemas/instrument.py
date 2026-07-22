from uuid import UUID

from pydantic import BaseModel, ConfigDict, field_validator


class InstrumentCreate(BaseModel):
    symbol: str
    cusip: str | None
    sedol: str | None
    isin: str | None
    figi_global: str | None
    name: str
    instrument_type: str
    currency: str
    sector: str | None

    @field_validator("currency")
    @classmethod
    def normalise_currency(cls, value: str) -> str:
        return value.upper()

class InstrumentRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    symbol: str
    cusip: str | None
    sedol: str | None
    isin: str | None
    figi_global: str | None
    name: str
    instrument_type: str
    currency: str
    sector: str | None