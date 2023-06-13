import json


def save_to_json(filename, data):
    if filename and data:
        with open(filename, 'w', encoding='UTF-8') as f:
            json.dump(data, f, indent=4)
