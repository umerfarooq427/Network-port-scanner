# 📡 Network Port Scanner

A command-line network port scanner built with Python using Object-Oriented Programming (OOP) principles. This project was made as part of a 2nd semester OOP course and is related to **cybersecurity**.

---

##  What it does

-  Scan any target IP address for open and closed ports
-  Identify what service is running on each open port
-  Quick Scan — scans top 100 ports fast
-  Full Scan — scans all ports from 1 to 1000
-  Custom Scan — user picks their own port range
-  Generate a clean scan report with timestamp

---

##  OOP Concepts Used

| Concept | Where it is applied |
|---|---|
| **Classes & Objects** | Every port scanned becomes a Port object |
| **Encapsulation** | Socket logic hidden inside `_check_port()` |
| **Abstraction** | User just calls `scanner.run()` — complexity hidden |
| **Inheritance** | `QuickScanner` and `FullScanner` both extend `Scanner` |

---

##  Project Structure

```
network-port-scanner/
 ├── main.py                 ← entry point, run this
 ├── scanner.py              ← Scanner, QuickScanner, FullScanner
 ├── port.py                 ← Port class
 ├── report.py               ← ScanReport class
 └── service_identifier.py   ← maps port numbers to service names
```

---

##  Requirements

- Python 3.x
- No pip install needed — all libraries are built-in ✅

---

##  How to Run

**Step 1 — Clone the repository**
```
git clone https://github.com/yourusername/network-port-scanner.git
```

**Step 2 — Go into the project folder**
```
cd network-port-scanner
```

**Step 3 — Run the project**
```
python main.py
```

---

## 🖥️ Menu Options

```
╔══════════════════════════════════════╗
║       📡 NETWORK PORT SCANNER       ║
╠══════════════════════════════════════╣
║  [1]  Quick Scan  (ports 1–100)     ║
║  [2]  Full Scan   (ports 1–1000)    ║
║  [3]  Custom Scan (you pick range)  ║
║  [4]  Exit                          ║
╚══════════════════════════════════════╝
```

---

##  Safe Targets to Scan

| Target | Description |
|---|---|
| `127.0.0.1` | Your own PC — safest option |
| `192.168.1.1` | Your home WiFi router |
| `scanme.nmap.org` | Server made for legal scanning practice |

---

##  Sample Output

```
Scanning 127.0.0.1 (ports 1–100)...

══════════════════════════════════════
           SCAN REPORT
══════════════════════════════════════
Target  : 127.0.0.1
Time    : 2024-05-26 14:32:01
Total   : 100 ports scanned
──────────────────────────────────────

OPEN PORTS (3 found):

  [OPEN]   Port 22     →  SSH
  [OPEN]   Port 80     →  HTTP
  [OPEN]   Port 443    →  HTTPS

──────────────────────────────────────
Open   : 3
Closed : 97
══════════════════════════════════════
```

---

##  Common Port Numbers

| Port | Service | Description |
|---|---|---|
| 21 | FTP | File transfer |
| 22 | SSH | Remote login |
| 25 | SMTP | Sending emails |
| 53 | DNS | Domain name system |
| 80 | HTTP | Websites |
| 443 | HTTPS | Secure websites |
| 3306 | MySQL | Database |
| 3389 | RDP | Remote desktop |

---

##  Legal Warning

> **Never scan IP addresses you do not own.**
> Unauthorized port scanning is illegal under cybercrime laws.
> Only scan `127.0.0.1` (your own PC), your home router, or `scanme.nmap.org` which is made for practice.

---

##  Team Members

| Name | Role | File Responsible |
|---|---|---|
| Umer farooq | Team Lead | main.py |
| Ayaan hassan | Developer | scanner.py |
| Matti ullah | Developer | port.py |
| Ather ahmed khan | Developer | report.py |
| Muhammad hanan ameer | Developer | service_identifier.py |

---

##  Course Info

- **Subject**  : Object Oriented Programming (OOP)
- **Language** : Python 3
- **Semester** : 2nd Semester
- **Topic**    : Cybersecurity
