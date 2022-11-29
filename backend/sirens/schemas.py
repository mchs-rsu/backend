from pydantic import BaseModel


class Siren(BaseModel):
    uid: int
    name: str
    district_id: int
    type: str
    own: str | None
    engineer: str | None
    date: str | None
    condition: str | None
    ident: str
    ip: str
    mask: str | None
    gateway: str | None
    adress: str | None
    geo: str | None
    comment: str | None
    photo: str | None
