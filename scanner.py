# ============================================================
# scanner.py
# Core scanning logic + QuickScanner and FullScanner
# OOP Concept: Encapsulation, Abstraction, Inheritance
# ============================================================

import socket
from port               import Port
from service_identifier import ServiceIdentifier

class Scanner:

    def __init__(self, target):
        self.__target     = target
        self.__service_id = ServiceIdentifier()
        self.__results    = []

    # ── Public: run the scan on a port range ─────────────────
    def run(self, start_port, end_port):
        self.__results = []
        total = end_port - start_port + 1
        done  = 0

        print(f"\n  Scanning {self.__target} (ports {start_port}–{end_port})...")
        print(f"  Please wait...\n")

        for port_num in range(start_port, end_port + 1):
            port = self.__check_port(port_num)
            self.__results.append(port)

            # Show progress every 100 ports
            done += 1
            if done % 100 == 0 or done == total:
                percent = int((done / total) * 100)
                print(f"  Progress: {percent}%  ({done}/{total} ports scanned)", end="\r")

        print()  # new line after progress
        return self.__results

    # ── Public: get all scanned results ──────────────────────
    def get_results(self):
        return self.__results

    # ── Public: get target IP ────────────────────────────────
    def get_target(self):
        return self.__target

    # ── Private: check if a single port is open ──────────────
    def __check_port(self, port_number):
        service = self.__service_id.identify(port_number)
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((self.__target, port_number))
            s.close()
            is_open = (result == 0)
        except Exception:
            is_open = False

        return Port(port_number, is_open, service)


# ============================================================
# QuickScanner — scans top 100 most common ports
# OOP Concept: Inheritance (extends Scanner)
# ============================================================

class QuickScanner(Scanner):

    def __init__(self, target):
        super().__init__(target)
        self.__start = 1
        self.__end   = 100

    def run(self):
        print("  [Quick Scan Mode] Scanning ports 1–100")
        return super().run(self.__start, self.__end)


# ============================================================
# FullScanner — scans all ports from 1 to 1000
# OOP Concept: Inheritance (extends Scanner)
# ============================================================

class FullScanner(Scanner):

    def __init__(self, target):
        super().__init__(target)
        self.__start = 1
        self.__end   = 1000

    def run(self):
        print("  [Full Scan Mode] Scanning ports 1–1000")
        return super().run(self.__start, self.__end)
