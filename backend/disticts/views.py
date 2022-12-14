from flask import Blueprint, request

from backend.disticts.schemas import District
from backend.disticts.storage import WebStorage
from backend.errors import AppError
from backend.sirens.storage import WebStorage as SirenStorage


district_view = Blueprint('districts', __name__)

storage = WebStorage()
siren_storage = SirenStorage()


@district_view.post('/')
def add():
    payload = request.json

    if not payload:
        raise AppError('empty payload')

    payload['uid'] = -1

    district = District(**payload)
    district = storage.add(district)

    return district.dict(), 201


@district_view.get('/<int:uid>')
def get_by_id(uid):
    district = storage.get_by_id(uid)

    return district.dict(), 200


@district_view.delete('/<int:uid>')
def delete_district(uid):
    storage.delete(uid)

    return {}, 204


@district_view.put('/<int:uid>')
def update_by_id(uid):
    payload = request.json

    if not payload:
        raise('empty payload')

    payload['uid'] = uid
    district = District(**payload)
    district = storage.update(uid, district)

    return district.dict(), 200


@district_view.get('/')
def get_all(name=''):
    if 'name' in request.args:
        name = request.args.get('name')
        districts = storage.get_by_name(name)
    else:
        districts = storage.get_all()

    return [district.dict() for district in districts], 200


@district_view.get('/<int:uid>/sirens')
def get_all_sirens(uid, name=''):
    if 'name' in request.args:
        name = request.args.get('name')
        sirens = siren_storage.find_for_district(uid, name)
    else:
        sirens = siren_storage.get_for_district(uid)

    return [siren.dict() for siren in sirens], 200
