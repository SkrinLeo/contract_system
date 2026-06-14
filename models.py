from sqlalchemy import Column, Integer, String, Float
from database import Base

from pydantic import BaseModel

# SQLAlchemy модель для БД
class Contract(Base):
    __tablename__ = "contracts"

    id = Column(Integer, primary_key=True, index=True)

    number = Column(String, unique=True, index=True)

    title = Column(String)

    contractor = Column(String)

    amount = Column(Float)

    status = Column(String)

    created_at = Column(String)

    end_date = Column(String)

# Pydantic модель для FastAPI
class ContractCreate(BaseModel):
    number: str
    title: str
    contractor: str
    amount: float
    status: str
    created_at: str
    end_date: str

