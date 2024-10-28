from typing import Annotated
from sqlmodel import Field, Session, SQLModel, create_engine, select

class Availability(SQLModel, table=True):
    sap: str
    status0: bool
    status1: bool
    status2: bool
    status3: bool
    status4: bool
    status5: bool
    status6: bool
    status7: bool
    status8: bool
    status9: bool
    status10: bool
    status11: bool
    status12: bool
    status13: bool
    status14: bool
    status15: bool
    status16: bool
    status17: bool
    status18: bool
    status19: bool
    status20: bool
    status21: bool
    status22: bool
    status23: bool
