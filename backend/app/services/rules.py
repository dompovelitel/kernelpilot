RULES = [
    {
        "pattern": "failed to start nginx",
        "status": "warning",
        "summary": "The nginx service failed to start.",
        "severity": "medium",
        "possible_causes": [
            "Configuration error",
            "Port 80 is already in use",
            "Permission issue"
        ],
        "suggested_commands": [
            "systemctl status nginx",
            "journalctl -u nginx",
            "nginx -t"
        ]
    },
    {
        "pattern": "out of memory",
        "status": "critical",
        "summary": "System ran out of memory.",
        "severity": "high",
        "possible_causes": [
            "RAM exhausted",
            "Memory leak",
            "Too many running processes"
        ],
        "suggested_commands": [
            "free -h",
            "top",
            "htop"
        ]
    },
    {
        "pattern": "permission denied",
        "status": "warning",
        "summary": "Permission denied.",
        "severity": "medium",
        "possible_causes": [
            "Missing permissions",
            "Wrong file owner",
            "SELinux or AppArmor restrictions"
        ],
        "suggested_commands": [
            "ls -l",
            "chmod",
            "chown"
        ]
    },
    {
        "pattern": "no space left on device",
        "status": "critical",
        "summary": "Disk is full.",
        "severity": "high",
        "possible_causes": [
            "Filesystem is full",
            "Large log files",
            "Too many temporary files"
        ],
        "suggested_commands": [
            "df -h",
            "du -sh *",
            "journalctl --vacuum-time=7d"
        ]
    }
]