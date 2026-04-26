import json
from pathlib import Path


class ConfigReader:
    instance = None
    config = None

    def __new__(cls, config_path="config.json"):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.load_config(config_path)
        return cls.instance

    def load_config(self, config_path):
        path = Path(config_path)
        with path.open("r", encoding="utf-8") as file:
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

