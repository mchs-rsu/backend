from backend.disticts.schemas import District as DistrictSchema
from backend.database import db_session
from backend.models import District
from backend.errors import NotFoundError, ConflictError

from sqlalchemy.exc import IntegrityError


class WebStorage():
    def add(self, district: DistrictSchema) -> DistrictSchema:
        entity = District(name=district.name)

        try:
            db_session.add(entity)
            db_session.commit()
        except IntegrityError:
            raise ConflictError(self.name)

        return DistrictSchema(uid=entity.uid, name=entity.name)


    def update(self, uid: int, district: DistrictSchema) -> DistrictSchema:
        entity = District.query.get(uid)

        if not entity:
            raise NotFoundError(self.name, uid)

        entity.name = district.name
        db_session.commit()

        return DistrictSchema(uid=entity.uid, name=entity.name)


    def delete(self, uid: int) -> None:
        entity = District.query.get(uid)

        if not entity:
            raise NotFoundError(self.name, uid)

        db_session.delete(entity)
        db_session.commit()


    def get_all(self) -> list[DistrictSchema]:
        entities = District.query.all()
        all_districts = []

        for entity in entities:
            district = DistrictSchema(uid=entity.uid, name=entity.name)
            all_districts.append(district)

        return all_districts


    def get_by_id(self, uid: int) -> DistrictSchema:
        entity = District.query.get(uid)

        if not entity:
            raise NotFoundError(self.name, uid)

        return DistrictSchema(uid=entity.uid, name=entity.name)


    def get_by_name(self, name: str) -> list[DistrictSchema]:
        search = '%{name}%'.format(name=name)
        entities = District.query.filter(District.name.ilike(search)).all()

        all_districts = []

        for entity in entities:
            district = DistrictSchema(uid=entity.uid, name=entity.name)
            all_districts.append(district)

        return all_districts
