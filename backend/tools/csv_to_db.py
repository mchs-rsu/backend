import csv
from typing import Any
from backend.database import db_session
from backend.models import District, Siren


def read_csv(filename: str) -> list[dict[str, Any]]:
    with open (filename, 'r', encoding='utf-8') as file:
        fields = ['name, ']
        reader = csv.DictReader(file, fields, delimiter=',')
        all_data = []
        for row in reader:
            all_data.append(row)

        return all_data
