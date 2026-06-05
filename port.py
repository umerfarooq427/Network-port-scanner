# ============================================================
# port.py
# Represents a single scanned port
# OOP Concept: Encapsulation (private attributes + getters)
# ============================================================

class Port:

    def __init__(self, number, is_open, service):
        self.__number  = number
        self.__is_open = is_open
        self.__service = service

    # ── Getters ─────────────────────────────────────────────
    def get_number(self):
        return self.__number

    def is_open(self):
        return self.__is_open

    def get_service(self):
        return self.__service

    def get_status(self):
        return "OPEN" if self.__is_open else "CLOSED"

    # ── Nice display format ──────────────────────────────────
    def __str__(self):
        status = "OPEN  " if self.__is_open else "CLOSED"
        return f"  [{status}]  Port {self.__number:<6} →  {self.__service}"
