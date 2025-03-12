from sqlalchemy import Column, DateTime, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

import os

Base = declarative_base()


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

def init_db(file_path: None):
    """
    Initialize the database and return a sessionmaker object.
    `check_same_thread` and `StaticPool` are helpful for unit testing of
    in-memory sqlite databases; they should not be used in production.
    https://stackoverflow.com/questions/6519546/scoped-sessionsessionmaker-or-plain-sessionmaker-in-sqlalchemy
    """

    engine = None
    if not file_path:
        engine = create_engine(
          url="sqlite:///:memory:",
          connect_args={"check_same_thread": False},
          poolclass=StaticPool,
          echo=True,
        )

    else:
      data_volume_dir = "/app/data"
      try:
        os.makedirs(data_volume_dir, exist_ok=False)
      except FileExistsError:
        pass # Directory exists, no action needed
      except Exception as e:
        raise Exception(f"An error occurred: {e}") from e
      else:
        raise FileNotFoundError(f"Data dir '{data_volume_dir}' does not exist. Declare a volume for it!")

      file_name = os.path.basename(file_path)
    
      # Create engine with file-based SQLite
      engine = create_engine(
          url=f"sqlite:///{data_volume_dir}/{file_name}",  # Use a file path instead of :memory:
          connect_args={"check_same_thread": False},  # Can keep this for dev purposes
          echo=True,
      )
 
    # Create all tables
    Base.metadata.create_all(bind=engine)
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)
