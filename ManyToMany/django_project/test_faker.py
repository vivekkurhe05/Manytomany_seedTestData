from __future__ import print_function
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
django.setup()
from faker import Faker


fake = Faker()
fake.seed(0000)

print("City ->", fake.city())
print("Address ->", fake.address())
print("Zipcode ->", fake.zipcode_plus4())
print("Street name ->", fake.street_name())
print("country ->", fake.country())

