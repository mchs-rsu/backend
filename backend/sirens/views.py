from flask import Blueprint, request

from backend.sirens.storage import WebStorage
from backend.sirens.schemas import Siren
from backend.errors import AppError


siren_view = Blueprint('sirens', __name__)

storage = WebStorage()


@siren_view.post('/')
def add():
    payload = request.json

    if not payload:
        raise AppError('empty payload')

    payload['uid'] = -1

    siren = Siren(**payload)
    siren = storage.add(siren)

    return siren.dict(), 201


@siren_view.get('/<int:uid>')
def get_by_id(uid):
    siren = storage.get_by_id(uid)

    return siren.dict(), 200


@siren_view.put('/<int:uid>')
def update_by_id(uid):
    payload = request.json

    if not payload:
        raise AppError('empty payload')

    payload['uid'] = uid
    siren = Siren(**payload)
    siren = storage.update(uid, siren)

    return siren.dict(), 200


@siren_view.delete('/<int:uid>')
def delete_by_id(uid):
    storage.delete(uid)

    return {}, 204


@siren_view.get('/')
def get_by_name(name=''):
    if 'name' in request.args:
        name = request.args.get('name')
        sirens = storage.get_by_name(name)
    else:
        sirens = []

    return [siren.dict() for siren in sirens], 200
