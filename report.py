# ============================================================
# report.py
# Collects scan results and prints the final report
# OOP Concept: Abstraction (display logic hidden inside)
# ============================================================

import datetime

class ScanReport:

    def __init__(self, target):
        self.__target    = target
        self.__results   = []
        self.__scan_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # ── Add a Port object to report ──────────────────────────
    def add_results(self, results):
        self.__results = results

    # ── Display the full report ──────────────────────────────
    def display(self):
        open_ports   = [p for p in self.__results if p.is_open()]
        closed_ports = [p for p in self.__results if not p.is_open()]

        print("\n  ══════════════════════════════════════")
        print("            SCAN REPORT               ")
        print("  ══════════════════════════════════════")
        print(f"  Target  : {self.__target}")
        print(f"  Time    : {self.__scan_time}")
        print(f"  Total   : {len(self.__results)} ports scanned")
        print("  ──────────────────────────────────────")

        # Show open ports first
        if open_ports:
            print(f"\n  OPEN PORTS ({len(open_ports)} found):\n")
            for port in open_ports:
                print(port)
        else:
            print("\n  No open ports found.")

        # Show closed ports
        if closed_ports:
            print(f"\n  CLOSED PORTS ({len(closed_ports)} found):\n")
            for port in closed_ports:
                print(port)

        # Summary at bottom
        print("\n  ──────────────────────────────────────")
        print(f"  Open   : {len(open_ports)}")
        print(f"  Closed : {len(closed_ports)}")
        print("  ══════════════════════════════════════\n")

    # ── Display only open ports (short summary) ──────────────
    def display_open_only(self):
        open_ports = [p for p in self.__results if p.is_open()]

        print("\n  ══════════════════════════════════════")
        print("         OPEN PORTS SUMMARY            ")
        print("  ══════════════════════════════════════")
        print(f"  Target : {self.__target}")
        print(f"  Time   : {self.__scan_time}")
        print("  ──────────────────────────────────────\n")

        if open_ports:
            for port in open_ports:
                print(port)
        else:
            print("  No open ports found.")

        print(f"\n  Total open : {len(open_ports)}")
        print("  ══════════════════════════════════════\n")
