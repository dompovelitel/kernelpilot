RULES = [
    {
        "id": "NGINX_START_FAILED",
        "category": "systemd",
        "pattern": "failed to start nginx",
        "status": "warning",
        "severity": "medium",
        "confidence": 0.99,
        "summary": "The nginx service failed to start.",
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
        "id": "OUT_OF_MEMORY",
        "category": "memory",
        "pattern": "out of memory",
        "status": "critical",
        "severity": "high",
        "confidence": 0.98,
        "summary": "System ran out of memory.",
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
        "id": "PERMISSION_DENIED",
        "category": "permissions",
        "pattern": "permission denied",
        "status": "warning",
        "severity": "medium",
        "confidence": 0.97,
        "summary": "Permission denied.",
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
        "id": "DISK_FULL",
        "category": "storage",
        "pattern": "no space left on device",
        "status": "critical",
        "severity": "high",
        "confidence": 0.99,
        "summary": "Disk is full.",
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