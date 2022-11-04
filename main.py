from fastapi import FastAPI
from pydantic import BaseModel

class SentenceRequest(BaseModel):
    sentence: str

app = FastAPI()

@app.post("/analyze")
async def analyze(request: SentenceRequest):
    return {"ret": request.sentence}
