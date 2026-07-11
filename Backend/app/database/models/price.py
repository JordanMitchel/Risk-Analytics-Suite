# app/database/models/price.py

import uuid
from datetime import date
from decimal import Decimal

from sqlalchemy import Date, ForeignKey, Numeric, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from Backend.app.database.base import Base


class PriceModel(Base):
    __tablename__ = "prices"

    __table_args__ = (
        UniqueConstraint(
            "instrument_id",
            "price_date",
            name="uq_price_instrument_date",
        ),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )

    instrument_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey(
            "instruments.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    price_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
        index=True,
    )

    close_price: Mapped[Decimal] = mapped_column(
        Numeric(20, 8),
        nullable=False,
    )

    currency: Mapped[str] = mapped_column(
        String(3),
        nullable=False,
    )

    instrument = relationship(
        "InstrumentModel",
        back_populates="prices",
    )

    def __repr__(self) -> str:
        return (
            f"PriceModel("
            f"instrument_id={self.instrument_id}, "
            f"price_date={self.price_date}, "
            f"close_price={self.close_price}"
            f")"
        )