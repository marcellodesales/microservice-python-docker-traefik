# SQLAlchemy Example

.. note::

A simple example of how one might use SQLAlchemy as a backing store for a 
Connexion based application.

# Development

Create a new virtual environment and install the required libraries
with these commands:

.. code-block:: bash

    $ python3.13 -m venv my-venv
    $ source my-venv/bin/activate
    $ pip install -r requirements.txt

# Running

Launch the connexion server with this command:

```console
$ docker compose up --build
[+] Building 1.6s (17/17) FINISHED                                                                                                           docker-container:kind_khayyam
 => [myapp internal] load build definition from Dockerfile                                                                                                            0.0s
 => => transferring dockerfile: 570B                                                                                                                                  0.0s
 => [myapp internal] load metadata for docker.io/library/python:3.13.2-alpine3.21                                                                                     1.2s
 => [myapp internal] load .dockerignore                                                                                                                               0.0s
 => => transferring context: 2B                                                                                                                                       0.0s
 => [myapp internal] load build context                                                                                                                               0.0s
 => => transferring context: 21.83kB                                                                                                                                  0.0s
 => [myapp builder 1/7] FROM docker.io/library/python:3.13.2-alpine3.21@sha256:323a717dc4a010fee21e3f1aac738ee10bb485de4e7593ce242b36ee48d6b352                       0.0s
 => => resolve docker.io/library/python:3.13.2-alpine3.21@sha256:323a717dc4a010fee21e3f1aac738ee10bb485de4e7593ce242b36ee48d6b352                                     0.0s
 => CACHED [myapp service 2/5] WORKDIR /root/app/site-packages                                                                                                        0.0s
 => CACHED [myapp builder 2/7] WORKDIR /usr/src/app                                                                                                                   0.0s
 => CACHED [myapp builder 3/7] RUN python3 -m venv /venv                                                                                                              0.0s
 => CACHED [myapp builder 4/7] RUN pip install --upgrade pip                                                                                                          0.0s
 => CACHED [myapp builder 5/7] RUN apk add cargo                                                                                                                      0.0s
 => CACHED [myapp builder 6/7] COPY requirements.txt requirements.txt                                                                                                 0.0s
 => CACHED [myapp builder 7/7] RUN pip install --no-cache-dir -r requirements.txt                                                                                     0.0s
 => CACHED [myapp service 3/5] COPY --from=builder /venv /venv                                                                                                        0.0s
 => CACHED [myapp service 4/5] RUN pip install uvicorn                                                                                                                0.0s
 => [myapp service 5/5] COPY . .                                                                                                                                      0.0s
 => [myapp] exporting to docker image format                                                                                                                          0.4s
 => => exporting layers                                                                                                                                               0.0s
 => => exporting manifest sha256:a781cb609b01b4d486339b9f3a8492887884321c50be8f9de61933e61a443b91                                                                     0.0s
 => => exporting config sha256:717d6bb00e3cf1b21a210d848f01f55f4282c42bc86c3fe736a0ed760b7ca5fd                                                                       0.0s
 => => sending tarball                                                                                                                                                0.3s
 => [myapp] importing to docker                                                                                                                                       0.0s
 => => loading layer 7d9dccedd8e5 32.77kB / 56.78kB                                                                                                                   0.0s
WARN[0001] Found orphan containers ([sqlalchemy-traefik-1 sqlalchemy-service-1]) for this project. If you removed or renamed this service in your compose file, you can run this command with the --remove-orphans flag to clean it up.
[+] Running 1/0
 ✔ Container sqlalchemy-myapp-6  Recreated                                                                                                                            0.1s
Attaching to myapp-6
WARN[0002] Found orphan containers ([sqlalchemy-traefik-1 sqlalchemy-service-1]) for this project. If you removed or renamed this service in your compose file, you can run this command with the --remove-orphans flag to clean it up.
[+] Running 1/0
 ✔ Container sqlalchemy-myapp-6  Recreated                                                                                                                            0.0s
Attaching to myapp-6
myapp-6  | Setting up logger with level INFO
myapp-6  | 2025-03-12 17:32:54,724 INFO sqlalchemy.engine.Engine BEGIN (implicit)
myapp-6  | 2025-03-12 17:32:54,724 INFO BEGIN (implicit)
myapp-6  | 2025-03-12 17:32:54,726 INFO PRAGMA main.table_info("pets")
myapp-6  | 2025-03-12 17:32:54,726 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("pets")
myapp-6  | 2025-03-12 17:32:54,726 INFO sqlalchemy.engine.Engine [raw sql] ()
myapp-6  | 2025-03-12 17:32:54,726 INFO [raw sql] ()
myapp-6  | 2025-03-12 17:32:54,735 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("pets")
myapp-6  | 2025-03-12 17:32:54,735 INFO sqlalchemy.engine.Engine [raw sql] ()
myapp-6  | 2025-03-12 17:32:54,735 INFO PRAGMA temp.table_info("pets")
myapp-6  | 2025-03-12 17:32:54,735 INFO [raw sql] ()
myapp-6  | 2025-03-12 17:32:54,736 INFO
myapp-6  | CREATE TABLE pets (
myapp-6  | 	id VARCHAR(20) NOT NULL,
myapp-6  | 	name VARCHAR(100),
myapp-6  | 	animal_type VARCHAR(20),
myapp-6  | 	created DATETIME,
myapp-6  | 	PRIMARY KEY (id)
myapp-6  | )
myapp-6  |
myapp-6  |
myapp-6  | 2025-03-12 17:32:54,736 INFO sqlalchemy.engine.Engine
myapp-6  | CREATE TABLE pets (
myapp-6  | 	id VARCHAR(20) NOT NULL,
myapp-6  | 	name VARCHAR(100),
myapp-6  | 	animal_type VARCHAR(20),
myapp-6  | 	created DATETIME,
myapp-6  | 	PRIMARY KEY (id)
myapp-6  | )
myapp-6  |
myapp-6  |
myapp-6  | 2025-03-12 17:32:54,736 INFO sqlalchemy.engine.Engine [no key 0.00007s] ()
myapp-6  | 2025-03-12 17:32:54,736 INFO [no key 0.00007s] ()
myapp-6  | 2025-03-12 17:32:54,743 INFO sqlalchemy.engine.Engine COMMIT
myapp-6  | 2025-03-12 17:32:54,743 INFO COMMIT
myapp-6  | 2025-03-12 17:32:54,766 INFO BEGIN (implicit)
myapp-6  | 2025-03-12 17:32:54,766 INFO sqlalchemy.engine.Engine BEGIN (implicit)
myapp-6  | 2025-03-12 17:32:54,768 INFO sqlalchemy.engine.Engine SELECT pets.id AS pets_id, pets.name AS pets_name, pets.animal_type AS pets_animal_type, pets.created AS pets_created
myapp-6  | FROM pets
myapp-6  | WHERE pets.id = ?
myapp-6  | 2025-03-12 17:32:54,768 INFO SELECT pets.id AS pets_id, pets.name AS pets_name, pets.animal_type AS pets_animal_type, pets.created AS pets_created
myapp-6  | FROM pets
myapp-6  | WHERE pets.id = ?
myapp-6  | 2025-03-12 17:32:54,768 INFO sqlalchemy.engine.Engine [generated in 0.00016s] (1,)
myapp-6  | 2025-03-12 17:32:54,768 INFO [generated in 0.00016s] (1,)
myapp-6  | 2025-03-12 17:32:54,770 resources.py:43 INFO - Creating pet 1..
myapp-6  | 2025-03-12 17:32:54,770 INFO Creating pet 1..
myapp-6  | 2025-03-12 17:32:54,771 INFO INSERT INTO pets (id, name, animal_type, created) VALUES (?, ?, ?, ?)
myapp-6  | 2025-03-12 17:32:54,771 INFO sqlalchemy.engine.Engine INSERT INTO pets (id, name, animal_type, created) VALUES (?, ?, ?, ?)
myapp-6  | 2025-03-12 17:32:54,771 INFO sqlalchemy.engine.Engine [generated in 0.00016s] (1, 'Aldo', 'cat', '2025-03-12 17:32:54.770459')
myapp-6  | 2025-03-12 17:32:54,771 INFO [generated in 0.00016s] (1, 'Aldo', 'cat', '2025-03-12 17:32:54.770459')
myapp-6  | 2025-03-12 17:32:54,773 INFO COMMIT
myapp-6  | 2025-03-12 17:32:54,773 INFO sqlalchemy.engine.Engine COMMIT
myapp-6  | 2025-03-12 17:32:54,773 INFO BEGIN (implicit)
myapp-6  | 2025-03-12 17:32:54,773 INFO sqlalchemy.engine.Engine BEGIN (implicit)
myapp-6  | 2025-03-12 17:32:54,773 INFO SELECT pets.id AS pets_id, pets.name AS pets_name, pets.animal_type AS pets_animal_type, pets.created AS pets_created
myapp-6  | FROM pets
myapp-6  | WHERE pets.id = ?
myapp-6  | 2025-03-12 17:32:54,773 INFO sqlalchemy.engine.Engine SELECT pets.id AS pets_id, pets.name AS pets_name, pets.animal_type AS pets_animal_type, pets.created AS pets_created
myapp-6  | FROM pets
myapp-6  | WHERE pets.id = ?
myapp-6  | 2025-03-12 17:32:54,773 INFO sqlalchemy.engine.Engine [cached since 0.00498s ago] (2,)
myapp-6  | 2025-03-12 17:32:54,773 INFO [cached since 0.00498s ago] (2,)
myapp-6  | 2025-03-12 17:32:54,774 resources.py:43 INFO - Creating pet 2..
myapp-6  | 2025-03-12 17:32:54,774 INFO Creating pet 2..
myapp-6  | 2025-03-12 17:32:54,774 INFO INSERT INTO pets (id, name, animal_type, created) VALUES (?, ?, ?, ?)
myapp-6  | 2025-03-12 17:32:54,774 INFO sqlalchemy.engine.Engine INSERT INTO pets (id, name, animal_type, created) VALUES (?, ?, ?, ?)
myapp-6  | 2025-03-12 17:32:54,774 INFO sqlalchemy.engine.Engine [cached since 0.002861s ago] (2, 'Bailey', 'dog', '2025-03-12 17:32:54.774116')
myapp-6  | 2025-03-12 17:32:54,774 INFO [cached since 0.002861s ago] (2, 'Bailey', 'dog', '2025-03-12 17:32:54.774116')
myapp-6  | 2025-03-12 17:32:54,774 INFO COMMIT
myapp-6  | 2025-03-12 17:32:54,774 INFO sqlalchemy.engine.Engine COMMIT
myapp-6  | 2025-03-12 17:32:54,774 INFO BEGIN (implicit)
myapp-6  | 2025-03-12 17:32:54,774 INFO sqlalchemy.engine.Engine BEGIN (implicit)
myapp-6  | 2025-03-12 17:32:54,775 INFO SELECT pets.id AS pets_id, pets.name AS pets_name, pets.animal_type AS pets_animal_type, pets.created AS pets_created
myapp-6  | FROM pets
myapp-6  | WHERE pets.id = ?
myapp-6  | 2025-03-12 17:32:54,775 INFO sqlalchemy.engine.Engine SELECT pets.id AS pets_id, pets.name AS pets_name, pets.animal_type AS pets_animal_type, pets.created AS pets_created
myapp-6  | FROM pets
myapp-6  | WHERE pets.id = ?
myapp-6  | 2025-03-12 17:32:54,775 INFO sqlalchemy.engine.Engine [cached since 0.006511s ago] (3,)
myapp-6  | 2025-03-12 17:32:54,775 INFO [cached since 0.006511s ago] (3,)
myapp-6  | 2025-03-12 17:32:54,775 resources.py:43 INFO - Creating pet 3..
myapp-6  | 2025-03-12 17:32:54,775 INFO Creating pet 3..
myapp-6  | 2025-03-12 17:32:54,775 INFO INSERT INTO pets (id, name, animal_type, created) VALUES (?, ?, ?, ?)
myapp-6  | 2025-03-12 17:32:54,775 INFO sqlalchemy.engine.Engine INSERT INTO pets (id, name, animal_type, created) VALUES (?, ?, ?, ?)
myapp-6  | 2025-03-12 17:32:54,775 INFO sqlalchemy.engine.Engine [cached since 0.004057s ago] (3, 'Hugo', 'cat', '2025-03-12 17:32:54.775348')
myapp-6  | 2025-03-12 17:32:54,775 INFO [cached since 0.004057s ago] (3, 'Hugo', 'cat', '2025-03-12 17:32:54.775348')
myapp-6  | 2025-03-12 17:32:54,775 INFO sqlalchemy.engine.Engine COMMIT
myapp-6  | 2025-03-12 17:32:54,775 INFO COMMIT
myapp-6  | INFO:     Started server process [1]
myapp-6  | INFO:     Waiting for application startup.
myapp-6  | 2025-03-12 17:32:54,780 INFO Adding spec json: /openapi/openapi.json
myapp-6  | INFO:     Application startup complete.
myapp-6  | INFO:     Uvicorn running on http://0.0.0.0:8081 (Press CTRL+C to quit)
```

Now open your browser and view the Swagger UI for these specification files:

* http://localhost:8080/openapi/ui/ for the OpenAPI 3 spec

