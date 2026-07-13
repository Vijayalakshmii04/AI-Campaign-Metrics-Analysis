from fastapi import FastAPI
from app.api.analysis import router as analysis_router

app = FastAPI(
    title="Campaign Decision Assistant"
)

app.include_router(
    analysis_router,
    prefix="/api/v1"
)


@app.get("/")
def root():
    return {
        "message": "working"
    }