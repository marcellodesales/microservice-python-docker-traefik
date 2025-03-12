import logger
import connexion
import resources
import inspect

log = logger.get_logger(__name__)
log.debug("Bootstrapping the app...")

app = connexion.FlaskApp(__name__, specification_dir="spec")
app.add_api("openapi.yaml")

resources.init()

if __name__ == "__main__":
    app.run(port=8081, reload=False)


