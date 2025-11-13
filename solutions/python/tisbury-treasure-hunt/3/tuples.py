"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    return record[1]


def convert_coordinate(coordinate):
    return tuple([coordinate[0],coordinate[1]])


def compare_records(azara_record, rui_record):
    rui_coord = "".join(rui_record[1])
    if azara_record[1] == rui_coord:
        return True

    return False


def create_record(azara_record, rui_record):
    if (compare_records(azara_record, rui_record)) == True:
        return azara_record + rui_record
    return "not a match"


def clean_up(combined_record_group):
    report = ""
    for item in combined_record_group:
        report += (f"('{item[0]}', '{item[2]}', {item[3]}, '{item[4]}')\n")
    return report

