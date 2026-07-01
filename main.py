# ============================================================
# main.py
# Entry point — runs the CLI menu for the port scanner
# OOP Concept: Abstraction (ties all classes together)
# ============================================================

from scanner import Scanner, QuickScanner, FullScanner
from report  import ScanReport

class PortScannerApp:

    # ── Display main menu ────────────────────────────────────
    def __show_menu(self):
        print("  ╔══════════════════════════════════════╗")
        print("  ║       📡 NETWORK PORT SCANNER        ║")
        print("  ╠══════════════════════════════════════╣")
        print("  ║  [1]  Quick Scan  (ports 1–100)      ║")
        print("  ║  [2]  Full Scan   (ports 1–1000)     ║")
        print("  ║  [3]  Custom Scan (you pick range)   ║")
        print("  ║  [4]  Exit                           ║")
        print("  ╚══════════════════════════════════════╝")

    # ── Get target IP from user ──────────────────────────────
    def __get_target(self):
        print("\n  Safe targets to scan:")
        print("  → 127.0.0.1       (your own PC)")
        print("  → 192.168.1.1     (your home router)")
        print("  → scanme.nmap.org (practice server)\n")
        target = input("  Enter target IP or hostname: ").strip()
        return target

    # ── Handle Quick Scan ────────────────────────────────────
    def __handle_quick_scan(self):
        target  = self.__get_target()
        scanner = QuickScanner(target)
        results = scanner.run()

        report = ScanReport(target)
        report.add_results(results)
        self.__show_report_options(report)

    # ── Handle Full Scan ─────────────────────────────────────
    def __handle_full_scan(self):
        target  = self.__get_target()
        scanner = FullScanner(target)
        results = scanner.run()

        report = ScanReport(target)
        report.add_results(results)
        self.__show_report_options(report)

    # ── Handle Custom Scan ───────────────────────────────────
    def __handle_custom_scan(self):
        target = self.__get_target()

        try:
            start = int(input("  Start port : ").strip())
            end   = int(input("  End port   : ").strip())

            if start < 1 or end > 65535 or start > end:
                print("\n  ❌ Invalid port range. Use 1–65535.\n")
                return

        except ValueError:
            print("\n  ❌ Please enter valid numbers.\n")
            return

        scanner = Scanner(target)
        results = scanner.run(start, end)

        report = ScanReport(target)
        report.add_results(results)
        self.__show_report_options(report)

    # ── Ask user which report view they want ─────────────────
    def __show_report_options(self, report):
        print("  How do you want to see results?")
        print("  [1]  Full report (open + closed)")
        print("  [2]  Open ports only")
        choice = input("\n  Enter choice: ").strip()

        if choice == "1":
            report.display()
        elif choice == "2":
            report.display_open_only()
        else:
            report.display()

    # ── Main run loop ────────────────────────────────────────
    def run(self):
        print("\n  Welcome to Network Port Scanner 📡\n")

        while True:
            self.__show_menu()
            choice = input("\n  Enter choice (1-4): ").strip()

            if   choice == "1": self.__handle_quick_scan()
            elif choice == "2": self.__handle_full_scan()
            elif choice == "3": self.__handle_custom_scan()
            elif choice == "4":
                print("\n  Goodbye! 📡\n")
                break
            else:
                print("\n  ❌ Invalid choice. Enter 1-4.\n")


# ── Entry point ──────────────────────────────────────────────
if __name__ == "__main__":
    app = PortScannerApp()
    app.run()
