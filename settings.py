import json
import os

SETTING_DIR = "./.settings"


def load_config(filename="config.json"):
    directory = os.path.dirname(SETTING_DIR)
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

    try:
        filename = os.path.join(SETTING_DIR, filename)
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"{filename} 파일이 존재하지 않습니다.")
        return {}


def save_config(config, filename="config.json"):
    directory = os.path.dirname(SETTING_DIR)
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

    current_config = load_config(filename)
    updated_config = {**current_config, **config}

    filename = os.path.join(SETTING_DIR, filename)
    with open(filename, "w") as file:
        json.dump(updated_config, file, indent=4)
