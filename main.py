# ============================================================
# main.py
# GUI version of Network Port Scanner using tkinter
# OOP Concept: Abstraction (all GUI logic inside App class)
# ============================================================

import tkinter as tk
from tkinter import ttk, messagebox
import threading
from scanner import Scanner, QuickScanner, FullScanner
from report  import ScanReport

class PortScannerApp:

    def __init__(self, root):
        self.root = root
        self.root.title("📡 Network Port Scanner")
        self.root.geometry("720x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#0D1117")

        self.__scanning = False
        self.__build_ui()

    # ── Build the full UI ────────────────────────────────────
    def __build_ui(self):
        self.__build_header()
        self.__build_input_section()
        self.__build_scan_button()
        self.__build_results_section()
        self.__build_status_bar()

    # ── Header ───────────────────────────────────────────────
    def __build_header(self):
        header = tk.Frame(self.root, bg="#161B22", pady=12)
        header.pack(fill="x")

        tk.Label(
            header,
            text="📡  NETWORK PORT SCANNER",
            font=("Consolas", 18, "bold"),
            fg="#00E5FF", bg="#161B22"
        ).pack()

        tk.Label(
            header,
            text="OOP Python Project  ·  Cybersecurity",
            font=("Consolas", 10),
            fg="#7B93A8", bg="#161B22"
        ).pack()

    # ── Input Section ────────────────────────────────────────
    def __build_input_section(self):
        frame = tk.Frame(self.root, bg="#0D1117", pady=15)
        frame.pack(fill="x", padx=20)

        # Target IP
        tk.Label(
            frame, text="Target IP / Hostname",
            font=("Consolas", 11), fg="#7B93A8", bg="#0D1117"
        ).grid(row=0, column=0, sticky="w", padx=(0, 15))

        self.__target_entry = tk.Entry(
            frame, width=28,
            font=("Consolas", 12), fg="#E8F4FD", bg="#161B22",
            insertbackground="white",
            relief="flat", bd=5
        )
        self.__target_entry.insert(0, "127.0.0.1")
        self.__target_entry.grid(row=0, column=1, padx=(0, 20))

        # Scan Type
        tk.Label(
            frame, text="Scan Type",
            font=("Consolas", 11), fg="#7B93A8", bg="#0D1117"
        ).grid(row=0, column=2, sticky="w", padx=(0, 10))

        self.__scan_type = ttk.Combobox(
            frame,
            values=["Quick Scan (1–100)", "Full Scan (1–1000)", "Custom Range"],
            state="readonly", width=20,
            font=("Consolas", 11)
        )
        self.__scan_type.current(0)
        self.__scan_type.grid(row=0, column=3)
        self.__scan_type.bind("<<ComboboxSelected>>", self.__on_scan_type_change)

        # Custom range (hidden by default)
        self.__custom_frame = tk.Frame(self.root, bg="#0D1117")
        self.__custom_frame.pack(fill="x", padx=20)

        tk.Label(
            self.__custom_frame, text="Start Port",
            font=("Consolas", 11), fg="#7B93A8", bg="#0D1117"
        ).grid(row=0, column=0, sticky="w", padx=(0,10), pady=5)

        self.__start_port = tk.Entry(
            self.__custom_frame, width=8,
            font=("Consolas", 12), fg="#E8F4FD", bg="#161B22",
            insertbackground="white", relief="flat", bd=5
        )
        self.__start_port.insert(0, "1")
        self.__start_port.grid(row=0, column=1, padx=(0, 20))

        tk.Label(
            self.__custom_frame, text="End Port",
            font=("Consolas", 11), fg="#7B93A8", bg="#0D1117"
        ).grid(row=0, column=2, sticky="w", padx=(0,10))

        self.__end_port = tk.Entry(
            self.__custom_frame, width=8,
            font=("Consolas", 12), fg="#E8F4FD", bg="#161B22",
            insertbackground="white", relief="flat", bd=5
        )
        self.__end_port.insert(0, "500")
        self.__end_port.grid(row=0, column=3)

        self.__custom_frame.pack_forget()  # hide by default

    # ── Show/hide custom range ───────────────────────────────
    def __on_scan_type_change(self, event):
        if self.__scan_type.get() == "Custom Range":
            self.__custom_frame.pack(fill="x", padx=20, pady=4)
        else:
            self.__custom_frame.pack_forget()

    # ── Scan Button ──────────────────────────────────────────
    def __build_scan_button(self):
        btn_frame = tk.Frame(self.root, bg="#0D1117", pady=8)
        btn_frame.pack()

        self.__scan_btn = tk.Button(
            btn_frame,
            text="  🔍  START SCAN  ",
            font=("Consolas", 13, "bold"),
            fg="#0D1117", bg="#00E5FF",
            activebackground="#00B8CC",
            relief="flat", bd=0, padx=20, pady=8,
            cursor="hand2",
            command=self.__start_scan
        )
        self.__scan_btn.pack(side="left", padx=10)

        self.__clear_btn = tk.Button(
            btn_frame,
            text="  🗑️  CLEAR  ",
            font=("Consolas", 13),
            fg="#E8F4FD", bg="#21262D",
            activebackground="#30363D",
            relief="flat", bd=0, padx=15, pady=8,
            cursor="hand2",
            command=self.__clear_results
        )
        self.__clear_btn.pack(side="left", padx=5)

    # ── Results Table ────────────────────────────────────────
    def __build_results_section(self):
        frame = tk.Frame(self.root, bg="#0D1117", pady=5)
        frame.pack(fill="both", expand=True, padx=20)

        tk.Label(
            frame, text="SCAN RESULTS",
            font=("Consolas", 11, "bold"),
            fg="#00E5FF", bg="#0D1117"
        ).pack(anchor="w", pady=(0, 5))

        # Table frame
        table_frame = tk.Frame(frame, bg="#161B22")
        table_frame.pack(fill="both", expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(table_frame)
        scrollbar.pack(side="right", fill="y")

        # Treeview (table)
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Treeview",
            background="#0D1117",
            foreground="#E8F4FD",
            rowheight=28,
            fieldbackground="#0D1117",
            font=("Consolas", 11)
        )
        style.configure(
            "Treeview.Heading",
            background="#161B22",
            foreground="#00E5FF",
            font=("Consolas", 11, "bold"),
            relief="flat"
        )
        style.map("Treeview", background=[("selected", "#21262D")])

        self.__table = ttk.Treeview(
            table_frame,
            columns=("port", "status", "service"),
            show="headings",
            yscrollcommand=scrollbar.set
        )
        self.__table.heading("port",    text="Port")
        self.__table.heading("status",  text="Status")
        self.__table.heading("service", text="Service")

        self.__table.column("port",    width=120, anchor="center")
        self.__table.column("status",  width=150, anchor="center")
        self.__table.column("service", width=350, anchor="center")

        self.__table.pack(fill="both", expand=True)
        scrollbar.config(command=self.__table.yview)

        # Row color tags
        self.__table.tag_configure("open",   foreground="#00FF88")
        self.__table.tag_configure("closed", foreground="#7B93A8")

    # ── Status Bar ───────────────────────────────────────────
    def __build_status_bar(self):
        bar = tk.Frame(self.root, bg="#161B22", pady=6)
        bar.pack(fill="x", side="bottom")

        self.__status_label = tk.Label(
            bar,
            text="Ready to scan.",
            font=("Consolas", 10),
            fg="#7B93A8", bg="#161B22"
        )
        self.__status_label.pack(side="left", padx=15)

        self.__summary_label = tk.Label(
            bar, text="",
            font=("Consolas", 10, "bold"),
            fg="#00E5FF", bg="#161B22"
        )
        self.__summary_label.pack(side="right", padx=15)

    # ── Start Scan ───────────────────────────────────────────
    def __start_scan(self):
        if self.__scanning:
            return

        target = self.__target_entry.get().strip()
        if not target:
            messagebox.showerror("Error", "Please enter a target IP address.")
            return

        # Clear old results
        self.__clear_results()

        # Run scan in separate thread so GUI doesn't freeze
        self.__scanning = True
        self.__scan_btn.config(state="disabled", text="  ⏳  SCANNING...  ")
        self.__status_label.config(text=f"Scanning {target} ...")

        thread = threading.Thread(target=self.__run_scan, args=(target,))
        thread.daemon = True
        thread.start()

    # ── Run Scan in Thread ───────────────────────────────────
    def __run_scan(self, target):
        try:
            scan_choice = self.__scan_type.get()

            if scan_choice == "Quick Scan (1–100)":
                scanner = QuickScanner(target)
                results = scanner.run()

            elif scan_choice == "Full Scan (1–1000)":
                scanner = FullScanner(target)
                results = scanner.run()

            else:
                try:
                    start = int(self.__start_port.get())
                    end   = int(self.__end_port.get())
                except ValueError:
                    self.root.after(0, lambda: messagebox.showerror("Error", "Enter valid port numbers."))
                    return
                scanner = Scanner(target)
                results = scanner.run(start, end)

            # Update GUI from main thread
            self.root.after(0, lambda: self.__show_results(results, target))

        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Scan Error", str(e)))
        finally:
            self.__scanning = False
            self.root.after(0, lambda: self.__scan_btn.config(
                state="normal", text="  🔍  START SCAN  "
            ))

    # ── Show Results in Table ────────────────────────────────
    def __show_results(self, results, target):
        open_count   = 0
        closed_count = 0

        for port in results:
            if port.is_open():
                self.__table.insert(
                    "", "end",
                    values=(f"Port {port.get_number()}", "✅  OPEN", port.get_service()),
                    tags=("open",)
                )
                open_count += 1
            else:
                self.__table.insert(
                    "", "end",
                    values=(f"Port {port.get_number()}", "🔴  CLOSED", port.get_service()),
                    tags=("closed",)
                )
                closed_count += 1

        self.__status_label.config(text=f"Scan complete  →  {target}")
        self.__summary_label.config(
            text=f"Open: {open_count}   Closed: {closed_count}"
        )

    # ── Clear Results ────────────────────────────────────────
    def __clear_results(self):
        for row in self.__table.get_children():
            self.__table.delete(row)
        self.__status_label.config(text="Ready to scan.")
        self.__summary_label.config(text="")


# ── Entry Point ──────────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app  = PortScannerApp(root)
    root.mainloop()
