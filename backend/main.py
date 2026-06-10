from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from schemas import PredictRequest
from combine_service import predict_combined

app = FastAPI(
    title="Mental Health Detection API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Mental Health API running 🚀"}

@app.post("/predict")
def predict(request: PredictRequest):

    try:
        return predict_combined(
            request.model_dump()
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )