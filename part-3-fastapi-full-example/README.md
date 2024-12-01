1. The intent of this app structure is to make sure that your app can scale ( from code pov )
2. In parallel to this README.md file should go requirements.txt, Dockerfile, .dockerignore, .rull.toml, compose, Makefile etc.
3. You can just create a main.py and that's also fine if scope of your work is small
4. If unsure then follow this structure
5. We build an API that looks like this-
   1. It deals with two resources called resource1, resource2
   2. Both resources have two attributes attr1, attr2
   3. resource1 does not have any database table associated with it
   4. resource2's data is backed by some database table

# Part 3.1 - Setting up main structure ( Making API work for resource1 )
1. Keep api definition separate from utils / migrations / models / schemas etc.
2. We place api in app/api
3. You should ideally abstract out FastAPI app's creation under a callable ( called factory ) to perform any *init* related operations in that callable. Those *init* operations could be registering exception handlers, middlewares, startup, shutdown event handlers etc.
4. We can create this factory in [app.api.main:create_app](./app/api/main.py#L4)
5. We can create routers in [app.api.routers](./app/api/routers/__init__.py)
6. We can store schemas in [app.schemas](./app/schemas/__init__.py)
7. Schemas can be used to declare your API's contracts eg. request / response / external schemas for API resources
8. We can create common utilities in [app.common](./app/common/__init__.py) eg. settings, db utils etc.
9. All crud and ORM stuff can go into models [app.models](./app/models/__init__.py)

# Part 3.2 - Using SQLAlchemy ( Making API work for resource2 )
1. Create utilities to connect with DB in [app.common.db](./app/common/db.py)
2. Declare ORMs
   1. Declare base orm [app.models](./app/models/base.py)
   2. Declare ORM of resources in [app.models](./app/models/resource2.py)
3. Create migrations for these changes using alembic
   1. Create alembic ini, env.py and script py mako in [app.migrations](./app/migrations)
   2. Run migrations creation command `alembic -c app/migrations/alembic.ini --autogenerate -m "message"`
   3. Apply migrations `alembic -c app/migrations/alembic.ini upgrade head`
4. Declare model methods in [app.models](./app/models/resource2.py)
5. Use these model methods in [app.routers](./app/models/resource2.py)
6. We see some typing issues with returns and using sqlalchemy in general is a little cumbersome

# Part 3.3 - Using SQLModel
1. Declare same Resource2ORM but with SQLModel base class
2. We dont need to use mapped_column / Mapped etc. and syntax looks much cleaner
3. Its fully backwards compatible with sqlalchemy as its built on top of it so everything else can stay the same
4. Or we can change it to sqlmodel specific methods

# Part 3.4 - Using middlewares
1. What if we want to handle CORS or Compress traffic with gzip ? We can use inbuilt middlewares
2. We can do some pre and post request magic with custom middlewares as well like recording request time or doing logging
3. We can register middlewares in our app factory [app.api.main](./app/api/main.py)

# Part 3.5 - Using Authentication
1. FastAPI out of the box provides methods to setup OAuth2 authentication and We can add this logic on certain endpoints
2. Create token endpoint where we will get grant_type, username, password etc. [app.api.routers.token](./app/api/routers/token.py) This endpoint will decide if the authentication request is correct or not and will return a token
3. Add corresponding token decoding logic and getting current user logic in a dependency. [app.api.auth](./app/api/auth.py)
4. Use this token decoding logic as a dependency on protected endpoints eg. [app.api.routers.resource2](./app/api/routers/resource2.py)

# Part 3.6 - Exception Handling
1. Create exception handlers at [app.api.routers.main](./app/api/main.py)
2. These can be registered based on exception type or based on HTTP status code
3. These are helpful to translate 500s to more helpful errors

# Part 3.7 - Testing
1. We can use fastapi testclient to stub the api responses
2. Create test client as a fixture [test.conftest](./tests/conftest.py)
3. Use the fixture to write stubbed tests for your api [test.test_resource1](./tests/test_resource1.py)
