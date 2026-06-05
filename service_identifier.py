# ============================================================
# service_identifier.py
# Maps port numbers to known service names
# OOP Concept: Abstraction (hides the mapping logic)
# ============================================================

class ServiceIdentifier:

    def __init__(self):
        # Common port → service name mapping
        self.__port_map = {
            21   : "FTP",
            22   : "SSH",
            23   : "Telnet",
            25   : "SMTP",
            53   : "DNS",
            67   : "DHCP",
            68   : "DHCP",
            80   : "HTTP",
            110  : "POP3",
            119  : "NNTP",
            123  : "NTP",
            143  : "IMAP",
            161  : "SNMP",
            194  : "IRC",
            443  : "HTTPS",
            445  : "SMB",
            3306 : "MySQL",
            3389 : "RDP",
            5432 : "PostgreSQL",
            5900 : "VNC",
            6379 : "Redis",
            8080 : "HTTP-ALT",
            8443 : "HTTPS-ALT",
            27017: "MongoDB",
        }

    # ── Get service name for a port number ───────────────────
    def identify(self, port_number):
        return self.__port_map.get(port_number, "Unknown")

    # ── Check if port number is a known service ──────────────
    def is_known(self, port_number):
        return port_number in self.__port_map
