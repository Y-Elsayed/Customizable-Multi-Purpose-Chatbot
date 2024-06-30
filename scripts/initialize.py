import os
import json

def load_config(config_file="../config/config.json"):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, config_file)
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config

def save_config(config_data, config_file="../config/config.json"):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, config_file)
    with open(config_path, "w") as f:
        json.dump(config_data, f, indent=4)

def create_file(file_path, file_name):
    # Ensure file_path ends with a separator
    data_dir = os.path.join(file_path, "")

    json_path = os.path.join(data_dir, file_name)

    # Create directories if they don't exist
    os.makedirs(data_dir, exist_ok=True)

    # Check if the file already exists
    if os.path.isfile(json_path):
        print(f"File '{json_path}' already exists.")
        return True

    try:
        with open(json_path, "w+") as f:
            # File created successfully, do nothing
            print(f"File '{json_path}' created successfully.")
            return True
    except IOError as e:
        print(f"Error creating file '{json_path}': {e}")
        return False

def initialize(data_json_name="data.json", database_name="chatbot_database.sqlite"):
    config_json = load_config()

    # Ensure data_dir exists and is correctly set
    data_dir = config_json.get(
        "data_dir", "../data/"
    )  # Default value if not specified in config
    data_dir = os.path.abspath(data_dir)  # Convert to absolute path

    os.makedirs(data_dir, exist_ok=True)  # Ensure data_dir exists

    # Create data JSON file
    data_json_path = os.path.join(data_dir, data_json_name)
    if create_file(data_dir, data_json_name):
        config_json["data_json_name"] = data_json_name
        config_json["data_json_path"] = data_json_path

    # Create database file
    database_path = os.path.join(data_dir, database_name)
    if create_file(data_dir, database_name):
        config_json["database_name"] = database_name
        config_json["database_path"] = database_path

    # Save updated config back to file
    save_config(config_json)


initialize()