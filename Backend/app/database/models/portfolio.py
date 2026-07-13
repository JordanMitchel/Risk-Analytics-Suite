import uuid
from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from Backend.app.database.base import Base


class PortfolioModel(Base):
    __tablename__ = "portfolios"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )
    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )
    base_currency: Mapped[str] = mapped_column(
        String(3),
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    positions = relationship(
        "PositionModel",
        back_populates="portfolio",
        cascade="all, delete-orphan",
    )

    risk_results = relationship(
        "RiskResultModel",
        back_populates="portfolio",
        cascade="all, delete-orphan",
        order_by="RiskResultModel.calculation_date",
    )