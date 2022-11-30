from backend.disticts.schemas import District as DistrictSchema
from backend.database import db_session
from backend.models import District


class Storage():
    def add(self, district: DistrictSchema) -> DistrictSchema:
        entity = District(name=district)

        db_session.add(entity)
        db_session.commit()

        return DistrictSchema(uid=entity.uid, name=entity.name)


    def update(self, uid: int, district: DistrictSchema) -> DistrictSchema:
        entity = District.query.get(uid)

        if not entity:
            """здесь будет raise ошибки not found"""

        entity.name = district.name
        db_session.commit()

        return DistrictSchema(uid=entity.uid, name=entity.name)


    def delete(self, uid: int) -> None:
        entity = District.query.get(uid)

        if not entity:
            """здесь будет raise ошибки not found"""

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
            """здесь будет raise ошибки not found"""

        return DistrictSchema(uid=entity.uid, name=entity.name)


    def get_by_name(self, name: str) -> list[DistrictSchema]:
        search = '%name%'.format(name=name)
        entities = District.query.filter(District.name.ilike(search)).all()

        all_districts = []

        for entity in entities:
            district = DistrictSchema(uid=entity.uid, name=entity.name)

        return all_districts
