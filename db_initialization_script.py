from datetime import *
from models.init import *

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

# create clinic items
clinicitem1 = ClinicItem(name='clinicitem1', quantity=20, secretary_id=1)
clinicitem2 = ClinicItem(name='clinicitem2', quantity=40, secretary_id=2)

# add patients to database
patient1 = Patient(first_name='Ahmed', last_name='Maged', birth_date=datetime(1990, 1, 1), phone_number='01122029349', email='a@gmail.com')


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


# Create a new record object
record = Record(date=date.today(), marital_status='Married',
                notes='Patient is feeling much better now')

# Add lab tests to the record
lab_test1 = LabTest(name='Blood test', result='Normal', date=date.today())
lab_test2 = LabTest(name='Urine test', result='Abnormal', date=date.today())
record.lab_tests.append(lab_test1)
record.lab_tests.append(lab_test2)

# Add medications to the record
medication1 = Medication(
    date=date.today(), notes='Take one tablet every 6 hours')
medication2 = Medication(
    date=date.today(), notes='Apply cream to affected area twice daily')
record.medications.append(medication1)
record.medications.append(medication2)

# Add medical histories to the record
medical_history1 = MedicalHistory(
    date=date(2010, 6, 15), notes='Diagnosed with asthma')
medical_history2 = MedicalHistory(
    date=date(2015, 8, 10), notes='Diagnosed with diabetes')
record.medical_histories.append(medical_history1)
record.medical_histories.append(medical_history2)

# Add allergies to the record
allergy1 = Allergy(name='Pollen', allergen='Tree pollen',
                   description='Causes sneezing and itchy eyes')
allergy2 = Allergy(name='Penicillin', allergen='Antibiotic',
                   description='Causes rash and swelling')
record.allergies.append(allergy1)
record.allergies.append(allergy2)

# Add the record to the database
db.session.add(record)
db.session.commit()
