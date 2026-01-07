#!/bin/bash

GREEN="\e[32m"
RED="\e[31m"
YELLOW="\e[33m"
NC="\e[0m"

TOOL_NAME="shellx"
TOOL_DISPLAY_NAME="ShellCraft"
ENTRY_FILE="ShellCraft.py"

INSTALL_DIR="/opt/$TOOL_NAME"
BIN_PATH="/usr/local/bin/$TOOL_NAME"

echo -e "${GREEN}[+] Installing $TOOL_DISPLAY_NAME (Linux only)...${NC}"

# Root check
if [ "$EUID" -ne 0 ]; then
  echo -e "${RED}[-] Please run as root (sudo ./install.sh)${NC}"
  exit 1
fi

# Python check
if ! command -v python3 &>/dev/null; then
  echo -e "${RED}[-] Python3 not found. Install Python3 first.${NC}"
  exit 1
fi

# pip check
if ! command -v pip3 &>/dev/null; then
  echo -e "${RED}[-] pip3 not found. Install pip3 first.${NC}"
  exit 1
fi

# Install dependencies
pip3 install pyfiglet termcolor pyperclip --break-system-packages 2>/dev/null

# Create install directory
mkdir -p "$INSTALL_DIR"

# Copy tool
cp "$ENTRY_FILE" "$INSTALL_DIR/$ENTRY_FILE"

# Create launcher
cat << EOF > "$BIN_PATH"
#!/bin/bash
exec python3 "$INSTALL_DIR/$ENTRY_FILE"
EOF

# Make executable
chmod +x "$BIN_PATH"

echo ""
echo -e "${GREEN}[✓] Installation completed successfully!${NC}"
echo -e "${YELLOW}[✓] Run the tool using:${NC} shellx"
echo ""
