from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from Backend.app.schemas.instrument import InstrumentRead


class PositionRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    portfolio_id: UUID
    instrument_id: UUID
    quantity: Decimal
    average_cost: Decimal
    instrument: InstrumentRead