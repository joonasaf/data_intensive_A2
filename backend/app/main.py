from fastapi import (
    Depends,
    FastAPI,
    HTTPException,
    status
)

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import (
    get_customer_db,
    get_service_db,
    get_vehicle_db
)


app = FastAPI(
    title="Multi-Database Management API",
    version="1.0.0"
)

@app.get("/api/health")
def health_check():
    return{
        "status": "ok"
    }

############
#### Customer ####
############


@app.get("/api/customers", response_model=list[schemas.CustomerResponse])
def get_customers(
    database: Session = Depends(get_customer_db)
):
    customers = (
        database
        .query(models.Customer)
        .order_by(models.Customer.id)
        .all()
    )

    return customers

@app.post("/api/customers",response_model=schemas.CustomerResponse, status_code=status.HTTP_201_CREATED)
def create_customer(
    customer_data: schemas.CustomerCreate, 
    database: Session = Depends(get_customer_db)
):
    customer = models.Customer(
        **customer_data.model_dump()
    )

    try:
        database.add(customer)
        database.commit()
        database.refresh(customer)

        return customer

    except IntegrityError:
        database.rollback()

        raise HTTPException(
            status_code=409,
            detail="A customer with this email already exists."
        )

@app.put("/api/customers/{customer_id}", response_model=schemas.CustomerResponse)
def update_customer(
    customer_id: int,
    customer_data: schemas.CustomerUpdate,
    database: Session = Depends(get_customer_db)
):
    customer = database.get(
        models.Customer,
        customer_id
    )

    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found."
        )

    for field, value in customer_data.model_dump().items():
        setattr(
            customer,
            field,
            value
        )

    try:
        database.commit()
        database.refresh(customer)

        return customer

    except IntegrityError:
        database.rollback()

        raise HTTPException(
            status_code=409,
            detail="A customer with this email already exists."
        )

@app.delete("/api/customers/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer(
    customer_id: int,
    database: Session = Depends(get_customer_db)
):
    customer = database.get(
        models.Customer,
        customer_id
    )

    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found."
        )

    database.delete(customer)
    database.commit()


############
#### Vehicle ####
############



@app.get("/api/vehicles", response_model=list[schemas.VehicleResponse])
def get_vehicles(
    database: Session = Depends(get_vehicle_db)
):
    vehicles = (
        database
        .query(models.Vehicle)
        .order_by(models.Vehicle.id)
        .all()
    )

    return vehicles

@app.post("/api/vehicles",response_model=schemas.VehicleResponse, status_code=status.HTTP_201_CREATED)
def create_vehicle(
    vehicle_data: schemas.VehicleCreate, 
    database: Session = Depends(get_vehicle_db)
):
    vehicle = models.Vehicle(
        **vehicle_data.model_dump()
    )

    try:
        database.add(vehicle)
        database.commit()
        database.refresh(vehicle)

        return vehicle

    except IntegrityError:
        database.rollback()

        raise HTTPException(
            status_code=409,
            detail=("A vehicle with this registration "
                    "number already exists."
            )
        )

@app.put("/api/vehicles/{vehicle_id}", response_model=schemas.VehicleResponse)
def update_vehicle(
    vehicle_id: int,
    vehicle_data: schemas.VehicleUpdate,
    database: Session = Depends(get_vehicle_db)
):
    vehicle = database.get(
        models.Vehicle,
        vehicle_id
    )

    if vehicle is None:
        raise HTTPException(
            status_code=404,
            detail="Vehicle not found."
        )

    for field, value in vehicle_data.model_dump().items():
        setattr(
            vehicle,
            field,
            value
        )

    try:
        database.commit()
        database.refresh(vehicle)

        return vehicle

    except IntegrityError:
        database.rollback()

        raise HTTPException(
            status_code=409,
            detail=("A vehicle with this registration "
                    "number already exists."
            )
        )


@app.delete("/api/vehicles/{vehicle_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vehicle(
    vehicle_id: int,
    database: Session = Depends(get_vehicle_db)
):
    vehicle = database.get(
        models.Vehicle,
        vehicle_id
    )

    if vehicle is None:
        raise HTTPException(
            status_code=404,
            detail="Vehicle not found."
        )

    database.delete(vehicle)
    database.commit()


############
#### Service ####
############


@app.get("/api/services", response_model=list[schemas.ServiceResponse])
def get_services(
    database: Session = Depends(get_service_db)
):
    services = (
        database
        .query(models.ServiceRecord)
        .order_by(models.ServiceRecord.id)
        .all()
    )

    return services

@app.post("/api/services",response_model=schemas.ServiceResponse, status_code=status.HTTP_201_CREATED)
def create_service(
    services_data: schemas.ServiceCreate, 
    database: Session = Depends(get_service_db)
):
    services = models.ServiceRecord(
        **services_data.model_dump()
    )


    database.add(services)
    database.commit()
    database.refresh(services)

    return services


@app.put("/api/services/{service_id}", response_model=schemas.ServiceResponse)
def update_service(
    service_id: int,
    service_data: schemas.ServiceUpdate,
    database: Session = Depends(get_service_db)
):
    service = database.get(
        models.ServiceRecord,
        service_id
    )

    if service is None:
        raise HTTPException(
            status_code=404,
            detail="Service record not found."
        )

    for field, value in service_data.model_dump().items():
        setattr(
            service,
            field,
            value
        )

    database.commit()
    database.refresh(service)

    return service



@app.delete("/api/services/{service_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_service(
    service_id: int,
    database: Session = Depends(get_service_db)
):
    service = database.get(
        models.ServiceRecord,
        service_id
    )

    if service is None:
        raise HTTPException(
            status_code=404,
            detail="Service Record not found."
        )

    database.delete(service)
    database.commit()