#!/bin/bash

# ------------------------------------------------------------------------
# setup.sh for zap-cli
# - Creates and uses a virtual environment (venv).
# - Installs dependencies from requirements.txt.
# - Installs zap-cli in editable mode and makes it available globally
#   by adding the venv bin to your PATH in ~/.bashrc.
#
# After running: open a new terminal or run: source ~/.bashrc
# Then you can run: zap-cli
# ------------------------------------------------------------------------

set -e

# Project directory: where this script lives (works when run from any cwd)
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REQUIREMENTS="$PROJECT_DIR/requirements.txt"
VENV_BIN="$PROJECT_DIR/venv/bin"

# 1. Check Python 3
if ! command -v python3 &>/dev/null; then
    echo "Error: python3 not found. Please install Python 3."
    exit 1
fi

# 2. Check venv module (command -v doesn't work for "python3 -m venv")
if ! python3 -m venv --help &>/dev/null; then
    echo "Error: python3 -m venv not available. Install python3-venv, e.g.:"
    echo "  sudo apt install python3-venv"
    exit 1
fi

# 3. Create virtual environment
echo "Creating virtual environment in $PROJECT_DIR/venv ..."
python3 -m venv "$PROJECT_DIR/venv"

# 4. Activate and install
echo "Activating venv and installing dependencies..."
# shellcheck source=/dev/null
source "$VENV_BIN/activate"

# 5. Install from requirements.txt (use python -m pip for portability)
if [[ -f "$REQUIREMENTS" ]]; then
    python -m pip install -r "$REQUIREMENTS"
else
    echo "Error: requirements.txt not found at $REQUIREMENTS"
    exit 1
fi

# 6. Install zap-cli in editable mode (adds 'zap-cli' to venv/bin)
echo "Installing zap-cli in editable mode..."
python -m pip install -e "$PROJECT_DIR"

deactivate

# 7. Make zap-cli available globally: add venv/bin to PATH in .bashrc
BASHRC="${HOME}/.bashrc"
MARKER="# zap-cli venv PATH (added by setup.sh)"
LINE="export PATH=\"$VENV_BIN:\$PATH\" $MARKER"

touch "$BASHRC" 2>/dev/null || true
if grep -qF "$MARKER" "$BASHRC" 2>/dev/null; then
    echo "zap-cli PATH already present in $BASHRC"
else
    echo "" >> "$BASHRC"
    echo "$LINE" >> "$BASHRC"
    echo "Added $VENV_BIN to PATH in $BASHRC"
fi

echo ""
echo "Setup complete. To use zap-cli from any path:"
echo "  source ~/.bashrc   # or open a new terminal"
echo "  zap-cli"
echo ""
