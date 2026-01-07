#!/bin/bash

TOOL_NAME="shellx"
TOOL_DISPLAY_NAME="ShellCraft"

INSTALL_DIR="/opt/$TOOL_NAME"
BIN_PATH="/usr/local/bin/$TOOL_NAME"

echo "[*] Uninstalling $TOOL_DISPLAY_NAME..."

# Root check
if [ "$EUID" -ne 0 ]; then
  echo "[-] Please run as root (sudo ./uninstall.sh)"
  exit 1
fi

# Safety guard
if [ -z "$INSTALL_DIR" ] || [ "$INSTALL_DIR" = "/" ]; then
  echo "[-] Unsafe INSTALL_DIR detected. Aborting."
  exit 1
fi

# Remove installation directory
if [ -d "$INSTALL_DIR" ]; then
  echo "[+] Removing $INSTALL_DIR"
  rm -rf "$INSTALL_DIR"
else
  echo "[!] $INSTALL_DIR not found"
fi

# Remove binary
if [ -f "$BIN_PATH" ] || [ -L "$BIN_PATH" ]; then
  echo "[+] Removing $BIN_PATH"
  rm -f "$BIN_PATH"
else
  echo "[!] shellx binary not found in $BIN_PATH"
fi

echo "[✔] $TOOL_DISPLAY_NAME successfully uninstalled"
