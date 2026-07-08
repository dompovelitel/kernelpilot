print("MAIN.PY LOADED")
from fastapi import FastAPI

from app.api.analyze import router as analyze_router

app = FastAPI(
    title="KernelPilot API",
    description="AI-powered Linux diagnostics",
    version="0.1.0",
)

app.include_router(analyze_router)


@app.get("/")
def root():
    return {
        "name": "KernelPilot",
        "status": "running",
        "version": "0.1.0",
    }