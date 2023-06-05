from datetime import *
from models.init import *

print('starting db initialization script')

# drop all of the existing database tables
db.drop_all()

# create the database and the database table
db.create_all()

# create user types
doctoruser = UserType(name='doctor')
secretaryuser = UserType(name='secretary')
dumyuser = UserType(name='dumy')

# insert user types
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
clinicitem1 = ClinicItem(
    name='clinicitem1', quantity=20, secretary_id=1, price=10)
clinicitem2 = ClinicItem(
    name='clinicitem2', quantity=40, secretary_id=2, price=20)

# add patients to database
patient1 = Patient(first_name='Ahmed', last_name='Maged', birth_date=datetime(
    1990, 1, 1), phone_number='01122029349', email='a@gmail.com')


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
# add appointments to database
a = Appointment(patient_id=1,
                doctor_id=3,
                secretary_id=6,
                start_time=datetime(1985, 1, 1),
                notes="patrikos"
                )

a.insert()
# add secretaries to database
secretary1.insert()
secretary2.insert()

# add clinic items to database
clinicitem1.insert()
clinicitem2.insert()

# add patients to database
patient1.insert()


# Create a new record object
record = Record(date=date.today(), marital_status='Married', patient_profile_id=patient1.id,
                notes='Patient is feeling much better now')

# Add the record to the database
record.insert()

# Create purchase object
purchase1 = Purchase(patient_id=patient1.id, secretary_id=secretary1.id)

# Add the purchase to the database
purchase1.insert()

# Create purchasedetails object
purchasedetail1 = PurchaseDetail(
    clinic_item_id=clinicitem1.id, purchase_id=purchase1.id, quantity=5)
purchasedetail2 = PurchaseDetail(
    clinic_item_id=clinicitem2.id, purchase_id=purchase1.id, quantity=10)

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
peterEntity = ReportEntity(name="peter")

# add report entites to database
AllergyEntity.insert()
MedicationsEntity.insert()
MedicalHistoryEntity.insert()
LabTesTsEntity.insert()
peterEntity.insert()

# create report attributes
NameAttribute = ReportAttribute(name='Name', type='text')
DateAttribute = ReportAttribute(name='Date', type='date')
NotesAttribute = ReportAttribute(name='Notes', type='text')
ResultAttribute = ReportAttribute(name='Result', type='text')
AllergenAttribute = ReportAttribute(name='Allergen', type='text')
DescriptionAttribute = ReportAttribute(name='Description', type='text')
peterAttrb = ReportAttribute(name='peterattt', type='text')

# add report attributes to database
NameAttribute.insert()
DateAttribute.insert()
NotesAttribute.insert()
ResultAttribute.insert()
AllergenAttribute.insert()
DescriptionAttribute.insert()
peterAttrb.insert()

# create entity attributes
AllergyEntity.attributes.append(NameAttribute)
AllergyEntity.attributes.append(AllergenAttribute)
AllergyEntity.attributes.append(DescriptionAttribute)

MedicationsEntity.attributes.append(NameAttribute)
MedicationsEntity.attributes.append(DateAttribute)

MedicalHistoryEntity.attributes.append(NameAttribute)
MedicalHistoryEntity.attributes.append(DateAttribute)
MedicalHistoryEntity.attributes.append(NotesAttribute)

LabTesTsEntity.attributes.append(NameAttribute)
LabTesTsEntity.attributes.append(DateAttribute)
LabTesTsEntity.attributes.append(ResultAttribute)

peterEntity.attributes.append(peterAttrb)
peterEntity.attributes.append(NotesAttribute)


# create report
allergyreport1 = Report(record_id=record.id, report_entity_id=AllergyEntity.id)
allergyreport2 = Report(record_id=record.id, report_entity_id=AllergyEntity.id)
medicationsreport1 = Report(
    record_id=record.id, report_entity_id=MedicationsEntity.id)
'''
medicalhistoryreport1 = Report(record_id = record.id, report_entity_id = MedicalHistoryEntity.id)
labtestsreport1 = Report(record_id = record.id, report_entity_id = LabTesTsEntity.id)
labtestsreport2 = Report(record_id = record.id, report_entity_id = LabTesTsEntity.id)
'''

# add reports to database
allergyreport1.insert()
allergyreport2.insert()
medicationsreport1.insert()
'''
medicalhistoryreport1.insert()
labtestsreport1.insert()
labtestsreport2.insert()
'''

# create report values
allergyreport1_value1 = ReportValue(
    report_id=allergyreport1.id, report_entity_id=AllergyEntity.id, report_attribute_id=NameAttribute.id, value='Pollen')
allergyreport1_value2 = ReportValue(report_id=allergyreport1.id, report_entity_id=AllergyEntity.id,
                                    report_attribute_id=AllergenAttribute.id, value='Tree pollen')
allergyreport1_value3 = ReportValue(report_id=allergyreport1.id, report_entity_id=AllergyEntity.id,
                                    report_attribute_id=DescriptionAttribute.id, value='Causes sneezing and itchy eyes')

allergyreport2_value1 = ReportValue(report_id=allergyreport2.id, report_entity_id=AllergyEntity.id,
                                    report_attribute_id=NameAttribute.id, value='Penicillin')
allergyreport2_value2 = ReportValue(report_id=allergyreport2.id, report_entity_id=AllergyEntity.id,
                                    report_attribute_id=AllergenAttribute.id, value='Antibiotic')
allergyreport2_value3 = ReportValue(report_id=allergyreport2.id, report_entity_id=AllergyEntity.id,
                                    report_attribute_id=DescriptionAttribute.id, value='Causes rash and swelling')

medicationsreport1_value1 = ReportValue(
    report_id=medicationsreport1.id, report_entity_id=MedicationsEntity.id, report_attribute_id=NameAttribute.id, value='Paracetamol')
medicationsreport1_value2 = ReportValue(
    report_id=medicationsreport1.id, report_entity_id=MedicationsEntity.id, report_attribute_id=DateAttribute.id, value='2020-01-01')

# add report values to database
allergyreport1_value1.insert()
allergyreport1_value2.insert()
allergyreport1_value3.insert()
allergyreport2_value1.insert()
allergyreport2_value2.insert()
allergyreport2_value3.insert()
medicationsreport1_value1.insert()
medicationsreport1_value2.insert()
