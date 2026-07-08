from pydantic import BaseModel


class AnalysisRequest(BaseModel):
    log: str


class AnalysisResponse(BaseModel):
    status: str
    summary: str
    severity: str
    possible_causes: list[str]
    suggested_commands: list[str]