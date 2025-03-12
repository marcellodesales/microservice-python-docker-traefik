####
#### These are contracts with openapi.yaml
#### 
from datetime import datetime, timezone
from connexion import NoContent

import orm
import logger
from db import get_db_session_factory

log = logger.get_logger(__name__)

db_session_factory = get_db_session_factory()

def get_pets(limit, animal_type=None):
    log.debug("Getting pets...")

    with db_session_factory() as db_session:
        q = db_session.query(orm.Pet)
        if animal_type:
            q = q.filter(orm.Pet.animal_type == animal_type)
        return [p.dump() for p in q][:limit]


def get_pet(pet_id):
    log.debug(f"Getting a pet with id={pet_id}")

    with db_session_factory() as db_session:
        pet = db_session.query(orm.Pet).filter(orm.Pet.id == pet_id).one_or_none()
        return pet.dump() if pet is not None else ("Not found", 404)


def put_pet(pet_id, pet):
    log.debug(f"Updating a pet with id={pet_id}")

    with db_session_factory() as db_session:
        p = db_session.query(orm.Pet).filter(orm.Pet.id == pet_id).one_or_none()
        pet["id"] = pet_id
        if p is not None:
            log.info("Updating pet %s..", pet_id)
            p.update(**pet)
        else:
            log.info("Creating pet %s..", pet_id)
            pet["created"] = datetime.now(timezone.utc)
            db_session.add(orm.Pet(**pet))
        db_session.commit()
        return NoContent, (200 if p is not None else 201)


def delete_pet(pet_id):
    log.debug(f"Deleting a pet with id={pet_id}")

    with db_session_factory() as db_session:
        pet = db_session.query(orm.Pet).filter(orm.Pet.id == pet_id).one_or_none()
        if pet is not None:
            log.info("Deleting pet %s..", pet_id)
            db_session.delete(pet)
            db_session.commit()
            return NoContent, 204
        else:
            return NoContent, 404

def init():
  # Initialize the db with instances
  pets = {
    1: {"name": "Aldo", "animal_type": "cat"},
    2: {"name": "Bailey", "animal_type": "dog"},
    3: {"name": "Hugo", "animal_type": "cat"},
  }
  for id_, pet in pets.items():
    put_pet(id_, pet)

