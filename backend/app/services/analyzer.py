from app.schemas.analysis import AnalysisResponse


def analyze_log(log: str) -> AnalysisResponse:
    log = log.lower()

    if "failed to start nginx" in log:
        return AnalysisResponse(
            status="warning",
            summary="The nginx service failed to start.",
            severity="medium",
            possible_causes=[
                "Configuration error",
                "Port 80 is already in use",
                "Permission issue"
            ],
            suggested_commands=[
                "systemctl status nginx",
                "journalctl -u nginx",
                "nginx -t"
            ]
        )

    if "out of memory" in log:
        return AnalysisResponse(
            status="critical",
            summary="System ran out of memory.",
            severity="high",
            possible_causes=[
                "RAM exhausted",
                "Memory leak",
                "Too many running processes"
            ],
            suggested_commands=[
                "free -h",
                "top",
                "htop"
            ]
        )

    if "permission denied" in log:
        return AnalysisResponse(
            status="warning",
            summary="Permission denied.",
            severity="medium",
            possible_causes=[
                "Missing permissions",
                "Wrong file owner",
                "SELinux or AppArmor restrictions"
            ],
            suggested_commands=[
                "ls -l",
                "chmod",
                "chown"
            ]
        )

    if "no space left on device" in log:
        return AnalysisResponse(
            status="critical",
            summary="Disk is full.",
            severity="high",
            possible_causes=[
                "Filesystem is full",
                "Large log files",
                "Too many temporary files"
            ],
            suggested_commands=[
                "df -h",
                "du -sh *",
                "journalctl --vacuum-time=7d"
            ]
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
        ]
    )