import json
import os

config_file = os.path.join(os.path.dirname(__file__), "config.json")

default_config = {
    "application": {
        "name": "Student Registration System",
        "version": "1.0.0"
    },
    "settings": {
        "theme": "light",
        "language": "English",
        "max_students": 100,
        "notifications": True
    }
}

try:
    with open(config_file, "r", encoding="utf-8") as file:
        config = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    config = default_config
    print("Configuration file is missing or invalid. Using default configuration.")

print("Application:", config["application"]["name"])
print("Version:", config["application"]["version"])
print("Theme:", config["settings"]["theme"])
print("Language:", config["settings"]["language"])
print("Maximum Students:", config["settings"]["max_students"])
print("Notifications:", config["settings"]["notifications"])

config["settings"]["theme"] = "dark"

with open(config_file, "w", encoding="utf-8") as file:
    json.dump(config, file, indent=4)

print("Configuration updated successfully.")
print("New theme:", config["settings"]["theme"])