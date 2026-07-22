from sqlalchemy import Enum

class CsvType(str, Enum):
    FREETRADE = "freetrade"
    CSV = "csv"