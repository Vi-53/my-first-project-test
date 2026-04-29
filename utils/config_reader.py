import json
from pathlib import Path


class ConfigReader:
    _instances = {}

    def __new__(cls, config_path="config.json"):
        config_path = Path(config_path).resolve()

        if config_path not in cls._instances:
            instance = super().__new__(cls)
            instance._load_config(config_path)
            cls._instances[config_path] = instance
        return cls._instances[config_path]

    def _load_config(self, config_path):
        with open(config_path, "r", encoding="utf-8") as file:
            self.config = json.load(file)

    @property
    def base_url(self):
        return self.config["base_url"]

    @property
    def browser(self):
        return self.config["browser"]

    @property
    def timeout(self):
        return self.config["timeout"]

    @property
    def headless(self):
        return self.config["headless"]

