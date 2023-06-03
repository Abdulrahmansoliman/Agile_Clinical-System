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
# add appointments to database
a = Appointment(patient_id= 1,
    doctor_id= 3,
    secretary_id= 6,
                start_time=datetime(1985, 1, 1),
    notes= "patrikos"
)

a.insert()
# add secretaries to database
secretary1.insert()
secretary2.insert()

# add clinic items to database
clinicitem1.insert()
clinicitem2.insert()

#add patients to database
patient1.insert()


# Create a new record object
record = Record(date=date.today(), marital_status='Married', patient_profile_id=patient1.id,
                notes='Patient is feeling much better now')

# Add the record to the database
record.insert()

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


# create report
allergyreport1 = Report(record_id = record.id, report_entity_id = AllergyEntity.id)
allergyreport2 = Report(record_id = record.id, report_entity_id = AllergyEntity.id)
medicationsreport1 = Report(record_id = record.id, report_entity_id = MedicationsEntity.id)
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
allergyreport1_value1 = ReportValue(report_id = allergyreport1.id, report_entity_id = AllergyEntity.id, report_attribute_id = NameAttribute.id, value = 'Pollen')
allergyreport1_value2 = ReportValue(report_id = allergyreport1.id, report_entity_id = AllergyEntity.id, report_attribute_id = AllergenAttribute.id, value = 'Tree pollen')
allergyreport1_value3 = ReportValue(report_id = allergyreport1.id, report_entity_id = AllergyEntity.id, report_attribute_id = DescriptionAttribute.id, value = 'Causes sneezing and itchy eyes')

allergyreport2_value1 = ReportValue(report_id = allergyreport2.id, report_entity_id = AllergyEntity.id, report_attribute_id = NameAttribute.id, value = 'Penicillin')
allergyreport2_value2 = ReportValue(report_id = allergyreport2.id, report_entity_id = AllergyEntity.id, report_attribute_id = AllergenAttribute.id, value = 'Antibiotic')
allergyreport2_value3 = ReportValue(report_id = allergyreport2.id, report_entity_id = AllergyEntity.id, report_attribute_id = DescriptionAttribute.id, value = 'Causes rash and swelling')

medicationsreport1_value1 = ReportValue(report_id = medicationsreport1.id, report_entity_id = MedicationsEntity.id, report_attribute_id = NameAttribute.id, value = 'Paracetamol')
medicationsreport1_value2 = ReportValue(report_id = medicationsreport1.id, report_entity_id = MedicationsEntity.id, report_attribute_id = DateAttribute.id, value = '2020-01-01')

# add report values to database
allergyreport1_value1.insert()
allergyreport1_value2.insert()
allergyreport1_value3.insert()
allergyreport2_value1.insert()
allergyreport2_value2.insert()
allergyreport2_value3.insert()
medicationsreport1_value1.insert()
medicationsreport1_value2.insert()


# create instances of Address Type class (self, name)
address_type1 = AddressType(name='Country')
address_type2 = AddressType(name='City')
address_type3 = AddressType(name='Street')

# add address types to database
address_types = [address_type1, address_type2, address_type3]
for address_type in address_types:
    address_type.insert()

# Creating instances of Address class (self, name, address_type_id, parent_id)
# countries with parent_id = None
country1 = Address(name='United Kingdom', address_type_id=address_type1.id, parent_id=None)
country2 = Address(name='United States', address_type_id=address_type1.id, parent_id=None)
country3 = Address(name='France', address_type_id=address_type1.id, parent_id=None)
country4 = Address(name='Germany', address_type_id=address_type1.id, parent_id=None)
country5 = Address(name='Italy', address_type_id=address_type1.id, parent_id=None)

# add countries to database
countries = [country1, country2, country3, country4, country5]
for country in countries:
    country.insert()

# cities with parent_id = country
city1 = Address(name='London', address_type_id=address_type2.id, parent_id=country1.id)
city2 = Address(name='New York', address_type_id=address_type2.id, parent_id=country2.id)
city3 = Address(name='Paris', address_type_id=address_type2.id, parent_id=country3.id)
city4 = Address(name='Berlin', address_type_id=address_type2.id, parent_id=country4.id)
city5 = Address(name='Rome', address_type_id=address_type2.id, parent_id=country5.id)

# more cities with parent_id = country
city6 = Address(name='Manchester', address_type_id=address_type2.id, parent_id=country1.id)
city7 = Address(name='Liverpool', address_type_id=address_type2.id, parent_id=country1.id)
city8 = Address(name='Birmingham', address_type_id=address_type2.id, parent_id=country1.id)
city9 = Address(name='Leeds', address_type_id=address_type2.id, parent_id=country1.id)
city10 = Address(name='Sheffield', address_type_id=address_type2.id, parent_id=country1.id)

# more cities with parent_id = country
city11 = Address(name='Los Angeles', address_type_id=address_type2.id, parent_id=country2.id)
city12 = Address(name='Chicago', address_type_id=address_type2.id, parent_id=country2.id)
city13 = Address(name='Houston', address_type_id=address_type2.id, parent_id=country2.id)
city14 = Address(name='Phoenix', address_type_id=address_type2.id, parent_id=country2.id)
city15 = Address(name='Philadelphia', address_type_id=address_type2.id, parent_id=country2.id)

# more cities with parent_id = country
city16 = Address(name='Marseille', address_type_id=address_type2.id, parent_id=country3.id)
city17 = Address(name='Lyon', address_type_id=address_type2.id, parent_id=country3.id)
city18 = Address(name='Toulouse', address_type_id=address_type2.id, parent_id=country3.id)
city19 = Address(name='Nice', address_type_id=address_type2.id, parent_id=country3.id)
city20 = Address(name='Nantes', address_type_id=address_type2.id, parent_id=country3.id)

# more cities with parent_id = country
city21 = Address(name='Hamburg', address_type_id=address_type2.id, parent_id=country4.id)
city22 = Address(name='Munich', address_type_id=address_type2.id, parent_id=country4.id)
city23 = Address(name='Cologne', address_type_id=address_type2.id, parent_id=country4.id)
city24 = Address(name='Frankfurt', address_type_id=address_type2.id, parent_id=country4.id)
city25 = Address(name='Stuttgart', address_type_id=address_type2.id, parent_id=country4.id)

# more cities with parent_id = country
city26 = Address(name='Milan', address_type_id=address_type2.id, parent_id=country5.id)
city27 = Address(name='Naples', address_type_id=address_type2.id, parent_id=country5.id)
city28 = Address(name='Turin', address_type_id=address_type2.id, parent_id=country5.id)
city29 = Address(name='Palermo', address_type_id=address_type2.id, parent_id=country5.id)
city30 = Address(name='Genoa', address_type_id=address_type2.id, parent_id=country5.id)

# add cities to database
cities = [city1, city2, city3, city4, city5, city6, city7, city8, city9, city10,
            city11, city12, city13, city14, city15, city16, city17, city18, city19, city20,
            city21, city22, city23, city24, city25, city26, city27, city28, city29, city30]

for city in cities:
    city.insert()

# streets with parent_id = city
street1 = Address(name='Baker Street', address_type_id=address_type3.id, parent_id=city1.id)
street2 = Address(name='Oxford Street', address_type_id=address_type3.id, parent_id=city1.id)
street3 = Address(name='Regent Street', address_type_id=address_type3.id, parent_id=city1.id)
street4 = Address(name='Bond Street', address_type_id=address_type3.id, parent_id=city1.id)
street5 = Address(name='Park Avenue', address_type_id=address_type3.id, parent_id=city2.id)

# more streets with parent_id = city
street6 = Address(name='Broadway', address_type_id=address_type3.id, parent_id=city2.id)
street7 = Address(name='Madison Avenue', address_type_id=address_type3.id, parent_id=city2.id)
street8 = Address(name='Fifth Avenue', address_type_id=address_type3.id, parent_id=city2.id)
street9 = Address(name='Wall Street', address_type_id=address_type3.id, parent_id=city2.id)
street10 = Address(name='Champs-Elysees', address_type_id=address_type3.id, parent_id=city3.id)

# add streets to database
streets = [street1, street2, street3, street4, street5, street6, street7, street8, street9, street10]
for street in streets:
    street.insert()

print(Address.query.get(street1.id).get_full_address())
print(Address.query.get(street1.id).get_address_string())

