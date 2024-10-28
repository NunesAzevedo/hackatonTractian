from typing import Annotated
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Tool(SQLModel, table=True):
    sap: str
    category: str
    description: str
