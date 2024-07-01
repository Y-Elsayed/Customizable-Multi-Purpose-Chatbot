import json
import os


def file_exists(file_path):
    return os.path.exists(file_path)


def write_json_to_file(file_path, json_obj, create_new_when_not_found=True):
    if not file_exists(file_path):
        if create_new_when_not_found:
            create_file(file_path, json.dumps(json_obj))
            print(f"File '{file_path}' created successfully.")
        else:
            print(f"File '{file_path}' not found.")
            return

    try:
        with open(file_path, "w") as f:
            json.dump(json_obj, f)
    except IOError as e:
        print(f"Error writing to file '{file_path}': {e}")


def read_json_from_file(file_path):
    if not file_exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return None

    try:
        with open(file_path, "r") as f:
            json_obj = json.load(f)
        return json_obj
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from file '{file_path}': {e}")
        return None
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}")


def create_file(file_path, content=""):
    try:
        with open(file_path, "w") as f:
            f.write(content)
    except IOError as e:
        print(f"Error creating file '{file_path}': {e}")
