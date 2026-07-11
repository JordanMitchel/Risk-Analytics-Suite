from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from Backend.app.database.session import get_db
from Backend.app.schemas.portfolio import PortfolioCreate, PortfolioRead
from Backend.app.services.portfolio_service import PortfolioService


router = APIRouter(
    prefix="/portfolios",
    tags=["portfolios"],
)


@router.post(
    "",
    response_model=PortfolioRead,
    status_code=status.HTTP_201_CREATED,
)
def create_portfolio(
    payload: PortfolioCreate,
    db: Session = Depends(get_db),
) -> PortfolioRead:
    service = PortfolioService(db)

    try:
        portfolio = service.create_portfolio(payload)
        return PortfolioRead.model_validate(portfolio)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        ) from exc


@router.get(
    "",
    response_model=list[PortfolioRead],
)
def list_portfolios(
    db: Session = Depends(get_db),
) -> list[PortfolioRead]:
    service = PortfolioService(db)
    portfolios = service.list_portfolios()
    return [PortfolioRead.model_validate(portfolio) for portfolio in portfolios]