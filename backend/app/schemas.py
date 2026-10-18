from datetime import date
from pydantic import BaseModel, ConfigDict, Field


# Customer schemas

class CustomerBase(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: str = Field(min_length=1, max_length=150)
    phone: str = Field(min_length=1, max_length=30)

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    pass

class CustomerResponse(CustomerBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


# Vehicle schemas

class VehicleBase(BaseModel):
    registration_number: str = Field(min_length=1, max_length=20)
    manufacturer: str = Field(min_length=1, max_length=100)
    model: str = Field(min_length=1, max_length=100)
    year: int = Field(ge=1886, le=2100)
    customer_id: int = Field(gt=0)

class VehicleCreate(VehicleBase):
    pass

class VehicleUpdate(VehicleBase):
    pass

class VehicleResponse(VehicleBase):
    model_config = ConfigDict(from_attributes=True)

    id:int


# Service schemas

class ServiceBase(BaseModel):
    vehicle_id: int = Field(gt=0)
    service_date: date
    description: str = Field(min_length=1, max_length=250)
    mileage: int = Field(ge=0)

class ServiceCreate(ServiceBase):
    pass

class ServiceUpdate(ServiceBase):
    pass

class ServiceResponse(ServiceBase):
    model_config = ConfigDict(from_attributes=True)

    id: int