import requests
from faker import Faker
from random import randint, choice
from datetime import date, timedelta

BASE_URL = "http://127.0.0.1:8000"

def add_student(name_srn, gpa, age, entry_year, gender):
    url = f"{BASE_URL}/add_student"
    params = {
        "name_srn_": name_srn,
        "gpa_": gpa if gpa is not None else 0.0,
        "age_": age,
        "entry_year_": entry_year,
        "gender_": gender
    }
    response = requests.post(url, params=params)
    try:
        json_response = response.json()
        if response.status_code == 200:
            print(f"Student Added")
        else:
            print(f"Failed to add student. Status code: {response.status_code}")
            print(f"Response content: {json_response}")
    except ValueError:
        print(f"Failed to parse response as JSON. Status code: {response.status_code}")
        print(f"Response content: {response.text}")

if __name__ == "__main__":
    fake = Faker()

    for _ in range(10):
        add_student(
            name_srn=fake.name(),
            gpa=randint(1, 100) / 10.0 if randint(0, 1) else None,
            age=randint(18, 30),
            entry_year=randint(2010, 2023),
            gender=choice(["Male", "Female"])
        )

# Add Faculty

def add_faculty(name, decan, capacity):
    url = f"{BASE_URL}/add_faculty"
    params = {
        "name_": name,
        "decan_": decan,
        "capacity_": capacity
    }

    response = requests.post(url, params=params)
    try:
        json_response = response.json()
        if response.status_code == 200:
            print(f"Faculty Added")
        else:
            print(f"Failed to add faculty. Status code: {response.status_code}")
            print(f"Response content: {json_response}")
    except ValueError:
        print(f"Failed to parse response as JSON. Status code: {response.status_code}")
        print(f"Response content: {response.text}")

if __name__ == "__main__":
    fake = Faker()

    for _ in range(100):
        add_faculty(
            name=fake.job(),
            decan=fake.name(),
            capacity=randint(100, 1000)
        )


