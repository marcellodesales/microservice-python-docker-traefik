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
myapp-6  | 2025-03-12 17:21:24,263 db.py:22 DEBUG - Bootstrapping the sqlite database...
myapp-6  | 2025-03-12 17:21:24,263 DEBUG /root/app/site-packages/db.py:22:init_db Bootstrapping the sqlite database...
myapp-6  | 2025-03-12 17:21:24,265 db.py:26 DEBUG - Creating an in-memory sqlite database at 'sqlite:///:memory:'
myapp-6  | 2025-03-12 17:21:24,265 DEBUG /root/app/site-packages/db.py:26:init_db Creating an in-memory sqlite database at 'sqlite:///:memory:'
myapp-6  | 2025-03-12 17:21:24,278 INFO /venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py:2699:_connection_begin_impl BEGIN (implicit)
myapp-6  | Setting up logger with level DEBUG
myapp-6  | 2025-03-12 17:21:24,278 INFO sqlalchemy.engine.Engine BEGIN (implicit)
myapp-6  | 2025-03-12 17:21:24,278 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("pets")
myapp-6  | 2025-03-12 17:21:24,278 INFO /venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py:1843:_execute_context PRAGMA main.table_info("pets")
myapp-6  | 2025-03-12 17:21:24,278 INFO sqlalchemy.engine.Engine [raw sql] ()
myapp-6  | 2025-03-12 17:21:24,278 INFO /venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py:1843:_execute_context [raw sql] ()
myapp-6  | 2025-03-12 17:21:24,286 INFO /venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py:1843:_execute_context PRAGMA temp.table_info("pets")
myapp-6  | 2025-03-12 17:21:24,286 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("pets")
myapp-6  | 2025-03-12 17:21:24,286 INFO /venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py:1843:_execute_context [raw sql] ()
myapp-6  | 2025-03-12 17:21:24,286 INFO sqlalchemy.engine.Engine [raw sql] ()
myapp-6  | 2025-03-12 17:21:24,287 INFO /venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py:1843:_execute_context
myapp-6  | CREATE TABLE pets (
myapp-6  | 	id VARCHAR(20) NOT NULL,
myapp-6  | 	name VARCHAR(100),
myapp-6  | 	animal_type VARCHAR(20),
myapp-6  | 	created DATETIME,
myapp-6  | 	PRIMARY KEY (id)
myapp-6  | )
myapp-6  |
myapp-6  |
myapp-6  | 2025-03-12 17:21:24,287 INFO sqlalchemy.engine.Engine
myapp-6  | CREATE TABLE pets (
myapp-6  | 	id VARCHAR(20) NOT NULL,
myapp-6  | 	name VARCHAR(100),
myapp-6  | 	animal_type VARCHAR(20),
myapp-6  | 	created DATETIME,
myapp-6  | 	PRIMARY KEY (id)
myapp-6  | )
myapp-6  |
myapp-6  |
myapp-6  | 2025-03-12 17:21:24,288 INFO /venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py:1843:_execute_context [no key 0.00007s] ()
myapp-6  | 2025-03-12 17:21:24,288 INFO sqlalchemy.engine.Engine [no key 0.00007s] ()
myapp-6  | 2025-03-12 17:21:24,295 INFO /venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py:2705:_connection_commit_impl COMMIT
myapp-6  | 2025-03-12 17:21:24,295 INFO sqlalchemy.engine.Engine COMMIT
myapp-6  | 2025-03-12 17:21:24,295 app.py:7 DEBUG - Bootstrapping the app...
myapp-6  | 2025-03-12 17:21:24,295 DEBUG /root/app/site-packages/app.py:7:<module> Bootstrapping the app...
myapp-6  | 2025-03-12 17:21:24,316 resources.py:34 DEBUG - Updating a pet with id=1
myapp-6  | 2025-03-12 17:21:24,316 DEBUG /root/app/site-packages/resources.py:34:put_pet Updating a pet with id=1
myapp-6  | 2025-03-12 17:21:24,317 INFO /venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py:2699:_connection_begin_impl BEGIN (implicit)
myapp-6  | 2025-03-12 17:21:24,317 INFO sqlalchemy.engine.Engine BEGIN (implicit)
myapp-6  | 2025-03-12 17:21:24,320 INFO /venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py:1843:_execute_context SELECT pets.id AS pets_id, pets.name AS pets_name, pets.animal_type AS pets_animal_type, pets.created AS pets_created
myapp-6  | FROM pets
myapp-6  | WHERE pets.id = ?
myapp-6  | 2025-03-12 17:21:24,320 INFO sqlalchemy.engine.Engine SELECT pets.id AS pets_id, pets.name AS pets_name, pets.animal_type AS pets_animal_type, pets.created AS pets_created
myapp-6  | FROM pets
myapp-6  | WHERE pets.id = ?
myapp-6  | 2025-03-12 17:21:24,320 INFO sqlalchemy.engine.Engine [generated in 0.00015s] (1,)
myapp-6  | 2025-03-12 17:21:24,320 INFO /venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py:1843:_execute_context [generated in 0.00015s] (1,)
myapp-6  | 2025-03-12 17:21:24,322 resources.py:43 INFO - Creating pet 1..
myapp-6  | 2025-03-12 17:21:24,322 INFO /root/app/site-packages/resources.py:43:put_pet Creating pet 1..
myapp-6  | 2025-03-12 17:21:24,323 INFO sqlalchemy.engine.Engine INSERT INTO pets (id, name, animal_type, created) VALUES (?, ?, ?, ?)
myapp-6  | 2025-03-12 17:21:24,323 INFO /venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py:1843:_execute_context INSERT INTO pets (id, name, animal_type, created) VALUES (?, ?, ?, ?)
myapp-6  | 2025-03-12 17:21:24,323 INFO sqlalchemy.engine.Engine [generated in 0.00017s] (1, 'Aldo', 'cat', '2025-03-12 17:21:24.322236')
myapp-6  | 2025-03-12 17:21:24,323 INFO /venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py:1843:_execute_context [generated in 0.00017s] (1, 'Aldo', 'cat', '2025-03-12 17:21:24.322236')
myapp-6  | 2025-03-12 17:21:24,324 INFO /venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py:2705:_connection_commit_impl COMMIT
myapp-6  | 2025-03-12 17:21:24,324 INFO sqlalchemy.engine.Engine COMMIT
myapp-6  | 2025-03-12 17:21:24,325 resources.py:34 DEBUG - Updating a pet with id=2
myapp-6  | 2025-03-12 17:21:24,325 DEBUG /root/app/site-packages/resources.py:34:put_pet Updating a pet with id=2
myapp-6  | 2025-03-12 17:21:24,325 INFO /venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py:2699:_connection_begin_impl BEGIN (implicit)
myapp-6  | 2025-03-12 17:21:24,325 INFO sqlalchemy.engine.Engine BEGIN (implicit)
myapp-6  | 2025-03-12 17:21:24,325 INFO /venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py:1843:_execute_context SELECT pets.id AS pets_id, pets.name AS pets_name, pets.animal_type AS pets_animal_type, pets.created AS pets_created
myapp-6  | FROM pets
myapp-6  | WHERE pets.id = ?
myapp-6  | 2025-03-12 17:21:24,325 INFO sqlalchemy.engine.Engine SELECT pets.id AS pets_id, pets.name AS pets_name, pets.animal_type AS pets_animal_type, pets.created AS pets_created
myapp-6  | FROM pets
myapp-6  | WHERE pets.id = ?
myapp-6  | 2025-03-12 17:21:24,325 INFO sqlalchemy.engine.Engine [cached since 0.005352s ago] (2,)
myapp-6  | 2025-03-12 17:21:24,325 INFO /venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py:1843:_execute_context [cached since 0.005352s ago] (2,)
myapp-6  | 2025-03-12 17:21:24,325 resources.py:43 INFO - Creating pet 2..
myapp-6  | 2025-03-12 17:21:24,325 INFO /root/app/site-packages/resources.py:43:put_pet Creating pet 2..
myapp-6  | 2025-03-12 17:21:24,326 INFO sqlalchemy.engine.Engine INSERT INTO pets (id, name, animal_type, created) VALUES (?, ?, ?, ?)
myapp-6  | 2025-03-12 17:21:24,326 INFO /venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py:1843:_execute_context INSERT INTO pets (id, name, animal_type, created) VALUES (?, ?, ?, ?)
myapp-6  | 2025-03-12 17:21:24,326 INFO sqlalchemy.engine.Engine [cached since 0.002932s ago] (2, 'Bailey', 'dog', '2025-03-12 17:21:24.326017')
myapp-6  | 2025-03-12 17:21:24,326 INFO /venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py:1843:_execute_context [cached since 0.002932s ago] (2, 'Bailey', 'dog', '2025-03-12 17:21:24.326017')
myapp-6  | 2025-03-12 17:21:24,326 INFO sqlalchemy.engine.Engine COMMIT
myapp-6  | 2025-03-12 17:21:24,326 INFO /venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py:2705:_connection_commit_impl COMMIT
myapp-6  | 2025-03-12 17:21:24,326 resources.py:34 DEBUG - Updating a pet with id=3
myapp-6  | 2025-03-12 17:21:24,326 DEBUG /root/app/site-packages/resources.py:34:put_pet Updating a pet with id=3
myapp-6  | 2025-03-12 17:21:24,326 INFO /venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py:2699:_connection_begin_impl BEGIN (implicit)
myapp-6  | 2025-03-12 17:21:24,326 INFO sqlalchemy.engine.Engine BEGIN (implicit)
myapp-6  | 2025-03-12 17:21:24,327 INFO /venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py:1843:_execute_context SELECT pets.id AS pets_id, pets.name AS pets_name, pets.animal_type AS pets_animal_type, pets.created AS pets_created
myapp-6  | FROM pets
myapp-6  | WHERE pets.id = ?
myapp-6  | 2025-03-12 17:21:24,327 INFO sqlalchemy.engine.Engine SELECT pets.id AS pets_id, pets.name AS pets_name, pets.animal_type AS pets_animal_type, pets.created AS pets_created
myapp-6  | FROM pets
myapp-6  | WHERE pets.id = ?
myapp-6  | 2025-03-12 17:21:24,327 INFO sqlalchemy.engine.Engine [cached since 0.006813s ago] (3,)
myapp-6  | 2025-03-12 17:21:24,327 INFO /venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py:1843:_execute_context [cached since 0.006813s ago] (3,)
myapp-6  | 2025-03-12 17:21:24,327 resources.py:43 INFO - Creating pet 3..
myapp-6  | 2025-03-12 17:21:24,327 INFO /root/app/site-packages/resources.py:43:put_pet Creating pet 3..
myapp-6  | 2025-03-12 17:21:24,327 INFO /venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py:1843:_execute_context INSERT INTO pets (id, name, animal_type, created) VALUES (?, ?, ?, ?)
myapp-6  | 2025-03-12 17:21:24,327 INFO sqlalchemy.engine.Engine INSERT INTO pets (id, name, animal_type, created) VALUES (?, ?, ?, ?)
myapp-6  | 2025-03-12 17:21:24,327 INFO sqlalchemy.engine.Engine [cached since 0.004122s ago] (3, 'Hugo', 'cat', '2025-03-12 17:21:24.327255')
myapp-6  | 2025-03-12 17:21:24,327 INFO /venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py:1843:_execute_context [cached since 0.004122s ago] (3, 'Hugo', 'cat', '2025-03-12 17:21:24.327255')
myapp-6  | 2025-03-12 17:21:24,327 INFO /venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py:2705:_connection_commit_impl COMMIT
myapp-6  | 2025-03-12 17:21:24,327 INFO sqlalchemy.engine.Engine COMMIT
myapp-6  | INFO:     Started server process [1]
myapp-6  | INFO:     Waiting for application startup.
myapp-6  | 2025-03-12 17:21:24,329 DEBUG /venv/lib/python3.13/site-packages/connexion/middleware/abstract.py:89:add_paths Adding /openapi/pets...
myapp-6  | 2025-03-12 17:21:24,329 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:100:__init__ consumes: []
myapp-6  | 2025-03-12 17:21:24,329 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:101:__init__ produces: ['application/json']
myapp-6  | 2025-03-12 17:21:24,329 DEBUG /venv/lib/python3.13/site-packages/connexion/middleware/abstract.py:89:add_paths Adding /openapi/pets/{pet_id}...
myapp-6  | 2025-03-12 17:21:24,330 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:100:__init__ consumes: []
myapp-6  | 2025-03-12 17:21:24,330 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:101:__init__ produces: ['application/json']
myapp-6  | 2025-03-12 17:21:24,330 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:100:__init__ consumes: ['application/json']
myapp-6  | 2025-03-12 17:21:24,330 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:101:__init__ produces: []
myapp-6  | 2025-03-12 17:21:24,330 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:100:__init__ consumes: []
myapp-6  | 2025-03-12 17:21:24,330 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:101:__init__ produces: []
myapp-6  | 2025-03-12 17:21:24,332 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:100:__init__ consumes: []
myapp-6  | 2025-03-12 17:21:24,332 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:101:__init__ produces: ['application/json']
myapp-6  | 2025-03-12 17:21:24,332 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:100:__init__ consumes: []
myapp-6  | 2025-03-12 17:21:24,332 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:101:__init__ produces: ['application/json']
myapp-6  | 2025-03-12 17:21:24,332 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:100:__init__ consumes: ['application/json']
myapp-6  | 2025-03-12 17:21:24,332 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:101:__init__ produces: []
myapp-6  | 2025-03-12 17:21:24,332 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:100:__init__ consumes: []
myapp-6  | 2025-03-12 17:21:24,332 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:101:__init__ produces: []
myapp-6  | 2025-03-12 17:21:24,333 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:100:__init__ consumes: []
myapp-6  | 2025-03-12 17:21:24,333 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:101:__init__ produces: ['application/json']
myapp-6  | 2025-03-12 17:21:24,333 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:100:__init__ consumes: []
myapp-6  | 2025-03-12 17:21:24,333 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:101:__init__ produces: ['application/json']
myapp-6  | 2025-03-12 17:21:24,333 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:100:__init__ consumes: ['application/json']
myapp-6  | 2025-03-12 17:21:24,333 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:101:__init__ produces: []
myapp-6  | 2025-03-12 17:21:24,333 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:100:__init__ consumes: []
myapp-6  | 2025-03-12 17:21:24,333 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:101:__init__ produces: []
myapp-6  | 2025-03-12 17:21:24,333 DEBUG /venv/lib/python3.13/site-packages/connexion/middleware/request_validation.py:159:__init__ Strict Request Validation: None
myapp-6  | 2025-03-12 17:21:24,333 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:100:__init__ consumes: []
myapp-6  | 2025-03-12 17:21:24,333 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:101:__init__ produces: ['application/json']
myapp-6  | 2025-03-12 17:21:24,333 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:100:__init__ consumes: []
myapp-6  | 2025-03-12 17:21:24,333 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:101:__init__ produces: ['application/json']
myapp-6  | 2025-03-12 17:21:24,333 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:100:__init__ consumes: ['application/json']
myapp-6  | 2025-03-12 17:21:24,333 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:101:__init__ produces: []
myapp-6  | 2025-03-12 17:21:24,333 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:100:__init__ consumes: []
myapp-6  | 2025-03-12 17:21:24,333 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:101:__init__ produces: []
myapp-6  | 2025-03-12 17:21:24,333 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:100:__init__ consumes: []
myapp-6  | 2025-03-12 17:21:24,333 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:101:__init__ produces: ['application/json']
myapp-6  | 2025-03-12 17:21:24,333 DEBUG /venv/lib/python3.13/site-packages/connexion/middleware/security.py:58:_get_verification_fn ... Security: None
myapp-6  | 2025-03-12 17:21:24,333 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:100:__init__ consumes: []
myapp-6  | 2025-03-12 17:21:24,334 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:101:__init__ produces: ['application/json']
myapp-6  | 2025-03-12 17:21:24,334 DEBUG /venv/lib/python3.13/site-packages/connexion/middleware/security.py:58:_get_verification_fn ... Security: None
myapp-6  | 2025-03-12 17:21:24,334 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:100:__init__ consumes: ['application/json']
myapp-6  | 2025-03-12 17:21:24,334 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:101:__init__ produces: []
myapp-6  | 2025-03-12 17:21:24,334 DEBUG /venv/lib/python3.13/site-packages/connexion/middleware/security.py:58:_get_verification_fn ... Security: None
myapp-6  | 2025-03-12 17:21:24,334 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:100:__init__ consumes: []
myapp-6  | 2025-03-12 17:21:24,334 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:101:__init__ produces: []
myapp-6  | 2025-03-12 17:21:24,334 DEBUG /venv/lib/python3.13/site-packages/connexion/middleware/security.py:58:_get_verification_fn ... Security: None
myapp-6  | 2025-03-12 17:21:24,334 DEBUG /venv/lib/python3.13/site-packages/connexion/middleware/abstract.py:89:add_paths Adding /openapi/pets...
myapp-6  | 2025-03-12 17:21:24,334 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:100:__init__ consumes: []
myapp-6  | 2025-03-12 17:21:24,334 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:101:__init__ produces: ['application/json']
myapp-6  | 2025-03-12 17:21:24,334 DEBUG /venv/lib/python3.13/site-packages/connexion/middleware/abstract.py:89:add_paths Adding /openapi/pets/{pet_id}...
myapp-6  | 2025-03-12 17:21:24,334 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:100:__init__ consumes: []
myapp-6  | 2025-03-12 17:21:24,334 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:101:__init__ produces: ['application/json']
myapp-6  | 2025-03-12 17:21:24,335 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:100:__init__ consumes: ['application/json']
myapp-6  | 2025-03-12 17:21:24,335 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:101:__init__ produces: []
myapp-6  | 2025-03-12 17:21:24,335 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:100:__init__ consumes: []
myapp-6  | 2025-03-12 17:21:24,335 DEBUG /venv/lib/python3.13/site-packages/connexion/operations/openapi.py:101:__init__ produces: []
myapp-6  | 2025-03-12 17:21:24,335 INFO /venv/lib/python3.13/site-packages/connexion/middleware/swagger_ui.py:80:add_openapi_json Adding spec json: /openapi/openapi.json
myapp-6  | 2025-03-12 17:21:24,335 DEBUG /venv/lib/python3.13/site-packages/connexion/middleware/swagger_ui.py:98:add_openapi_yaml Adding spec yaml: /openapi//openapi.yaml
myapp-6  | 2025-03-12 17:21:24,335 DEBUG /venv/lib/python3.13/site-packages/connexion/middleware/swagger_ui.py:127:add_swagger_ui Adding swagger-ui: /openapi/ui/
myapp-6  | INFO:     Application startup complete.
myapp-6  | INFO:     Uvicorn running on http://0.0.0.0:8081 (Press CTRL+C to quit)
```

Now open your browser and view the Swagger UI for these specification files:

* http://localhost:8080/openapi/ui/ for the OpenAPI 3 spec

