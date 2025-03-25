from fastapi import FastAPI
from models.prompt import PromptRequest
from generators.content_generator import ContentGeneratorAPI
from uvicorn import run

app = FastAPI()
contet_generator = ContentGeneratorAPI()

@app.post("/generate_script")
async def generate_script(prompt_request: PromptRequest):

    roteiro = contet_generator.generate_text(prompt_request.prompt, prompt_request.style, prompt_request.model)
    return {"roteiro": roteiro}

@app.post("/set_ia/{ia}")
async def set_ia(ia: str):
    contet_generator.set_ia(ia)
    return {"ia": ia}
@app.post("/set_style/{style}")
async def set_style(style: str):
    contet_generator.set_style(style)
    return {"style": style}



if __name__ == "__main__":
    run("main:app", host="0.0.0.0", port=8000, reload=True)
