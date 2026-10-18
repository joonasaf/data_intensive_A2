from app.database import (
    CustomerBase,
    VehicleBase,
    ServiceBase,
    customer_engine,
    vehicle_engine,
    service_engine
)

from app import models

print("Creating customer table...")
CustomerBase.metadata.create_all(
    bind=customer_engine
)

print("Creating vehicle table...")
VehicleBase.metadata.create_all(
    bind=vehicle_engine
)

print("Creating service table...")
ServiceBase.metadata.create_all(
    bind=service_engine
)

print("All tables created successfully.")