from datetime import *
from models.init import *

print ('starting db initialization script')

# drop all of the existing database tables
db.drop_all()

# create the database and the database table
db.create_all()

#create user types
doctoruser = UserType(name='doctor')
secretaryuser = UserType(name='secretary')
dumyuser = UserType(name='dumy')

#insert user types
doctoruser.insert()
secretaryuser.insert()
dumyuser.insert()

# create links 
link1 = Link(name='link1', url='https://www.google.com')
link2 = Link(name='link2', url='https://www.facebook.com')
link3 = Link(name='link3', url='https://www.twitter.com')

# add links to database
link1.insert()
link2.insert()
link3.insert()

# add links to user types
doctoruser.linking.append(link1)
doctoruser.linking.append(link2)
secretaryuser.linking.append(link3)
db.session.commit()

# test if links are added to user types
print(doctoruser.linking)
print(secretaryuser.linking)
print(link1.user_types)
print(link2.user_types)
print(link3.user_types)



# create dumy users
user1 = User(username='johndoe', password='password', email='johndoe@example.com', usertypeid=dumyuser.id,
            first_name='John', last_name='Doe', birth_date=datetime(1990, 1, 1), phone_number='123-456-7890', role='doctor')

user2 = User(username='komsry', password='password1258', email='komsry@example.com', usertypeid=dumyuser.id,
            first_name='Jane', last_name='Doe', birth_date=datetime(1995, 1, 1), phone_number='123-456-7890', role='secretary')


# create doctors
doctor1 = Doctor(username='doctor1', password='password', email='doctor1@example.com', usertypeid=doctoruser.id,
                first_name='Doctor', last_name='One', birth_date=datetime(1980, 1, 1), phone_number='123-456-7890', specialization='General Medicine')

doctor2 = Doctor(username='doctor2', password='password', email='doctor2@example.com', usertypeid=doctoruser.id,
                first_name='Docor', last_name='Two', birth_date=datetime(1985, 1, 1), phone_number='123-456-7890', specialization='Pediatrics')

# create secretaries
secretary1 = Secretary(username='secretary1', password='password', email='secretary1@example.com', usertypeid=secretaryuser.id,
                    first_name='Secretary', last_name='One', birth_date=datetime(1990, 1, 1), phone_number='123-456-7890')

secretary2 = Secretary(username='secretary2', password='password', email='secretary2@example.com', usertypeid=secretaryuser.id,
                    first_name='Secretary', last_name='Two', birth_date=datetime(1995, 1, 1), phone_number='123-456-7890')

# create clinic items
clinicitem1 = ClinicItem(name='clinicitem1', quantity=20, secretary_id=1)
clinicitem2 = ClinicItem(name='clinicitem2', quantity=40, secretary_id=2)

# add patients to database
patient1 = Patient(first_name='Ahmed', last_name='Maged', birth_date=datetime(1990, 1, 1), phone_number='01122029349', email='ahmed@gmail.com')


# add users to database
user1.insert()
user2.insert()

# add doctors to database
doctor1.insert()
doctor2.insert()

# add secretaries to database
secretary1.insert()
secretary2.insert()

# add clinic items to database
clinicitem1.insert()
clinicitem2.insert()

#add patients to database
patient1.insert()