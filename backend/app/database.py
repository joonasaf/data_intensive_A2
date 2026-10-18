from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file = ".env",
        extra = "ignore"
    )

    customers_database_url: str
    vehicles_database_url: str
    services_database_url: str

settings = Settings()

customer_engine = create_engine (
    settings.customers_database_url,
    pool_pre_ping=True
)

vehicle_engine = create_engine (
    settings.vehicles_database_url,
    pool_pre_ping=True
)

service_engine = create_engine(
    settings.services_database_url,
    pool_pre_ping=True
)

class CustomerBase(DeclarativeBase):
    pass

class VehicleBase(DeclarativeBase):
    pass

class ServiceBase(DeclarativeBase):
    pass


CustomerSessionLocal = sessionmaker(
    bind=customer_engine,
    autoflush=False,
    autocommit=False
)

VehicleSessionLocal = sessionmaker(
    bind=vehicle_engine,
    autoflush=False,
    autocommit=False
)

ServiceSessionLocal = sessionmaker(
    bind=service_engine,
    autoflush=False,
    autocommit=False
)

def get_customer_db():
    database = CustomerSessionLocal()

    try:
        yield database
    finally:
        database.close()

def get_vehicle_db():
    database = VehicleSessionLocal()

    try:
        yield database
    finally:
        database.close()

def get_service_db():
    database = ServiceSessionLocal()

    try:
        yield database
    finally:
        database.close()

