from openai import OpenAI
from utils.manager import KeyManager, ModelManager

class OpenAIAPI:
    def __init__(self):
        self.key_manager = KeyManager("OpenAI")
        self.model_manager = ModelManager("OpenAI")

    def generate_text(self, prompt: str, style: str, model: str):
        key = self.key_manager.get_key()
        model = self.model_manager.validate_model(style)
        client = OpenAI(api_key=key)
        try:
            response = client.completions.create(
                model=model,
                prompt=f"{style}: {prompt}",
                max_tokens=100
            )
            return response.choicies[0].text
        except Exception as e:
            return "Quota atingida"

