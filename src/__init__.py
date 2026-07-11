"""
qrGenerator Package
A simple QR code generator library and CLI tool.
"""

from .qrGenerator import generate_qr_code, validate_output_path, main

__version__ = "1.1.0"
__author__ = "qrGenerator"

__all__ = ["generate_qr_code", "validate_output_path", "main"]
