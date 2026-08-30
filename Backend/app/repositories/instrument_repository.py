from uuid import UUID

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from Backend.app.database.models import InstrumentModel


class InstrumentRepository:
    def __init__(self, db:Session):
        self.db = db

    def add(self,instrument: InstrumentModel) -> InstrumentModel:
        self.db.add(instrument)
        self.db.flush()
        return instrument

    def get_by_id(self, instrument_id: UUID, check_active:bool = False) ->InstrumentModel:
        if check_active:
            statement = select(InstrumentModel).where(
                InstrumentModel.id == instrument_id,
                InstrumentModel.active == True
            )
        else:
            statement = select(InstrumentModel).where(InstrumentModel.id == instrument_id)
        instrument = self.db.execute(statement).scalar_one_or_none()
        if instrument is None:
            raise HTTPException(status_code=404, detail="Instrument not found")

        return instrument

    def get_instruments_by_symbol(self, name:str, check_active:bool = False) -> list[InstrumentModel]:
        if check_active:
            statement = select(InstrumentModel).where(
                InstrumentModel.name == name,
                InstrumentModel.active == True
            )
        else:
           statement = select(InstrumentModel).where(InstrumentModel.name == name)

        instruments = self.db.execute(statement).scalars().all()

        if not instruments:
            raise HTTPException(status_code=404, detail="Instruments not found")

        return list(instruments)

    def get_by_isin(self, isin: str, check_active:bool= False) -> InstrumentModel | None:
        if check_active:
            statement = select(InstrumentModel).where(
                InstrumentModel.isin == isin,
                InstrumentModel.active == True
            )
        else:
            statement = select(InstrumentModel).where(InstrumentModel.isin == isin)
        instrument = self.db.execute(statement).scalar_one_or_none()
        if instrument is None:
            raise HTTPException(status_code=404, detail="Instrument not found")
        return instrument

    def get_by_name(self, name: str, check_active:bool= False) -> InstrumentModel | None:
        if check_active:
            statement = select(InstrumentModel).where(
                InstrumentModel.name == name,
                InstrumentModel.active == True
            )
        else:
            statement = select(InstrumentModel).where(InstrumentModel.name == name)
        instrument = self.db.execute(statement).scalar_one_or_none()
        if instrument is None:
            raise HTTPException(status_code=404, detail="Instrument not found")
        return instrument

    def get_by_figi_global(self, figi_global: str, check_active:bool= False) -> InstrumentModel | None:
        if check_active:
            statement = select(InstrumentModel).where(
                InstrumentModel.figi_global == figi_global,
                InstrumentModel.active == True
            )
        else:
            statement = select(InstrumentModel).where(InstrumentModel.figi_global == figi_global)
        instrument = self.db.execute(statement).scalar_one_or_none()
        if instrument is None:
            raise HTTPException(status_code=404, detail="Instrument not found")
        return instrument

    def list_all_active_instruments(self) -> list[InstrumentModel]:

        statement = select(InstrumentModel).where(InstrumentModel.active).order_by(
            InstrumentModel.created_at.desc()
        )
        instruments = self.db.execute(statement).scalars()
        return list(instruments)
