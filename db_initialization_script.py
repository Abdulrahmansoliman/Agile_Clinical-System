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

'''
# test if links are added to user types
print(doctoruser.linking)
print(secretaryuser.linking)
print(link1.user_types)
print(link2.user_types)
print(link3.user_types)
'''


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
clinicitem1 = ClinicItem(name='clinicitem1', quantity=20, secretary_id=1, price=10)
clinicitem2 = ClinicItem(name='clinicitem2', quantity=40, secretary_id=2, price=20)

# add patients to database
patient1 = Patient(first_name='Ahmed', last_name='Maged', birth_date=datetime(1990, 1, 1), phone_number='01122029349', email='a@gmail.com')


# add users to database
user1.insert()
user2.insert()

# add doctors to database
doctor1.insert()
doctor2.insert()

'''
print(doctor1.created_at)

delay = timedelta(days=1)
doctor1.updated_at = doctor1.updated_at + delay
print(doctor1.updated_at)
doctor1.update()
print(doctor1.updated_at)
doctor1.delete()
print(doctor1.deleted_at)

doctor1.insert()
'''
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

# Create purchase object
purchase1 = Purchase(patient_id = patient1.id, secretary_id= secretary1.id)

# Add the purchase to the database
purchase1.insert()

# Create purchasedetails object
purchasedetail1 = PurchaseDetail(clinic_item_id = clinicitem1.id, purchase_id = purchase1.id, quantity = 5)
purchasedetail2 = PurchaseDetail(clinic_item_id = clinicitem2.id, purchase_id = purchase1.id, quantity = 10)

# Add the purchasedetails to the database
purchasedetail1.insert()
purchasedetail2.insert()

# test if purchase is added to patient
'''
print('purchase1:')
print(purchase1.format())
print('purchase1 with items:')
print(purchase1.format_with_items())
print('purchasedetail1:')
print(purchasedetail1.format())
print('purchasedetail2:')
print(purchasedetail2.format())
'''

# create report entites
AllergyEntity = ReportEntity(name='Allergy')
MedicationsEntity = ReportEntity(name='Medications')
MedicalHistoryEntity = ReportEntity(name='Medical History')
LabTesTsEntity = ReportEntity(name='Lab Tests')

# add report entites to database
AllergyEntity.insert()
MedicationsEntity.insert()
MedicalHistoryEntity.insert()
LabTesTsEntity.insert()

# create report attributes
NameAttribute = ReportAttribute(name='Name', type='string')
DateAttribute = ReportAttribute(name='Date', type='date')
NotesAttribute = ReportAttribute(name='Notes', type='string')
ResultAttribute = ReportAttribute(name='Result', type='string')
AllergenAttribute = ReportAttribute(name='Allergen', type='string')
DescriptionAttribute = ReportAttribute(name='Description', type='string')

# add report attributes to database
NameAttribute.insert()
DateAttribute.insert()
NotesAttribute.insert()
ResultAttribute.insert()
AllergenAttribute.insert()
DescriptionAttribute.insert()


# create entity attributes
AllergyEntityAttribute1 = EntityAttribute(report_entity_id=AllergyEntity.id, report_attribute_id=NameAttribute.id)
AllergyEntityAttribute2 = EntityAttribute(report_entity_id=AllergyEntity.id, report_attribute_id=AllergenAttribute.id)
AllergyEntityAttribute3 = EntityAttribute(report_entity_id=AllergyEntity.id, report_attribute_id=DescriptionAttribute.id)

MedicationsEntityAttribute2 = EntityAttribute(report_entity_id=MedicationsEntity.id, report_attribute_id=DateAttribute.id)
MedicationsEntityAttribute3 = EntityAttribute(report_entity_id=MedicationsEntity.id, report_attribute_id=NotesAttribute.id)

MedicalHistoryEntityAttribute2 = EntityAttribute(report_entity_id=MedicalHistoryEntity.id, report_attribute_id=DateAttribute.id)
MedicalHistoryEntityAttribute3 = EntityAttribute(report_entity_id=MedicalHistoryEntity.id, report_attribute_id=NotesAttribute.id)

LabTesTsEntityAttribute1 = EntityAttribute(report_entity_id=LabTesTsEntity.id, report_attribute_id=NameAttribute.id)
LabTesTsEntityAttribute2 = EntityAttribute(report_entity_id=LabTesTsEntity.id, report_attribute_id=DateAttribute.id)
LabTesTsEntityAttribute3 = EntityAttribute(report_entity_id=LabTesTsEntity.id, report_attribute_id=ResultAttribute.id)

# add entity attributes to database
AllergyEntityAttribute1.insert()
AllergyEntityAttribute2.insert()
AllergyEntityAttribute3.insert()

MedicationsEntityAttribute2.insert()
MedicationsEntityAttribute3.insert()

MedicalHistoryEntityAttribute2.insert()
MedicalHistoryEntityAttribute3.insert()

LabTesTsEntityAttribute1.insert()
LabTesTsEntityAttribute2.insert()
LabTesTsEntityAttribute3.insert()

# test if entity attributes are added to entities by printing each entity with its attributes
print('AllergyEntity:')
print(AllergyEntity.get_attributes())
print('MedicationsEntity:')
print(MedicationsEntity.get_attributes())
print('MedicalHistoryEntity:')
print(MedicalHistoryEntity.get_attributes())
print('LabTesTsEntity:')
print(LabTesTsEntity.get_attributes())
print(AllergyEntity.format_with_attributes())

