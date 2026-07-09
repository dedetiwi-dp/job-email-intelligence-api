from fastapi import FastAPI
from app.api.extract import router

app = FastAPI(
    title="Job Email Intelligence API",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "Job Email Intelligence API is running!"
    }