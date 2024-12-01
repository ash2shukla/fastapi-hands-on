# 1. SerDe and Validations in Python were ugly before [PEP 484](https://peps.python.org/pep-0484/)
# 2. Pre 3.5 times had packages like marshmallow which were used for this
# 3. To do serde and validations we need field level information
# 4. The only way to do it was assigning an object to these fields
# 5. Now we have annotations which gave rise to Pydantic and consequently a whole new type hints based ecosystem

# 6. Create a class Point with annotations
class Point:
    x: float
    y: float


# 7. Type hint information is available at runtime too !
print(Point.__annotations__)
