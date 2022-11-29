from pydantic import BaseModel


class District(BaseModel):
    uid: int
    name: str
