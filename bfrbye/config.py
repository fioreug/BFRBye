import yaml
from pathlib import Path

CONFIG_FILE = Path("config.yaml")

default_config = {
    "storage": {
        "method": "csv",   # options: "csv", "txt", "notion"
        "output_file": "output.csv"
    },
    "notion": {
        "database_id": "",
        "token": ""
    }
}

def load_config():
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, "r") as f:
            return yaml.safe_load(f)
    return default_config

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        yaml.safe_dump(config, f)
