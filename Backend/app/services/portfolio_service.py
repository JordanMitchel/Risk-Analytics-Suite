from sqlalchemy.orm import Session

from Backend.app.database.models.portfolio import PortfolioModel
from Backend.app.repositories.portfolio_repository import PortfolioRepository
from Backend.app.schemas.portfolio import PortfolioCreate


class PortfolioService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = PortfolioRepository(db)

    def create_portfolio(
        self,
        payload: PortfolioCreate,
    ) -> PortfolioModel:
        existing = self.repository.get_by_name(payload.name)

        if existing is not None:
            raise ValueError(
                f"Portfolio '{payload.name}' already exists"
            )

        portfolio = PortfolioModel(
            name=payload.name,
            base_currency=payload.base_currency,
        )

        self.repository.add(portfolio)
        self.db.commit()
        self.db.refresh(portfolio)

        return portfolio

    def list_portfolios(self) -> list[PortfolioModel]:
        return self.repository.list_all()