#from api.deepseek_api import DeepSeekAPI
from api.openai_api import OpenAIAPI
from api.deepseek_api import DeepSeekAPI


class ContentGeneratorAPI:
    def __init__(self):
        self.current_api = "gpt"
        self.current_style = "cartomante"
        self.openai_api = OpenAIAPI()
        self.deepseek_api = DeepSeekAPI()

    def set_ia(self, ia: str):
        if ia in {"gpt", "deepseek"}:
            self.current_api = ia

    def set_style(self, style: str):
        if style in {"cartomante", "poet"}:
            self.current_style = style

    def generate_text(self, prompt: str, style: str, model: str):
        if self.current_api == "gpt":
            return self.openai_api.generate_text(prompt, style, model)
        else:
            return self.deepseek_api.generate_text(prompt, style, model)
