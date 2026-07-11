#!/usr/bin/env bash
# QR Generator Installation Script
# This script installs the required dependencies for the QR generator

set -e

echo "Installing QR Generator dependencies..."

# Check if pip is available
if ! command -v pip &> /dev/null; then
    echo "Error: pip is not installed. Please install pip first."
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 --version 2>&1 | cut -d' ' -f2 | cut -d'.' -f1-2)
if [[ "$PYTHON_VERSION" < "3.7" ]]; then
    echo "Error: Python 3.7 or higher is required. You have Python $PYTHON_VERSION"
    exit 1
fi

echo "Detected Python $PYTHON_VERSION"

# Install dependencies
if [ -f "requirements.txt" ]; then
    echo "Installing from requirements.txt..."
    pip install --user -r requirements.txt
else
    echo "requirements.txt not found. Installing core dependencies..."
    pip install --user pyqrcode pypng
fi

echo ""
echo "Installation complete!"
echo ""
echo "You can now use the QR generator:"
echo "  python src/qrGenerator.py -h"
echo ""
echo "Or install as a package:"
echo "  pip install --user -e ."
