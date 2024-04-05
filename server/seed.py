#!/usr/bin/env python3
# server/seed.py

import datetime
from app import app
from models import db, Employee, Review, Onboarding
from faker import Faker
from random import choice as rc

with app.app_context():
    # Delete all rows in tables
    Employee.query.delete()
    Review.query.delete()
    Onboarding.query.delete()

    # faker generator
    fake = Faker()

    # Add employee model instances to database
    employees = []
    onboarding = []
    days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
    months = [1,2,3,4,5,6,7,8,9,10,11,12]

    for n in range(10):
        # Hire employee
        n_employee = Employee(name=fake.first_name(), hire_date = datetime.datetime(2022, rc(months), rc(days)))
        employees.append(n_employee)

        # Onboarding employee
        n_onboarding = Onboarding(orientation=datetime.datetime(2022, rc(months), rc(days)), employee=n_employee)
        onboarding.append(n_onboarding)

    db.session.add_all(employees)
    db.session.add_all(onboarding)
    db.session.commit()

    # Add review model instances to database
    reviews = []
    for n in range(25):
        n_review = Review(year=2023, summary=fake.text(), employee=rc(employees))
        reviews.append(n_review)

    db.session.add_all(reviews)
    db.session.commit()