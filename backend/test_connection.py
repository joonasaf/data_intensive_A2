from sqlalchemy import text

from app.database import(
    customer_engine,
    vehicle_engine,
    service_engine
)

databases = {
    "customers_db": customer_engine,
    "vehicles_db": vehicle_engine,
    "services_db": service_engine
}

for database_name, engine in databases.items():
    try:
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT current_database();")
            )

            current_database = result.scalar()

            print(
                f"Connection successful: {current_database}"
            )
    except Exception as error:
        print(
            f"Connection failed for {database_name}: {error}"
        )
    