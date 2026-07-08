from app.schemas.analysis import AnalysisResponse
from app.services.rules import RULES


def analyze_log(log: str) -> AnalysisResponse:
    log = log.lower()

    for rule in RULES:
        if rule["pattern"] in log:
            return AnalysisResponse(
                status=rule["status"],
                summary=rule["summary"],
                severity=rule["severity"],
                possible_causes=rule["possible_causes"],
                suggested_commands=rule["suggested_commands"],
            )

    return AnalysisResponse(
        status="unknown",
        summary="No known issue detected.",
        severity="low",
        possible_causes=[
            "Unknown log message"
        ],
        suggested_commands=[
            "Check the full system log"
        ],
    )