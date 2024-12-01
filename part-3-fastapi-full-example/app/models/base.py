from sqlalchemy.inspection import inspect
from sqlalchemy.orm import DeclarativeBase


# Use an explicit ORMBase so that common ORM behavior is easy to modify later on
# eg. this ORM base gives a pretty print to ORM objects
class ORMBase(DeclarativeBase):
    def __repr__(self):
        pk_fields = inspect(self.__class__).primary_key
        pk_repr = " ".join([f"{k.name}={getattr(self, k.name)}" for k in pk_fields])
        return f"<{self.__class__.__name__} {pk_repr}>"
