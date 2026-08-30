import pandas as pd


class FreeTradeImportAdapter:
    def __init__(self,file):
        self.file = file

    def read(self):
        df = pd.DataFrame(self.file)
