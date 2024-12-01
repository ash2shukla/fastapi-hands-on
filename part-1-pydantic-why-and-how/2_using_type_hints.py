# 1. We can use this information to do some stuff like validation
class ValidationError(Exception): ...


class BaseValidator:
    """A very basic implementation of an annotation based validator"""

    def __init__(self, **kwargs):
        for k, v in self.__annotations__.items():
            val = kwargs.get(k)
            if not isinstance(val, v):
                raise ValidationError(f"{k} should be {v} but is {type(val)}")


class Point(BaseValidator):
    x: float
    y: float


# 2. now it raises ValidatonError if x or y is not of correct type
Point(x="a", b=2.1)

# 3. Pydantic v2 is much faster than v1 due to implementation is rust.
# 4. Check https://github.com/pydantic/pydantic/blob/main/pydantic/v1/main.py#L178 for deeper dive into How Pydantic v1 did it
