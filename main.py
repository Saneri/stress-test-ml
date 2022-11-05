from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from analyzer import analyzeStress
class RequestPayload(BaseModel):
    messageList: list[str]

app = FastAPI()

@app.post("/analyze")
async def analyze(request: RequestPayload): 
    if not len(request.messageList):
        raise HTTPException(status_code=422, detail="Empty list in request payload")
    stressValues = analyzeStress(request.messageList)
    return {"stressValues": stressValues}
