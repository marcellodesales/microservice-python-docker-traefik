import logger
import connexion
import resources
import inspect

log = logger.get_logger(__name__)
log.debug("Bootstrapping the app...")

app = connexion.FlaskApp(__name__, specification_dir="spec")
app.add_api("openapi.yaml")

# Initialize the local memory
pets = {
    1: {"name": "Aldo", "animal_type": "cat"},
    2: {"name": "Bailey", "animal_type": "dog"},
    3: {"name": "Hugo", "animal_type": "cat"},
}
for id_, pet in pets.items():
    resources.put_pet(id_, pet)

if __name__ == "__main__":
    app.run(port=8081, reload=False)


