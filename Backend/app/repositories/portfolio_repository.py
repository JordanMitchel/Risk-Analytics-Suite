from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from Backend.app.database.models.portfolio import PortfolioModel


class PortfolioRepository:
    def __init__(self, db: Session):
        self.db = db

    def add(self, portfolio: PortfolioModel) -> PortfolioModel:
        self.db.add(portfolio)
        self.db.flush()
        return portfolio

    def get_by_id(self, portfolio_id: UUID) -> PortfolioModel | None:
        statement = (
            select(PortfolioModel)
            .where(PortfolioModel.id == portfolio_id)
            .options(
                selectinload(PortfolioModel.positions),
            )
        )
        return self.db.scalar(statement)

    def get_by_name(self, name: str) -> PortfolioModel | None:
        statement = select(PortfolioModel).where(
            PortfolioModel.name == name
        )
        return self.db.scalar(statement)

    def list_all(self) -> list[PortfolioModel]:
        statement = select(PortfolioModel).order_by(
            PortfolioModel.created_at.desc()
        )
        return list(self.db.scalars(statement))