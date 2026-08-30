from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session

from Backend.app.database.session import get_db
from Backend.app.schemas.instrument import InstrumentRead, InstrumentCreate
from Backend.app.services.instrument_service import InstrumentService

router = APIRouter(
    prefix ="/instruments",
    tags=["instruments"]
)

@router.post("",
             response_model=InstrumentRead,
             status_code=status.HTTP_201_CREATED)
def create_instrument(
        payload: InstrumentCreate,
        db: Session = Depends(get_db),
) -> InstrumentRead:
    service = InstrumentService(db)

    try:
        instrument = service.create_instrument(payload)
        return InstrumentRead.model_validate(instrument)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        ) from exc

@router.get("/{instrument_id}",)
def get_instrument(
        instrument_id: str,
        db: Session = Depends(get_db),
) -> InstrumentRead:
    service = InstrumentService(db)

    try:
        instrument = service.get_instrument(instrument_id)
        return InstrumentRead.model_validate(instrument)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc