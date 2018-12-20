from __future__ import print_function
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
django.setup()
import sys
from m2m_app.models import Publication, Article
from faker import Faker
import random
import time


fake = Faker()
fake.seed(1)


def seed_Publications(num_entries=10, overwrite=True):

    if overwrite:
        print("Overwriting Fake Publications")
        Publication.objects.all().delete()

    count = 0
    for _ in range(num_entries):
        fake_title = fake.paragraph(nb_sentences=1, variable_nb_sentences=True, ext_word_list=None)
        pub = Publication.objects.create(title=fake_title)
        pub.save()

        count += 1
        percentage_complete = count / num_entries * 100
        print("Adding {} new Publications: {:.2f}%".format(num_entries, percentage_complete), end='\r')
        sys.stdout.flush()

    print()


def seed_Articles(num_entries=10, overwrite=True):

    if overwrite:
        print("Overwriting Fake Articles")
        Article.objects.all().delete()

    count = 0
    for _ in range(num_entries):
        fake_headline = fake.sentence(nb_words=5, variable_nb_words=True, ext_word_list=None)
        p = list(Publication.objects.all())
        art = Article.objects.create(headline=fake_headline)
        art.publications.add(random.choice(p))

        art.save()

        count += 1
        percentage_complete = count / num_entries * 100
        print("Adding {} new Articles: {:.2f}%".format(num_entries, percentage_complete), end='\r')
        sys.stdout.flush()

    print()


def seed_all():

    start_time = time.time()
    seed_Publications(num_entries=1, overwrite=True)
    seed_Articles(num_entries=1, overwrite=True)

    elapsed_time = time.time() - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    print("Script Execution took: {} minutes {} seconds".format(minutes, seconds))


seed_all()
print("Data populated successfully")
