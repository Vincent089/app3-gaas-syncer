We are building a small but yet scalable CRUD service 

# Tech Stack
Python, Flask, SQLAlchemy, Marshmallow

# Design principles
Layered modular Architecture inspired by DDD, RESTful Architecture

1. main.py = entrypoint(s)
2. api.py + schema.py = transport layer
3. service.py = service layer
4. uow.py = service layer. Binds data access layer to service layer for better separation and testability
5. repository.py + db.py = data access layer
6. models.py = domain

# Guidelines
1. Don't assume. Don't hide confusion. Surface tradeoffs
2. Minimum code that solves the problem. Nothing speculative
3. Touch only what you must. Clean up only your own mess
4. Define success criteria. Loop until verified

# Testability
Domain related test 
- pytest src/tests/unit

Integration related test
- pytest src/tests/integration