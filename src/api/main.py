from fastapi import FastAPI
from .routes.scan import router as scan_router

app = FastAPI()

app.include_router(scan_router, prefix="/scan")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Security Scanner API"}
