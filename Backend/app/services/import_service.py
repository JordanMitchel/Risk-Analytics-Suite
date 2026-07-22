import pandas as pd

from Backend.app.database.models import PortfolioModel, InstrumentModel, PriceModel
from Backend.app.repositories.instrument_repository import InstrumentRepository
from Backend.app.repositories.portfolio_repository import PortfolioRepository
from Backend.app.repositories.price_repository import PriceRepository
from Backend.app.services.adapters.portfolio_import_adapter import PortfolioImportAdapter
from Backend.app.services.portfolio_normalizer import PortfolioNormalizer


class ImportService:
    def __init__(self,
                 adapter: PortfolioImportAdapter,
                 normalizer: PortfolioNormalizer,
                 portfolio_repo: PortfolioRepository,
                 instrument_repo: InstrumentRepository,
                 price_repo: PriceRepository):

        self.adapter = adapter
        self.normalizer = normalizer
        self.portfolio_repo  = portfolio_repo
        self.instrument_repo = instrument_repo
        self.price_repo = price_repo


    def _import_porfolio(self, series: pd.Series) -> None:
        portfolio_model: PortfolioModel = PortfolioModel(
            name=series["portfolio_name"],
            description=series.get("portfolio_description"),
        )
        self.portfolio_repo.add(portfolio_model)

    def _import_instrument(self, series: pd.Series) -> None:
        instrument_model = self.instrument_repo.get_by_symbol(series["symbol"])
        if not instrument_model:
            instrument = self.instrument_repo.add(
                InstrumentModel(
                    symbol=series["symbol"],
                    instrument_type=series.get("instrument_type"),
                    name=series.get("instrument_name"),
                    currency=series.get("currency"),

                    sector = series.get("sector"),
                    cusip = series.get("cusip"),
                    isin = series.get("isin"),
                    sedol = series.get("sedol")

                #
                )
            )



    def _import_price(self, series: pd.Series) -> None:
        price_model = self.price_repo.get_by_instrument_id(series["symbol"])
        if price_model:
            return price_model
        else:
            price = self.price_repo.add(
                PriceModel(
                    instrument_id=series["symbol"],
                    date=series.get("date"),
                    price=series.get("price"),
                )
            )
        return price

    def import_data(self, file):
        df = self.adapter.read()
        normalized_df = self.normalizer.prepare(df)

        for _, row in normalized_df.iterrows():
            self._import_porfolio(row)
            self._import_instrument(row)
            self._import_price(row)

        return {"message": "Import completed successfully."}