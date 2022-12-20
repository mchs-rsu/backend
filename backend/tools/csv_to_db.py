import csv
from typing import Any
from backend.database import db_session
from backend.models import District, Siren


def read_csv(filename: str) -> list[dict[str, Any]]:
    with open (filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=',')
        all_data = []
        for row in reader:
            all_data.append(row)

        return all_data


def get_unique_districts(data_list):
    districts = {}

    for row in data_list:
        district_name = row['district']
        if district_name not in districts:
            district = {'name': district_name}
            districts[district_name] = district

    return districts


def save_districts(districts):
    db_session.bulk_insert_mappings(District, districts.values(), return_defaults=True)
    db_session.commit()


def get_unique_sirens(data_list, districts):
    sirens = {}

    for row in data_list:
        district_name = row['district']
        siren_name = row['siren']

        if siren_name not in sirens:
            siren = {
                    'name': row['siren'],
                    'district_id': districts[district_name]['uid'],
                    'type': row['type'],
                    'own': row['own'],
                    'engineer': row['engineer'],
                    'date': row['date'],
                    'condition': row['condition'],
                    'ident': row['ident'],
                    'ip': row['ip'],
                    'mask': row['mask'],
                    'gateway': row['gateway'],
                    'adress': row['adress'],
                    'geo': row['geo'],
                    'comment': row['comment'],
                    'photo': row['photo'],
                    'disabled': row['disabled']
            }

            sirens[siren_name] = siren

    return sirens


def save_sirens(sirens):
    db_session.bulk_insert_mappings(Siren, sirens.values(), return_defaults=True)
    db_session.commit()
