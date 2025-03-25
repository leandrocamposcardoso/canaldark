from utils.manager import KeyManager, ModelManager
from openai import OpenAI

class DeepSeekAPI:
    def __init__(self):
        self.key_manager = KeyManager("DeepSeek")
        self.model_manager = ModelManager("DeepSeek")

    def generate_text(self, prompt: str, style: str, model: str):
        key = self.key_manager.get_key()
        model = self.model_manager.validate_model(style)
        client = OpenAI(api_key="<DeepSeek API Key>", base_url="https://api.deepseek.com")
        response = client.completions.create(
            model=model,
            prompt=f"{style}: {prompt}",
            max_tokens=100
        )
        return response.choices[0].text

