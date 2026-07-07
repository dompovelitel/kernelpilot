from fastapi import FastAPI

app = FastAPI(
    title="KernelPilot API",
    description="AI-powered Linux diagnostics",
    version="0.1.0",
)

@app.get("/")
def root():
    return {
        "name": "KernelPilot",
        "status": "running",
        "version": "0.1.0"
    }