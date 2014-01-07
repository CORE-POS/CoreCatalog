from sqlalchemy import Column, Integer, String, Text, Numeric, ForeignKey
from sqlalchemy.orm import relationship, backref
from CoreCatalog.database import Base

class Items(Base):
    __tablename__ = 'items'
    upc = Column(String(13), primary_key=True)
    short_description = Column(String(35))
    long_description = Column(String(255))
    brand = Column(String(255))
    unit_size = Column(String(50))

    def __repr__(self):
        return '<Item %r>' % (self.upc)

    def serialize(self):
        repr = {}
        repr['upc'] = self.upc
        repr['short_description'] = self.short_description
        repr['long_description'] = self.long_description
        repr['brand'] = self.brand
        repr['unit_size'] = self.unit_size
        return repr

class ApiKeys(Base):
    __tablename__ = 'apikeys'
    id = Column(Integer, primary_key=True, autoincrement=True)
    apikey = Column(String(40))
