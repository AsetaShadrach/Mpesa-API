from distutils.command.config import config
from django_seed import Seed
from apps.entities.models import Transaction,User,Application
from decouple import config

DEBUG = config('DEBUG')
if DEBUG:
    seeder = Seed.seeder()
    seeder.add_entity(User, 10)
    seeder.add_entity(Application, 5)
    seeder.add_entity(Transaction, 10)

    inserted_pks = seeder.execute()
else:
    print(f"Cannot Run Seeder when DEBUG = {DEBUG}")