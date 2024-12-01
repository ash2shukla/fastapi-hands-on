# 1. Rather than declaring your own BaseModel we can use pydantic that allows us to do SerDe and BaseModel
from pydantic import BaseModel


# 2. Create a validatable model for "Point"
class Point(BaseModel):
    x: float
    y: float


# 3. Create a point
p = Point(x=1.2, y=2.4)

# 4. Dump it to dicts
print(p.model_dump())

# 5. Or Dump it to json ( remember dict != json )
print(p.model_dump_json())

# 6. Load dict to this model
print(Point.model_validate({"x": 1, "y": 2}))

# 7. Or Load json to this model
print(Point.model_validate_json('{"x": 1, "y": 2}'))
