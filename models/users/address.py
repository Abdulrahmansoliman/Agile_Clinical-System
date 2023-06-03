from models.init import db, BaseDbModel

class Address(BaseDbModel, db.Model):
    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=True)
    name = db.Column(db.String(50), nullable=False)
    address_type_id = db.Column(db.Integer, db.ForeignKey('address_type.id'), nullable=False)

    def __init__(self, name, address_type_id, parent_id):
        self.name = name
        self.address_type_id = address_type_id
        self.parent_id = parent_id
    
    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'address_type': self.address_type.format(),
            'parent_id': self.parent_id
        }

    def get_address(self):
        address = self
        address_list = [address]
        while address.parent_id is not None:
            address = Address.query.get(address.parent_id)
            address_list.append(address)
        return address_list[::-1]
    
    def get_address_string(self):
        address_list = self.get_address()
        address_string = ''
        for address in address_list:
            address_string += address.name + ', '
        return address_string[:-2]
    
    def get_full_address(self):
        address_list = self.get_address()
        address_string = ''
        for address in address_list:
            address_string += address.address_type.name + ': ' +  address.name + ', '
        return address_string[:-2]
    