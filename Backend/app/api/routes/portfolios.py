from fastapi import APIRouter, Depends, HTTPException, status, UploadFile
from sqlalchemy.orm import Session

from Backend.app.database.session import get_db
from Backend.app.repositories.instrument_repository import InstrumentRepository
from Backend.app.repositories.portfolio_repository import PortfolioRepository
from Backend.app.repositories.price_repository import PriceRepository
from Backend.app.schemas.portfolio import PortfolioCreate, PortfolioRead
from Backend.app.services.adapters.csv_import_adapter import CsvImportAdapter
from Backend.app.services.adapters.freetrade_import_adapter import FreeTradeImportAdapter
from Backend.app.services.import_service import ImportService
from Backend.app.services.portfolio_normalizer import PortfolioNormalizer
from Backend.app.services.portfolio_service import PortfolioService
from Backend.app.types.csv_types import CsvType

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


@router.post("/csv_import_portfolio")
def csv_import_portfolio(
        file: UploadFile,
        file_type: CsvType,
        db: Session = Depends(get_db)
):
    adapter = None
    match file_type:
        case CsvType.FREETRADE:
            adapter = FreeTradeImportAdapter(file.file)
        case CsvType.CSV:
            adapter = CsvImportAdapter(file.file)

    normalizer = PortfolioNormalizer()
    import_service = ImportService(adapter=adapter,
                  normalizer=normalizer,
                  portfolio_repo= PortfolioRepository(db=db),
                  instrument_repo= InstrumentRepository(db=db),
                  price_repo= PriceRepository(db=db))
    return import_service.import_data(file)

@router.post("/freetrade_import_portfolio")
def csv_import_portfolio(
        file: UploadFile,
        db: Session = Depends(get_db)
):
    adapter = CsvImportAdapter(file.file)
    normalizer = PortfolioNormalizer()
    import_service = ImportService(adapter=adapter,
                  normalizer=normalizer,
                  portfolio_repo= PortfolioRepository(db=db),
                  instrument_repo= InstrumentRepository(db=db),
                  price_repo= PriceRepository(db=db))
    return import_service.import_data(file)

@router.get("/list_portfolios", response_model=list[PortfolioRead])
def list_portfolios(
    db: Session = Depends(get_db),
) -> list[PortfolioRead]:
    service = PortfolioService(db)
    portfolios = service.list_portfolios()
    return [PortfolioRead.model_validate(portfolio) for portfolio in portfolios]