from .db import Base, engine
from .models import *


def init_db():
    Base.metadata.create_all(engine)