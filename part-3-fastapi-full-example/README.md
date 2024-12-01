1. The intent of this app structure is to make sure that your app can scale ( from code pov )
2. In parallel to this README.md file should go requirements.txt, Dockerfile, .dockerignore, .rull.toml, compose, Makefile etc.
3. You can just create a main.py and that's also fine if scope of your work is small
4. If unsure then follow this structure

# Part 3.1 - Setting up main structure
1. Keep api definition separate from utils / migrations / models / schemas etc.
2. We place api in src/api
3. You should ideally abstract out FastAPI app's creation under a callable ( called factory ) to perform any *init* related operations in that callable. Those *init* operations could be registering exception handlers, middlewares, startup, shutdown event handlers etc.
4. We can create this factory in [src.api.main:create_app](./src/api/main.py#L4)
5. We can create routers in [src.api.routers](./src/api/routers/__init__.py)
6. We can store schemas in [src.schemas](./src/schemas/__init__.py)
7. Schemas can be used to declare your API's contracts eg. request / response / external schemas for API resources
8. We can create common utilities in [src.common](./src/common/__init__.py) eg. settings, db utils etc.
9. All crud and ORM stuff can go into models [src.models](./src/models/__init__.py)
