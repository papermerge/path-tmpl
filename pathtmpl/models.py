import uuid
from pydantic import BaseModel


class Context(BaseModel):
    id: uuid.UUID
    title: str
    file_name: str
    category: str
    year: int
    month: int
    day: int
