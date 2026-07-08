from pydantic import BaseModel


class AnalysisRequest(BaseModel):
    log: str


class AnalysisResponse(BaseModel):
    id: str
    category: str
    confidence: float

    status: str
    summary: str
    severity: str

    possible_causes: list[str]
    suggested_commands: list[str]