from pathlib import Path

from sqlalchemy import Boolean, Column, Integer, Sequence, String, create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class MetaTableModel(Base):  # type: ignore
    __tablename__ = "meta_tables"

    table = Column(String, primary_key=True)
    dataset = Column(String)
    version = Column(String)
    namespace = Column(String)
    channel = Column(String)
    checksum = Column(String)
    dimensions = Column(String)
    path = Column(String)
    format = Column(String)
    table_db_name = Column(String)
    is_public = Column(Boolean)


class MetaVariableModel(Base):  # type: ignore
    __tablename__ = "meta_variables"

    # NOTE: Sequence is needed for duckdb integer primary keys
    variable_id = Column(Integer, Sequence("fakemodel_id_sequence"), primary_key=True)
    short_name = Column(String)
    table_path = Column(String)
    table_db_name = Column(String)
    variable_type = Column(String)
    title = Column(String)
    description = Column(String)
    sources = Column(String)
    grapher_meta = Column(String)
    unit = Column(String)
    short_unit = Column(String)
    # distinct values of years and entities encoded as JSON
    years_values = Column(String)
    entities_values = Column(String)


def db_init(path: Path) -> Engine:
    eng = create_engine(f"duckdb:///{path}")
    Base.metadata.create_all(eng)
    return eng