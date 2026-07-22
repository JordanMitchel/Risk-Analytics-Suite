import logging
import pandas as pd

from Backend.app.schemas.portfolio import PortfolioImportRow

logger = logging.getLogger(__name__)
class PortfolioNormalizer:
    def prepare(self, dataframe:pd.DataFrame)-> pd.DataFrame:

        dataframe = self._normalise_columns(dataframe)
        self._validate_columns(dataframe)

        dataframe = self._normalise_text(dataframe)
        dataframe = self._normalise_symbols(dataframe)
        dataframe = self._normalise_currencies(dataframe)
        dataframe = self._normalise_numbers(dataframe)

        self._validate_rows(dataframe)
        return dataframe

    @staticmethod
    def _validate_columns(dataframe):
        required_columns = {
            name
            for name,field in PortfolioImportRow.model_fields.items()
            if field.is_required()
        }

        optional_columns = {
            name
            for name, field in PortfolioImportRow.model_fields.items()
            if not field.is_required()
        }

        actual_columns = set(dataframe.columns)
        missing_columns = required_columns - actual_columns

        if missing_columns:
            missing = ", ".join(sorted(missing_columns))

            logger.error(
                "Missing required portfolio columns: %s",
                missing,
            )
            raise ValueError(f"Missing required columns: {missing}")

        allowed_columns = required_columns | optional_columns
        unexpected_columns = actual_columns - allowed_columns

        if unexpected_columns:
            logger.warning(
                "Ignoring unexpected columns: %s",
                ", ".join(sorted(unexpected_columns)),
            )


    @staticmethod
    def _normalise_columns(dataframe: pd.DataFrame) -> pd.DataFrame:
        dataframe = dataframe.copy()

        dataframe.columns = (
            dataframe.columns
            .astype(str)
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )

        return dataframe

    @staticmethod
    def _normalise_symbols(dataframe: pd.DataFrame) -> pd.DataFrame:
        dataframe = dataframe.copy()

        dataframe["symbol"] = (
            dataframe["symbol"]
            .astype("string")
            .str.strip()
            .str.upper()
        )

        return dataframe

    @staticmethod
    def _normalise_currencies(dataframe: pd.DataFrame) -> pd.DataFrame:
        dataframe = dataframe.copy()

        for column in ["base_currency", "currency"]:
            dataframe[column] = (
                dataframe[column]
                .astype("string")
                .str.strip()
                .str.upper()
            )

        return dataframe

    @staticmethod
    def _normalise_numbers(dataframe: pd.DataFrame) -> pd.DataFrame:
        dataframe = dataframe.copy()

        dataframe["quantity"] = pd.to_numeric(
            dataframe["quantity"],
            errors="coerce",
        )

        dataframe["average_cost"] = pd.to_numeric(
            dataframe["average_cost"],
            errors="coerce",
        )

        return dataframe

    @staticmethod
    def _normalise_text(dataframe: pd.DataFrame) -> pd.DataFrame:
        dataframe = dataframe.copy()

        text_columns = [
            "portfolio_name",
            "instrument_name",
            "instrument_type",
            "sector",
            "cusip",
            "isin",
            "sedol",
            "figi_global"
        ]

        for column in text_columns:
            if column in dataframe.columns:
                dataframe[column] = (
                    dataframe[column]
                    .astype("string")
                    .str.strip()
                )

        return dataframe

    @staticmethod
    def _validate_rows(dataframe: pd.DataFrame,
    ) -> None:
        if dataframe.empty:
            raise ValueError(
                "The portfolio import contains no rows"
            )

        if dataframe["portfolio_name"].nunique(dropna=True) != 1:
            raise ValueError(
                "Each import must contain exactly one portfolio"
            )

        if dataframe["symbol"].isna().any():
            raise ValueError("symbol cannot be blank")

        if dataframe["symbol"].eq("").any():
            raise ValueError("symbol cannot be blank")

        if dataframe["quantity"].isna().any():
            raise ValueError("quantity must be numeric")

        if dataframe["quantity"].eq(0).any():
            raise ValueError("quantity cannot be zero")

        if dataframe["average_cost"].isna().any():
            raise ValueError("average_cost must be numeric")

        if dataframe["average_cost"].lt(0).any():
            raise ValueError("average_cost cannot be negative")

        invalid_base_currency = (
                dataframe["base_currency"].isna()
                | dataframe["base_currency"].str.len().ne(3)
        )

        if invalid_base_currency.any():
            raise ValueError(
                "base_currency must contain three letters"
            )

        invalid_currency = (
                dataframe["currency"].isna()
                | dataframe["currency"].str.len().ne(3)
        )

        if invalid_currency.any():
            raise ValueError(
                "currency must contain three letters"
            )

    def normalize(self, df):
        pass

