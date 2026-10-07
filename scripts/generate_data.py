import random

from faker import Faker


SEED = 42

random.seed(SEED)
fake = Faker()
Faker.seed(SEED)


def generate_suppliers(count: int = 100) -> list[dict]:
    suppliers = []

    for supplier_id in range(1, count + 1):
        suppliers.append(
            {
                "supplier_id": supplier_id,
                "supplier_name": fake.company(),
                "supplier_category": random.choice(
                    [
                        "IT Services",
                        "Manufacturing",
                        "Facilities",
                        "Logistics",
                        "Professional Services",
                    ]
                ),
                "country": fake.country(),
                "city": fake.city(),
                "rating": round(random.uniform(2.5, 5.0), 2),
                "is_active": random.random() < 0.9,
                "created_at": fake.date_time_between(
                    start_date="-5y",
                    end_date="now",
                ),
            }
        )

    return suppliers


def generate_departments(count: int = 10) -> list[dict]:
    department_names = [
        "Finance",
        "Information Technology",
        "Human Resources",
        "Procurement",
        "Operations",
        "Legal",
        "Marketing",
        "Sales",
        "Engineering",
        "Facilities",
    ]

    departments = []

    for department_id in range(1, count + 1):
        departments.append(
            {
                "department_id": department_id,
                "department_name": department_names[department_id - 1],
                "cost_center": f"CC-{1000 + department_id}",
                "location": random.choice(
                    [
                        "Hyderabad",
                        "Bengaluru",
                        "Mumbai",
                        "Pune",
                        "Chennai",
                    ]
                ),
            }
        )

    return departments


def generate_employees(
    count: int = 500,
    department_count: int = 10,
) -> list[dict]:
    employees = []

    job_titles = [
        "Analyst",
        "Senior Analyst",
        "Manager",
        "Senior Manager",
        "Director",
        "Specialist",
        "Engineer",
    ]

    for employee_id in range(1, count + 1):
        employees.append(
            {
                "employee_id": employee_id,
                "employee_name": fake.name(),
                "department_id": random.randint(1, department_count),
                "job_title": random.choice(job_titles),
                "location": random.choice(
                    [
                        "Hyderabad",
                        "Bengaluru",
                        "Mumbai",
                        "Pune",
                        "Chennai",
                    ]
                ),
            }
        )

    return employees


def generate_products(count: int = 200) -> list[dict]:
    categories = {
        "IT Hardware": [
            "Laptop",
            "Monitor",
            "Keyboard",
            "Mouse",
            "Server",
        ],
        "Office Supplies": [
            "Printer Paper",
            "Notebook",
            "Pen",
            "Desk Organizer",
        ],
        "Software": [
            "Database License",
            "Security License",
            "Analytics License",
            "Cloud License",
        ],
        "Facilities": [
            "Office Chair",
            "Desk",
            "Air Conditioner",
            "Cleaning Supplies",
        ],
    }

    products = []

    category_names = list(categories.keys())

    for product_id in range(1, count + 1):
        category = random.choice(category_names)
        product_type = random.choice(categories[category])

        products.append(
            {
                "product_id": product_id,
                "product_name": f"{product_type} {fake.word().title()}",
                "category": category,
                "unit_of_measure": random.choice(
                    ["Each", "Box", "Pack", "License"]
                ),
                "standard_price": round(
                    random.uniform(25, 5000),
                    2,
                ),
            }
        )

    return products


if __name__ == "__main__":
    suppliers = generate_suppliers()
    departments = generate_departments()
    employees = generate_employees()
    products = generate_products()

    print(f"Generated {len(suppliers)} suppliers")
    print(f"Generated {len(departments)} departments")
    print(f"Generated {len(employees)} employees")
    print(f"Generated {len(products)} products")

    print("\nSample department:")
    print(departments[0])

    print("\nSample employee:")
    print(employees[0])

    print("\nSample product:")
    print(products[0])