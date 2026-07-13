# app/database/models/risk_result.py

import uuid
from datetime import date, datetime
from decimal import Decimal
from typing import Any

from sqlalchemy import (
    Date,
    DateTime,
    ForeignKey,
    JSON,
    Numeric,
    String,
    UniqueConstraint,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from Backend.app.database.base import Base


class RiskResultModel(Base):
    __tablename__ = "risk_results"

    __table_args__ = (
        UniqueConstraint(
            "portfolio_id",
            "metric_name",
            "calculation_date",
            "method",
            name="uq_risk_result_portfolio_metric_date_method",
        ),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )

    portfolio_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey(
            "portfolios.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    metric_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    metric_value: Mapped[Decimal] = mapped_column(
        Numeric(24, 8),
        nullable=False,
    )

    calculation_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
        index=True,
    )

    method: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        default="default",
    )

    currency: Mapped[str | None] = mapped_column(
        String(3),
        nullable=True,
    )

    parameters: Mapped[dict[str, Any] | None] = mapped_column(
        JSONB,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    portfolio = relationship(
        "PortfolioModel",
        back_populates="risk_results",
    )

    def __repr__(self) -> str:
        return (
            f"RiskResultModel("
            f"portfolio_id={self.portfolio_id}, "
            f"metric_name={self.metric_name!r}, "
            f"metric_value={self.metric_value}, "
            f"calculation_date={self.calculation_date}"
            f")"
        )