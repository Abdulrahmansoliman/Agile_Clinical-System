from datetime import *
from models import *

print ('starting db initialization script')
# create users
user1 = User(username='johndoe', password='password', email='johndoe@example.com',
            first_name='John', last_name='Doe', birth_date=datetime(1990, 1, 1), phone_number='123-456-7890', role='doctor')

user2 = User(username='komsry', password='password1258', email='komsry@example.com',
            first_name='Jane', last_name='Doe', birth_date=datetime(1995, 1, 1), phone_number='123-456-7890', role='secretary')

# create doctors
doctor1 = Doctor(username='doctor1', password='password', email='doctor1@example.com',
                first_name='Doctor', last_name='One', birth_date=datetime(1980, 1, 1), phone_number='123-456-7890', specialization='General Medicine')

doctor2 = Doctor(username='doctor2', password='password', email='doctor2@example.com',
                first_name='Docor', last_name='Two', birth_date=datetime(1985, 1, 1), phone_number='123-456-7890', specialization='Pediatrics')

# create secretaries
secretary1 = Secretary(username='secretary1', password='password', email='secretary1@example.com',
                    first_name='Secretary', last_name='One', birth_date=datetime(1990, 1, 1), phone_number='123-456-7890')

secretary2 = Secretary(username='secretary2', password='password', email='secretary2@example.com',
                    first_name='Secretary', last_name='Two', birth_date=datetime(1995, 1, 1), phone_number='123-456-7890')

# add users to database
user1.insert()
user2.insert()

# add doctors to database
doctor1.insert()
doctor2.insert()

# add secretaries to database
secretary1.insert()
secretary2.insert()
