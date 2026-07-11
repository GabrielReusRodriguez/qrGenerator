# QR Generator

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

A simple and powerful QR code generator CLI tool and Python library.

## Features

- Generate QR codes from text or URLs
- Save as PNG, SVG, or EPS format
- Customizable scale/size
- Interactive mode for easy use
- Automatic path validation and creation
- Overwrite protection
- Clean, type-hinted Python code

## Installation

### Quick Install

```bash
# Clone the repository
git clone https://github.com/yourusername/qrGenerator.git
cd qrGenerator

# Install dependencies
bash scripts/installLibs.sh

# Or using pip directly
pip install --user -r requirements.txt
```

### Install as Package

```bash
# Install in development mode
pip install --user -e .

# Then you can use the command
qr-generator "Hello World"
```

## Usage

### Basic Usage

```bash
# Generate QR code with default settings
python src/qrGenerator.py "Hello World"

# Specify output file
python src/qrGenerator.py -o my_qr.png "https://example.com"

# Custom scale factor
python src/qrGenerator.py -o my_qr.png -s 15 "My text"

# Interactive mode
python src/qrGenerator.py -i
# or just run without arguments
python src/qrGenerator.py
```

### Command Line Options

```
usage: qrGenerator.py [-h] [-o OUTPUT] [-s SCALE] [-i] [text]

Generate QR codes from text or URLs

positional arguments:
  text                  Text or URL to encode in the QR code

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output file path (default: ./qr.png)
  -s SCALE, --scale SCALE
                        Scale factor for the QR code (default: 10)
  -i, --interactive     Run in interactive mode

Examples:
  python qrGenerator.py "Hello World"
  python qrGenerator.py -o my_qr.png "https://example.com"
  python qrGenerator.py -o output/qr.png -s 15 "My text"
```

### As a Python Library

```python
from qrGenerator import generate_qr_code

# Generate a QR code
generate_qr_code(
    text="Hello World",
    output_path="my_qr.png",
    scale=10
)
```

## Project Structure

```
qrGenerator/
├── src/
│   ├── __init__.py           # Package initialization
│   └── qrGenerator.py        # Main QR generation logic
├── requirements.txt          # Dependencies
├── setup.py                 # Package setup
├── scripts/
│   └── installLibs.sh        # Installation script
├── README.md                # This file
└── LICENSE                   # License file
```

## Dependencies

- Python 3.7+
- [pyqrcode](https://pypi.org/project/PyQRCode/) - QR code generation
- [pypng](https://pypi.org/project/pypng/) - PNG support for pyqrcode

## Development

### Setting up a development environment

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
