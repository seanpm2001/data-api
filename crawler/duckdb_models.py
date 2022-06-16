from pathlib import Path

# from sqlalchemy import Boolean, Column, Integer, Sequence, String, create_engine
from sqlalchemy.engine import Engine

# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()


import pandas as pd
from pydantic import BaseModel

# from sqlalchemy.engine import Engine
from sqlmodel import JSON, Column, Field, Session, SQLModel, select
from sqlmodel.sql.expression import Select, SelectOfScalar
from sqlmodel import create_engine

# from sqlalchemy.engine import Engine
from sqlalchemy.future import Engine
import structlog


class MetaTableModel(SQLModel, table=True):
    __tablename__ = "meta_tables"

    table: str = Field(primary_key=True)
    dataset: str
    version: str
    namespace: str
    channel: str
    checksum: str
    dimensions: str
    path: str
    format: str
    table_db_name: str
    is_public: bool


class MetaVariableModel(SQLModel, table=True):
    __tablename__ = "meta_variables"

    # NOTE: Sequence is needed for duckdb integer primary keys
    # variable_id: int = Field(
    #     primary_key=True,
    #     sa_column_args=(
    #         Integer,
    #         Sequence("variable_id_seq"),
    #     ),
    # )
    variable_id: int = Field(primary_key=True)
    short_name: str
    table_path: str
    table_db_name: str
    variable_type: str
    title: str
    description: str
    sources: str
    grapher_meta: str
    unit: str
    short_unit: str
    display: str
    # distinct values of years and entities encoded as JSON
    years_values: str
    entities_values: str


# class MetaTableModel(Base):  # type: ignore
#     __tablename__ = "meta_tables"

#     table = Column(String, primary_key=True)
#     dataset = Column(String)
#     version = Column(String)
#     namespace = Column(String)
#     channel = Column(String)
#     checksum = Column(String)
#     dimensions = Column(String)
#     path = Column(String)
#     format = Column(String)
#     table_db_name = Column(String)
#     is_public = Column(Boolean)


# class MetaVariableModel(Base):  # type: ignore
#     __tablename__ = "meta_variables"

#     # NOTE: Sequence is needed for duckdb integer primary keys
#     variable_id = Column(Integer, Sequence("fakemodel_id_sequence"), primary_key=True)
#     short_name = Column(String)
#     table_path = Column(String)
#     table_db_name = Column(String)
#     variable_type = Column(String)
#     title = Column(String)
#     description = Column(String)
#     sources = Column(String)
#     grapher_meta = Column(String)
#     unit = Column(String)
#     short_unit = Column(String)
#     display = Column(String)
#     # distinct values of years and entities encoded as JSON
#     years_values = Column(String)
#     entities_values = Column(String)


def db_init(path: Path) -> Engine:
    engine = create_engine(f"duckdb:///{path}")
    # Base.metadata.create_all(eng)
    SQLModel.metadata.create_all(engine)
    return engine
