from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

model = joblib.load('model.pkl')
cv = joblib.load('cv.pkl')

class RequestPayload(BaseModel):
    messageList: list[str]

app = FastAPI()

@app.post("/analyze")
async def analyze(request: RequestPayload): 
    if not len(request.messageList):
        raise HTTPException(status_code=422, detail="Empty list in request payload")
    results = model.predict(cv.transform(request.messageList).toarray())
    resultsList = [int(x) for x in results]
    # stressAverage = float(np.average(results))
    return {"stressAverage": resultsList}
