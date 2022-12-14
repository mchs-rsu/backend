from backend.models import Siren, District
from backend.database import db_session
from backend.sirens.schemas import Siren as SirenSchema
from backend.errors import ConflictError, NotFoundError

from sqlalchemy.exc import IntegrityError


class WebStorage():
    name = 'sirens'

    def add(self, siren: SirenSchema) -> SirenSchema:
        entity = Siren(
                name=siren.name,
                district_id=siren.district_id,
                type=siren.type,
                own=siren.own,
                engineer=siren.engineer,
                date=siren.date,
                condition=siren.condition,
                ident=siren.ident,
                ip=siren.ip,
                mask=siren.mask,
                gateway=siren.gateway,
                adress=siren.adress,
                geo=siren.geo,
                comment=siren.comment,
                photo=siren.photo,
                disabled=siren.disabled,
        )

        try:
            db_session.add(entity)
            db_session.commit()
        except IntegrityError:
            raise ConflictError(self.name)

        return SirenSchema(
                uid=entity.uid,
                name=entity.name,
                district_id=entity.district_id,
                type=entity.type,
                own=entity.own,
                engineer=entity.engineer,
                date=entity.date,
                condition=entity.condition,
                ident=entity.ident,
                ip=entity.ip,
                mask=entity.mask,
                gateway=entity.gateway,
                adress=entity.adress,
                geo=entity.geo,
                comment=entity.comment,
                photo=entity.photo,
                disabled=entity.disabled,
        )


    def update(self, uid: int, siren: SirenSchema) -> SirenSchema:
        entity = Siren.query.get(uid)

        if not entity:
            raise NotFoundError(self.name, uid)

        entity.name=siren.name
        entity.district_id=siren.district_id
        entity.type=siren.type
        entity.own=siren.own
        entity.engineer=siren.engineer
        entity.date=siren.date
        entity.condition=siren.condition
        entity.ident=siren.ident
        entity.ip=siren.ip
        entity.mask=siren.mask
        entity.gateway=siren.gateway
        entity.adress=siren.adress
        entity.geo=siren.geo
        entity.comment=siren.comment
        entity.photo=siren.photo
        entity.disabled=siren.disabled

        db_session.commit()

        return SirenSchema(
            uid=entity.uid,
            name=entity.name,
            district_id=entity.district_id,
            type=entity.type,
            own=entity.own,
            engineer=entity.engineer,
            date=entity.date,
            condition=entity.condition,
            ident=entity.ident,
            ip=entity.ip,
            mask=entity.mask,
            gateway=entity.gateway,
            adress=entity.adress,
            geo=entity.geo,
            comment=entity.comment,
            photo=entity.photo,
            disabled=entity.disabled,
        )


    def delete(self, uid: int) -> None:
        entity = Siren.query.get(uid)

        if not entity:
            raise NotFoundError(self.name, uid)

        db_session.delete(entity)
        db_session.commit()


    def get_by_id(self, uid: int) -> SirenSchema:
        entity = Siren.query.get(uid)

        if not entity:
            raise NotFoundError(self.name, uid)

        return SirenSchema(
                uid=entity.uid,
                name=entity.name,
                district_id=entity.district_id,
                type=entity.type,
                own=entity.own,
                engineer=entity.engineer,
                date=entity.date,
                condition=entity.condition,
                ident=entity.ident,
                ip=entity.ip,
                mask=entity.mask,
                gateway=entity.gateway,
                adress=entity.adress,
                geo=entity.geo,
                comment=entity.comment,
                photo=entity.photo,
                disabled=entity.disabled,
        )


    def get_for_district(self, uid: int) -> list[SirenSchema]:
        district = District.query.get(uid)

        if not district:
            raise NotFoundError(self.name, uid)

        all_sirens = []

        entities = Siren.query.filter(Siren.district_id == uid).all()

        for entity in entities:
            siren = SirenSchema(
                uid=entity.uid,
                name=entity.name,
                district_id=entity.district_id,
                type=entity.type,
                own=entity.own,
                engineer=entity.engineer,
                date=entity.date,
                condition=entity.condition,
                ident=entity.ident,
                ip=entity.ip,
                mask=entity.mask,
                gateway=entity.gateway,
                adress=entity.adress,
                geo=entity.geo,
                comment=entity.comment,
                photo=entity.photo,
                disabled=entity.disabled,
            )

            all_sirens.append(siren)

        return all_sirens


    def get_by_name(self, name: str) -> list[SirenSchema]:
        search = '%{name}%'.format(name=name)
        entities = Siren.query.filter(Siren.name.ilike(search)).all()

        sirens_by_name = []

        for entity in entities:
            siren = SirenSchema(
                uid=entity.uid,
                name=entity.name,
                district_id=entity.district_id,
                type=entity.type,
                own=entity.own,
                engineer=entity.engineer,
                date=entity.date,
                condition=entity.condition,
                ident=entity.ident,
                ip=entity.ip,
                mask=entity.mask,
                gateway=entity.gateway,
                adress=entity.adress,
                geo=entity.geo,
                comment=entity.comment,
                photo=entity.photo,
                disabled=entity.disabled,
            )

            sirens_by_name.append(siren)

        return sirens_by_name


    def find_for_district(self, uid: int, name: str) -> list[SirenSchema]:
        search = '%{name}%'.format(name=name)
        entities = Siren.query.filter(
            Siren.district_id == uid,
            Siren.name.ilike(search),
        ).all()

        target_sirens = []

        for entity in entities:
            siren = SirenSchema(
                uid=entity.uid,
                name=entity.name,
                district_id=entity.district_id,
                type=entity.type,
                own=entity.own,
                engineer=entity.engineer,
                date=entity.date,
                condition=entity.condition,
                ident=entity.ident,
                ip=entity.ip,
                mask=entity.mask,
                gateway=entity.gateway,
                adress=entity.adress,
                geo=entity.geo,
                comment=entity.comment,
                photo=entity.photo,
                disabled=entity.disabled,
            )

            target_sirens.append(siren)

        return target_sirens
