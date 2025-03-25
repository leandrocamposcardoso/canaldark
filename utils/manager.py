import random
from .config_loader import load_config

class KeyManager():
    """docstring for KeyManager."""
    def __init__(self, service: str):
        config = load_config()
        self.keys = config.get(service, "keys").split(",")

    def get_key(self):
        return random.choice(self.keys)

class ModelManager():
    """docstring for ModelManager."""
    def __init__(self, service: str):
        config = load_config()
        self.models = config.get(service, "models").split(",")

    def get_models(self):
        return self.models

    def validate_model(self, model: str):
        return model if model in self.models else self.models[0]
