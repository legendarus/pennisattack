import json
def write_record(hscore):
    """Записывает рекорд"""
    file_name = "record.json"
    with open(file_name, "w") as f_obg:
        json.dump(hscore,f_obg)
def read_record():
    """Возвращает число рекорда"""
    file_name = "record.json"
    with open(file_name) as f_obg:
        hscore = json.load(f_obg)
    return hscore
