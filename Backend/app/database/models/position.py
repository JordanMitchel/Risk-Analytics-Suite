import uuid
from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from Backend.app.database.base import Base


class PositionModel(Base):
    __tablename__ = "positions"

    __table_args__ = (
        UniqueConstraint(
            "portfolio_id",
            "instrument_id",
            name="uq_position_portfolio_instrument",
        ),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )
    portfolio_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("portfolios.id"),
        nullable=False,
    )
    instrument_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("instruments.id"),
        nullable=False,
    )
    quantity: Mapped[Decimal] = mapped_column(
        Numeric(20, 6),
        nullable=False,
    )
    average_cost: Mapped[Decimal] = mapped_column(
        Numeric(20, 6),
        nullable=False,
    )

    portfolio = relationship(
        "PortfolioModel",
        back_populates="positions",
    )
    instrument = relationship(
        "InstrumentModel",
        back_populates="positions",
    )