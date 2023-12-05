import csv
import re
from checksum import serialize_result, calculate_checksum

PATTERN = {
    "telephone": r"^\+7-\(\d{3}\)-\d{3}-\d{2}-\d{2}$",
    "http_status_message": r"^\d{3}\s[a-zA-Z0-9_ ]{1,}$",
    "shils": r"^\d{11}$",
    "identifier": r"^\d{2}-\d{2}/\d{2}$",
    "ip_v4": r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",
    "longitude": r"^-? \d{1,3} \. \d+$",
    "blood_type": r"^(?: AB | A | B | O) [+\u2212]$",
    "isbn": r"^\d+-\d+-\d+-\d+(:?-\d+)?$",
    "locale_code": r"^[a-z]{2} (-[a-z]{2})?$",
    "date": r"^\d{4}-\d{2}-\d{2}$"
}


def read_csv(file_name) -> list:
    '''Читаем csv-файл и записываем его в список'''
    data = []
    with open(file_name, "r", newline="", encoding="utf-16") as file:
        reader = csv.reader(file, delimiter=";")
        for i in reader:
            data.append(i)
        data.pop(0)
        return data

if __name__ == "__main__":
    variant = 42
    file_name = "42.csv"
    read_csv(file_name)
