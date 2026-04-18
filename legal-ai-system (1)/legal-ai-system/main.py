from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Legal AI System", version="0.1.0")
app.include_router(router)


@app.get("/")
def root() -> dict:
    return {"message": "Legal AI Content System is running."}
