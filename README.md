## 🔁 ShellCraft <br>
ShellCraft is an interactive reverse shell payload generator for Linux-based systems, built for educational use, CTF challenges, and authorized penetration testing.
It helps security learners and red teamers quickly generate, manage, and test reverse shell payloads from a single CLI interface.

---

## 📁 Project Structure
```
ShellCraft/
├── Disclaimer # Project Disclaimer
├── LICENSE # License file
├── README.md # Project documentation
├── shellcraft.py # Main payload generator script
├── install.sh # Installs required Python packages with pip and sets up ShellCraft
└── uninstall.sh # Uninstall tool
```
---

## ✨ Features
```
| Feature                     | Status |
|-----------------------------|--------|
| Interactive Payload Menu    | ✅ Yes |
| Alphabetical Sorting        | ✅ Yes |
| Base64 Obfuscation          | ✅ Yes |
| Clipboard Copy              | ✅ Yes |
| Built-in Netcat Listener    | ✅ Yes |
| Cross-Platform Support      | ⚠️ Partial |
| Windows Payload Support    | ✅ Yes |
| Linux Payload Support       | ✅ Yes |

```
---

📦 **Requirements**
- Python 3.8+
- Linux/macOS (recommended)
- Netcat (nc) or Ncat
- Bash shell environment

📦 **Dependencies** <br>
All required Python libraries are automatically installed by the installer:<br>
- pyfiglet
- termcolor
- pyperclip

---

## ⚙️ Installation


### Download:

Download with `git`:
```
git clone https://github.com/chowdhurysandeep/ShellCraft.git
cd ShellCraft
```
### Install ShellCraft:
```
sudo bash install.sh
```
or
```
sudo ./install.sh
```
### Run ShellCraft:
```
shellx 
```
### Uninstall ShellCraft:
```
sudo bash uninstall.sh
```
or
```
sudo ./uninstall.sh
```
---

## ⚙️ Usage

1. Launch the tool

2. Enter your listener IP address

3. Enter the listening port

4. Choose the payload type

5. (Optional) Obfuscate the payload

6. Copy and directly start a listener

---

## 📋 Payload Types & Obfuscation Support
```
| Option | Payload Name           | Protocol | Target OS | Obfuscation |
|-------:|------------------------|----------|-----------|-------------|
| 1      | Awk Reverse Shell      | TCP      | Linux     | ✔ Yes |
| 2      | Bash Reverse Shell     | TCP      | Linux     | ✔ Yes |
| 3      | Bash Reverse Shell     | UDP      | Linux     | ✔ Yes |
| 4      | Ncat Reverse Shell     | TCP      | Linux     | ✔ Yes |
| 5      | Netcat BusyBox Shell   | TCP      | Linux     | ✔ Yes |
| 6      | Netcat OpenBSD Shell   | TCP      | Linux     | ✔ Yes |
| 7      | Netcat Traditional     | TCP      | Linux     | ✔ Yes |
| 8      | Perl Reverse Shell     | TCP      | Linux     | ✔ Yes |
| 9      | PHP Reverse Shell      | TCP      | Linux     | ✔ Yes |
| 10     | PowerShell Shell       | TCP      | Windows   | ❌ No |
| 11     | Python Reverse Shell   | TCP      | Linux     | ❌ No |
| 12     | Telnet Reverse Shell   | TCP      | Linux     | ❌ No |
| 13     | Exit                   | —        | —         | — |

```

**Note:**
```
Obfuscation uses Base64 encoding and is supported only for Unix-based
payloads. Windows PowerShell, Python, and Telnet payloads are intentionally
excluded to avoid execution and compatibility issues.
```
---


---
## ⚠️Disclaimer

ShellCraft is intended strictly for **educational and authorized security testing**.

By using this tool, you agree that:
- You will only use it on systems you own or have explicit permission to test
- You understand local and international cybercrime laws
- You accept full responsibility for your actions

Unauthorized use of this software may violate laws such as:
- Information Technology Act (India)
- Computer Misuse Act
- CFAA (USA)

---
## 🧠 Author

Sandeep Chowdhury
🔗 GitHub: https://github.com/chowdhurysandeep
