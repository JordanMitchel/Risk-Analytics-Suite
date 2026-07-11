import uuid

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from Backend.app.database.base import Base


class InstrumentModel(Base):
    __tablename__ = "instruments"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )

    symbol: Mapped[str] = mapped_column(
        String(30),
        unique=True,
        nullable=False,
    )

    cusip: Mapped[str | None] = mapped_column(
        String(30),
        unique=True,
        nullable=True,
    )

    isin: Mapped[str | None] = mapped_column(
        String(30),
        unique=True,
        nullable=True,
    )

    sedol: Mapped[str | None] = mapped_column(
        String(30),
        unique=True,
        nullable=True,
    )

    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    instrument_type: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    currency: Mapped[str] = mapped_column(
        String(3),
        nullable=False,
    )

    sector: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    positions = relationship(
        "PositionModel",
        back_populates="instrument",
    )

    prices = relationship(
        "PriceModel",
        back_populates="instrument",
        cascade="all, delete-orphan",
        order_by="PriceModel.price_date",
    )