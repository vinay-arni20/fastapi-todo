from pydantic import BaseModel

class Task(BaseModel):
    id: int
    title: str
    is_done: bool = False
