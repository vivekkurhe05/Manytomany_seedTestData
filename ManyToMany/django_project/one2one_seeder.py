from __future__ import print_function
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
django.setup()
import sys
from one2one_app.models import Place, Restaurant, Waiter
from faker import Faker
import random
import time


fake = Faker()
fake.seed(2)


def seed_Places(num_entries=10, overwrite=True):

    if overwrite:
        print("Overwriting Fake Places")
        Place.objects.all().delete()

    count = 0
    for _ in range(num_entries):
        fake_name = fake.first_name_male()
        fake_address = fake.address()

        place = Place.objects.create(
            name=fake_name,
            address=fake_address
        )
        place.save()
        count += 1
        percentage_complete = count / num_entries * 100
        print("Adding {} new Places: {:.2f}%".format(num_entries, percentage_complete), end='\r')
        sys.stdout.flush()

    print()


def seed_Restaurants(num_entries=10, overwrite=True):

    if overwrite:
        print("Overwriting Fake Restaurants")
        Restaurant.objects.all().delete()

    count = 0
    for _ in range(num_entries):

        fake_hot_dogs = fake.boolean(chance_of_getting_true=50)
        fake_pizzas = fake.boolean(chance_of_getting_true=50)
        places = list(Place.objects.all())

        rest = Restaurant.objects.create(
            place=places[_],
            serves_hot_dogs=fake_hot_dogs,
            serves_pizzas=fake_pizzas
        )

        rest.save()
        count += 1
        percentage_complete = count / num_entries * 100
        print("Adding {} new Restaurants: {:.2f}%".format(num_entries, percentage_complete), end='\r')
        sys.stdout.flush()

    print()


def seed_Waiters(num_entries=10, overwrite=True):

    if overwrite:
        print("Overwriting Fake Waiters")
        Waiter.objects.all().delete()

    count = 0
    for _ in range(num_entries):
        fake_waiter_name = fake.first_name_male()
        res = list(Restaurant.objects.all())

        wait = Waiter.objects.create(
            restaurant=random.choice(res),
            name=fake_waiter_name
        )
        wait.save()

        count += 1
        percentage_complete = count / num_entries * 100
        print("Adding {} new Waiters: {:.2f}%".format(num_entries, percentage_complete), end='\r')
        sys.stdout.flush()

    print()


def seed_all():

    start_time = time.time()
    seed_Places(num_entries=10, overwrite=True)
    seed_Restaurants(num_entries=10, overwrite=True)
    seed_Waiters(num_entries=10, overwrite=True)

    elapsed_time = time.time() - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    print("Script Execution took: {} minutes {} seconds".format(minutes, seconds))


seed_all()
print("Data populated successfully.")
