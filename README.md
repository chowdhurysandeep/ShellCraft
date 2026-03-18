# 🔁 ShellCraft

> An interactive reverse shell payload generator for Linux-based systems — built for CTF challenges, educational use, and authorized penetration testing.

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS-informational?style=flat-square&logo=linux)
![Category](https://img.shields.io/badge/Category-Offensive%20Security-red?style=flat-square)
![License](https://img.shields.io/badge/License-See%20LICENSE-green?style=flat-square)

> Made by [Sandeep Prasad Chowdhury](https://github.com/chowdhurysandeep) | 🎓 Ethical Hacking Student

---

## 📌 About

ShellCraft helps security learners and red teamers quickly generate, manage, and test reverse shell payloads from a single CLI interface. Instead of memorizing payloads, just enter your IP, port, and pick a shell type — ShellCraft handles the rest.

---

## 📁 Project Structure

```
ShellCraft/
├── Disclaimer        # Project disclaimer
├── LICENSE           # License file
├── README.md         # Project documentation
├── shellcraft.py     # Main payload generator script
├── install.sh        # Installs dependencies and sets up ShellCraft
└── uninstall.sh      # Uninstall tool
```

---

## ✨ Features

| Feature | Status |
|---|---|
| Interactive Payload Menu | ✅ Yes |
| Alphabetical Sorting | ✅ Yes |
| Base64 Obfuscation | ✅ Yes |
| Clipboard Copy | ✅ Yes |
| Built-in Netcat Listener | ✅ Yes |
| Linux Payload Support | ✅ Yes |
| Windows Payload Support | ✅ Yes |
| Cross-Platform Support | ⚠️ Partial |

---

## 📦 Requirements

- Python 3.8+
- Linux / macOS (recommended)
- Netcat (`nc`) or Ncat
- Bash shell environment

**Python Dependencies** — installed automatically by `install.sh`:
- `pyfiglet`
- `termcolor`
- `pyperclip`

---

## ⚙️ Installation

```bash
git clone https://github.com/chowdhurysandeep/ShellCraft.git
cd ShellCraft
sudo bash install.sh
```

### Run

```bash
shellx
```

### Uninstall

```bash
sudo bash uninstall.sh
```

---

## 🚀 Usage

1. Launch the tool with `shellx`
2. Enter your listener **IP address**
3. Enter the listening **port**
4. Choose a **payload type** from the menu
5. *(Optional)* Obfuscate the payload with Base64
6. Copy the payload and start your listener — done!

---

## 📋 Payload Types

| # | Payload | Protocol | Target OS | Obfuscation |
|---|---|---|---|---|
| 1 | Awk Reverse Shell | TCP | Linux | ✅ Yes |
| 2 | Bash Reverse Shell | TCP | Linux | ✅ Yes |
| 3 | Bash Reverse Shell | UDP | Linux | ✅ Yes |
| 4 | Ncat Reverse Shell | TCP | Linux | ✅ Yes |
| 5 | Netcat BusyBox Shell | TCP | Linux | ✅ Yes |
| 6 | Netcat OpenBSD Shell | TCP | Linux | ✅ Yes |
| 7 | Netcat Traditional | TCP | Linux | ✅ Yes |
| 8 | Perl Reverse Shell | TCP | Linux | ✅ Yes |
| 9 | PHP Reverse Shell | TCP | Linux | ✅ Yes |
| 10 | PowerShell Shell | TCP | Windows | ❌ No |
| 11 | Python Reverse Shell | TCP | Linux | ❌ No |
| 12 | Telnet Reverse Shell | TCP | Linux | ❌ No |
| 13 | Exit | — | — | — |

> **Note:** Obfuscation uses Base64 encoding and is supported only for Unix-based payloads. PowerShell, Python, and Telnet payloads are excluded to avoid execution and compatibility issues.

---

## ⚠️ Disclaimer

ShellCraft is intended strictly for **educational and authorized security testing only**.

By using this tool, you agree that:
- You will only use it on systems you **own or have explicit permission** to test
- You understand local and international cybercrime laws
- You accept **full responsibility** for your actions

Unauthorized use may violate laws including:
- Information Technology Act (India)
- Computer Misuse Act (UK)
- CFAA — Computer Fraud and Abuse Act (USA)

---

## 👤 Author

**Sandeep Prasad Chowdhury**
🔗 [GitHub](https://github.com/chowdhurysandeep) · [LinkedIn](https://www.linkedin.com/in/sandeep-chowdhury-661a54397)
