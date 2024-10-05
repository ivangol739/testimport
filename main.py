from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime


def get_data():
	print(f"Дата: {datetime.now()}")


if __name__ == "__main__":
	calculate_salary()
	get_employees()
	get_data()
