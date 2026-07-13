from uuid import UUID

from pydantic import BaseModel, ConfigDict


class InstrumentRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    symbol: str
    cusip: str
    sedol: str
    isin: str
    name: str
    instrument_type: str
    currency: str
    sector: str | None