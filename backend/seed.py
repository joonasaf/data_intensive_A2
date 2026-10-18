from datetime import date
from app.database import (
    CustomerSessionLocal,
    VehicleSessionLocal,
    ServiceSessionLocal
)

from app.models import (
    Customer,
    Vehicle,
    ServiceRecord
)

def seed_customers():
    database = CustomerSessionLocal()

    try:
        if database.query(Customer).count() > 0:
            print("Customers database already contains data.")
            return

        customers = [
            Customer(
                name="Matti Meikäläinen",
                email="matti@example.com",
                phone="0401234567"
            ),
            Customer(
                name="Anna Virtanen",
                email="anna@example.com",
                phone="0509876543"
            ),
            Customer(
                name="John Smith",
                email="john@example.com",
                phone="0451112233"
            ),
            Customer(
                name="Laura Laine",
                email="laura.laine@example.com",
                phone="0402345678"
            ),
            Customer(
                name="Mikko Korhonen",
                email="mikko.korhonen@example.com",
                phone="0503456789"
            ),
            Customer(
                name="Emma Niemi",
                email="emma.niemi@example.com",
                phone="0444567890"
            ),
            Customer(
                name="Antti Mäkinen",
                email="antti.makinen@example.com",
                phone="0405678901"
            ),
            Customer(
                name="Sofia Lehto",
                email="sofia.lehto@example.com",
                phone="0456789012"
            ),
            Customer(
                name="Daniel Johnson",
                email="daniel.johnson@example.com",
                phone="0507890123"
            ),
            Customer(
                name="Maria Koski",
                email="maria.koski@example.com",
                phone="0448901234"
            )
        ]


        database.add_all(customers)
        database.commit()

        print("Customers added.")

    finally:
        database.close()


def seed_vehicles():
    database = VehicleSessionLocal()

    try:
        if database.query(Vehicle).count() > 0:
            print("Vehicles database already contains data.")
            return

        vehicles = [
            Vehicle(
                registration_number="ABC-123",
                manufacturer="Mercedes-Benz",
                model="C-Class",
                year=2022,
                customer_id=1
            ),
            Vehicle(
                registration_number="XYZ-789",
                manufacturer="Volvo",
                model="XC60",
                year=2023,
                customer_id=2
            ),
            Vehicle(
                registration_number="TEST-01",
                manufacturer="Toyota",
                model="Corolla",
                year=2020,
                customer_id=3
            ),
            Vehicle(
                registration_number="DEF-456",
                manufacturer="BMW",
                model="320i",
                year=2021,
                customer_id=4
            ),
            Vehicle(
                registration_number="GHI-789",
                manufacturer="Audi",
                model="A4",
                year=2022,
                customer_id=5
            ),
            Vehicle(
                registration_number="JKL-321",
                manufacturer="Volkswagen",
                model="Golf",
                year=2019,
                customer_id=6
            ),
            Vehicle(
                registration_number="MNO-654",
                manufacturer="Skoda",
                model="Octavia",
                year=2023,
                customer_id=7
            ),
            Vehicle(
                registration_number="PQR-987",
                manufacturer="Ford",
                model="Focus",
                year=2018,
                customer_id=8
            ),
            Vehicle(
                registration_number="STU-246",
                manufacturer="Tesla",
                model="Model 3",
                year=2024,
                customer_id=9
            ),
            Vehicle(
                registration_number="VWX-135",
                manufacturer="Mercedes-Benz",
                model="E-Class",
                year=2020,
                customer_id=10
            )
        ]


        database.add_all(vehicles)
        database.commit()

        print("Vehicles added.")

    finally:
        database.close()


def seed_services():
    database = ServiceSessionLocal()

    try:
        if database.query(ServiceRecord).count() > 0:
            print("Services database already contains data.")
            return

        services =  [
            ServiceRecord(
                vehicle_id=1,
                service_date=date(2026, 4, 12),
                description="Annual maintenance",
                mileage=45000
            ),
            ServiceRecord(
                vehicle_id=2,
                service_date=date(2026, 5, 20),
                description="Brake inspection",
                mileage=67000
            ),
            ServiceRecord(
                vehicle_id=3,
                service_date=date(2026, 6, 5),
                description="Oil and filter change",
                mileage=82000
            ),
            ServiceRecord(
                vehicle_id=4,
                service_date=date(2026, 2, 15),
                description="Annual maintenance",
                mileage=58000
            ),
            ServiceRecord(
                vehicle_id=5,
                service_date=date(2026, 3, 10),
                description="Engine oil change",
                mileage=41000
            ),
            ServiceRecord(
                vehicle_id=6,
                service_date=date(2026, 1, 28),
                description="Brake pad replacement",
                mileage=96000
            ),
            ServiceRecord(
                vehicle_id=7,
                service_date=date(2026, 7, 3),
                description="Annual maintenance",
                mileage=32000
            ),
            ServiceRecord(
                vehicle_id=8,
                service_date=date(2026, 3, 22),
                description="Battery replacement",
                mileage=105000
            ),
            ServiceRecord(
                vehicle_id=9,
                service_date=date(2026, 8, 17),
                description="Tyre inspection",
                mileage=24000
            ),
            ServiceRecord(
                vehicle_id=10,
                service_date=date(2026, 9, 8),
                description="Annual maintenance",
                mileage=72000
            ),
            ServiceRecord(
                vehicle_id=1,
                service_date=date(2026, 8, 25),
                description="Brake fluid replacement",
                mileage=52000
            ),
            ServiceRecord(
                vehicle_id=2,
                service_date=date(2026, 9, 14),
                description="Oil and filter change",
                mileage=73500
            ),
            ServiceRecord(
                vehicle_id=3,
                service_date=date(2026, 9, 30),
                description="Front brake replacement",
                mileage=89500
            ),
            ServiceRecord(
                vehicle_id=5,
                service_date=date(2026, 10, 6),
                description="Air filter replacement",
                mileage=47500
            ),
            ServiceRecord(
                vehicle_id=7,
                service_date=date(2026, 10, 10),
                description="Winter tyre change",
                mileage=38500
            )
        ]

        database.add_all(services)
        database.commit()

        print("Service records added.")

    finally:
        database.close()


if __name__ == "__main__":
    seed_customers()
    seed_vehicles()
    seed_services()

    print("Dummy data creation completed.")