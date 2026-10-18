from datetime import date
from sqlalchemy import Date, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import (
    CustomerBase,
    ServiceBase,
    VehicleBase
)


class Customer(CustomerBase):
    __tablename__= "customers"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
        unique=True
    )

    phone: Mapped[str] = mapped_column(
        String(30),
        nullable=False
    )

class Vehicle(VehicleBase):
    __tablename__ = "vehicles"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    registration_number: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        unique=True
    )

    manufacturer: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    model: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    year: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    customer_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

class ServiceRecord(ServiceBase):
    __tablename__ = "service_records"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    vehicle_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    service_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        String(250),
        nullable=False
    )


    mileage: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )