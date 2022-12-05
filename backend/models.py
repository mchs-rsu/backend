from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship

from backend.database import Base, engine


class District(Base):
    __tablename__ = 'districts'

    uid = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    sirens = relationship('Siren')
    __table_args__ = (
        UniqueConstraint('name', name='district_name_uniq'),
    )


class Siren(Base):
    __tablename__ = 'sirens'

    uid = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    district_id = Column(Integer, ForeignKey('districts.uid'), nullable=False)
    type = Column(String, nullable=False)
    own = Column(String)
    engineer = Column(String)
    date = Column(String)
    condition = Column(String)
    ident = Column(String, nullable=False)
    ip = Column(String, nullable=False)
    mask = Column(String)
    gateway = Column(String)
    adress = Column(String)
    geo = Column(String)
    comment = Column(String)
    photo = Column(String)
    disabled = Column(Integer)


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
