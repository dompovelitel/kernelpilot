print("ANALYZE.PY LOADED")
from fastapi import APIRouter

from app.schemas.analysis import AnalysisRequest
from app.services.analyzer import analyze_log

router = APIRouter(prefix="/api", tags=["Analysis"])


@router.post("/analyze")
def analyze(request: AnalysisRequest):
    return analyze_log(request.log)