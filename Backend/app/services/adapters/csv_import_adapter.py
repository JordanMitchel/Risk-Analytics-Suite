from typing import BinaryIO

import pandas as pd


class CsvImportAdapter:
    def __init__(self,file:BinaryIO):
        self.file = file
    def read(self) -> pd.DataFrame:
        return pd.read_csv(self.file)
