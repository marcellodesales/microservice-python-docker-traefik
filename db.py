import logger
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

import orm

log = logger.get_logger(__name__)

# Get the base class from all resources
Base = orm.get_base_class()

def init_db(file_path: None):
    """
    Initialize the database and return a sessionmaker object.
    `check_same_thread` and `StaticPool` are helpful for unit testing of
    in-memory sqlite databases; they should not be used in production.
    https://stackoverflow.com/questions/6519546/scoped-sessionsessionmaker-or-plain-sessionmaker-in-sqlalchemy
    """

    log.debug("Bootstrapping the sqlite database...")

    engine = None
    if not file_path:
        log.debug("Creating an in-memory sqlite database at 'sqlite:///:memory:'")
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
    
      log.debug("Creating an file-system sqlite database at 'sqlite:///{data_volume_dir}/{file_name}'")

      # Create engine with file-based SQLite
      engine = create_engine(
          url=f"sqlite:///{data_volume_dir}/{file_name}",  # Use a file path instead of :memory:
          connect_args={"check_same_thread": False},  # Can keep this for dev purposes
          echo=True,
      )
 
    # Create all tables
    Base.metadata.create_all(bind=engine)
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Singleton instance for the db_session_factory
if 'DB_FILE' in os.environ:
  db_session_singleton = init_db(os.environ["DB_FILE"]) 

else:
  db_session_singleton = init_db(None)


# Export the session factory
def get_db_session_factory():
    return db_session_singleton


