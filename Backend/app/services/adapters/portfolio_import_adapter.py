from typing import Protocol

import pandas as pd


class PortfolioImportAdapter(Protocol):
    def read(self) -> pd.DataFrame:
        ...