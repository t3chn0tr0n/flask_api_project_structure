from sqlalchemy import (JSON, Boolean, Column, DateTime, Float, Integer,
                        MetaData, String, Table)
from sqlalchemy.ext.declarative import declarative_base

from .helpers import Model
from .sql_ops import Database

Base = declarative_base()

# --- Format ---

# class TableName(Base, Model):
#     __tablename__ = 'table_name'
#     id = Column(Integer, primary_key=True)
#     col_str_unique = Column(String, unique=True)
#     col_str = Column(String)
#     col_int = Column(Integer)
#     col_bool = Column(Boolean, default=True)
#     active = Column(Boolean, default=True) # if this is changed, make sure to change in Model class!

#     def __repr__(self):
#         """
#             Following str is what displayed if we print this class' object
#             Very important for debuging
#         """
#         return f"<TableName(name='{self.name}', col_str_unique='{self.col_str_unique}', col_str='{self.col_str}', ... )>"


class DemoModel(Base, Model):
    __tablename__ = 'table_name'
    # "id" is col name, pk is attribute name
    pk = Column("id", Integer, primary_key=True)
    col_str_unique = Column("", String, unique=True)
    col_str = Column(String)
    col_int = Column(Integer)
    col_bool = Column(Boolean, default=True)
    col_float = Column(Float)
    active = Column("is_active", Boolean, default=True)

    def __repr__(self):
        """
            Following str is what displayed if we print this class' object
        """
        return f"<DemoModel(id_='{self.id}', col_str_unique='{self.col_str_unique}', col_int='{self.col_int}', ... )>"
