import datetime

from sqlalchemy import UUID, select
from sqlalchemy.orm import Session

from Backend.app.database.models import PriceModel


class PriceRepository:
    def __init__(self, db: Session):
        self.db = db

    def add(self, price: PriceModel) -> PriceModel:
        self.db.add(price)
        self.db.flush()
        return price

    def get_by_id(self, price_id:UUID) -> PriceModel:
        ...

    def get_by_instrument_id(self, instrument_id:UUID):
        ...

    def get_todays_prices(self)-> list[PriceModel]:
        prices = select(PriceModel).where(PriceModel.date == datetime.date.today
                                          ()).order_by(
            PriceModel.created_at.desc()
        )
        return list(self.db.scalars(prices))
