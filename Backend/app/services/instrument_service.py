from sqlalchemy import UUID
from sqlalchemy.orm import Session

from Backend.app.database.models import InstrumentModel
from Backend.app.repositories.instrument_repository import InstrumentRepository
from Backend.app.schemas.instrument import InstrumentCreate


class InstrumentService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = InstrumentRepository(db)

    def create_instrument(self, payload: InstrumentCreate) -> InstrumentModel:
        existing_isin = self.repository.get_by_isin(payload.isin)
        if existing_isin is not None:
            raise ValueError(
                f"Instrument with ISIN '{payload.isin}' already exists"
            )
        exisiting_name = self.repository.get_by_name(payload.name)
        if exisiting_name is not None:
            raise ValueError(
                f"Instrument with name '{payload.name}' already exists"
            )
        existing_figi_global = self.repository.get_by_figi_global(payload.figi_global)
        if existing_figi_global is not None:
            raise ValueError(
                f"Instrument with FIGI Global '{payload.figi_global}' already exists"
            )
        insert_instrument = InstrumentModel(
            symbol=payload.symbol,
            cusip=payload.cusip,
            isin=payload.isin,
            sedol=payload.sedol,
            figi_global=payload.figi_global,
            active=payload.active,
            name=payload.name,
            instrument_type=payload.instrument_type,
        )
        instrument = self.repository.add(insert_instrument)
        self.db.commit()
        self.db.refresh(instrument)

        return instrument

    def get_instrument(self, instrument_id: UUID) -> InstrumentModel:
        instrument = self.repository.get_by_id(instrument_id)

        if instrument is None:
            raise ValueError(f"Instrument with ID '{instrument_id}' not found")

        return instrument