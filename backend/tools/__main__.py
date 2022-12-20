from backend.tools.csv_to_db import read_csv, get_unique_sirens, get_unique_districts, save_districts, save_sirens


if __name__ == '__main__':
    actual_data = read_csv('.data/rsu.csv')

    districts = get_unique_districts(actual_data)
    save_districts(districts)

    sirens = get_unique_sirens(actual_data, districts)
    save_sirens(sirens)
