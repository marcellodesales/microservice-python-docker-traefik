from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

import os

Base = declarative_base()

def get_base_class():
  return Base


class Pet(Base):
    __tablename__ = "pets"
    id = Column(String(20), primary_key=True)
    name = Column(String(100))
    animal_type = Column(String(20))
    created = Column(DateTime())

    def update(self, id=None, name=None, animal_type=None, tags=None, created=None):
        if name is not None:
            self.name = name
        if animal_type is not None:
            self.animal_type = animal_type
        if created is not None:
            self.created = created

    def dump(self):
        return {k: v for k, v in vars(self).items() if not k.startswith("_")}

