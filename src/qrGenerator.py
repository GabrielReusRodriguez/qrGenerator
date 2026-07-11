#!/usr/bin/env python3
"""
QR Code Generator
Generates QR codes from text or URLs and saves them as image files.

Usage:
    python qrGenerator.py -o <output_path> -s <scale> <text_or_url>
    python qrGenerator.py --output <output_path> --scale <scale> <text_or_url>
"""

import argparse
import os
import sys
from pathlib import Path

import pyqrcode


def generate_qr_code(text: str, output_path: str, scale: int = 10) -> None:
    """
    Generate a QR code from text and save it as a PNG image.
    
    Args:
        text: The text or URL to encode in the QR code
        output_path: Path to save the generated QR code image
        scale: Scale factor for the QR code (default: 10)
    
    Raises:
        ValueError: If text is empty or scale is invalid
        RuntimeError: If QR code generation fails
    """
    if not text or not text.strip():
        raise ValueError("Text to encode cannot be empty")
    
    if scale <= 0:
        raise ValueError("Scale must be a positive integer")
    
    try:
        qr = pyqrcode.create(text)
        qr.png(output_path, scale=scale)
    except Exception as e:
        raise RuntimeError(f"Failed to generate QR code: {str(e)}")


def validate_output_path(output_path: str) -> str:
    """
    Validate and normalize the output file path.
    
    Args:
        output_path: The output path to validate
        
    Returns:
        Normalized output path with .png extension if not specified
    """
    path = Path(output_path)
    
    if not path.suffix or path.suffix.lower() not in ['.png', '.svg', '.eps']:
        path = path.with_suffix('.png')
    
    path.parent.mkdir(parents=True, exist_ok=True)
    
    return str(path)


def main(argv: list[str] | None = None) -> None:
    """
    Main entry point for the QR generator CLI.
    
    Args:
        argv: Command line arguments (default: sys.argv[1:])
    """
    parser = argparse.ArgumentParser(
        description="Generate QR codes from text or URLs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python qrGenerator.py "Hello World"
  python qrGenerator.py -o my_qr.png "https://example.com"
  python qrGenerator.py -o output/qr.png -s 15 "My text"
        """
    )
    
    parser.add_argument(
        "text",
        nargs='?',
        help="Text or URL to encode in the QR code"
    )
    
    parser.add_argument(
        "-o", "--output",
        type=str,
        default="./qr.png",
        help="Output file path (default: ./qr.png)"
    )
    
    parser.add_argument(
        "-s", "--scale",
        type=int,
        default=10,
        help="Scale factor for the QR code (default: 10)"
    )
    
    parser.add_argument(
        "-i", "--interactive",
        action="store_true",
        help="Run in interactive mode"
    )
    
    args = parser.parse_args(argv)
    
    if args.interactive or not args.text:
        if not args.text:
            print("No text provided. Entering interactive mode...")
        
        text = input("Enter text or URL to encode: ").strip()
        if not text:
            print("Error: Text cannot be empty")
            sys.exit(1)
        
        output = input(f"Enter output path [{args.output}]: ").strip()
        output_path = output if output else args.output
        
        scale_input = input(f"Enter scale factor [{args.scale}]: ").strip()
        scale = int(scale_input) if scale_input.isdigit() else args.scale
    else:
        text = args.text
        output_path = args.output
        scale = args.scale
    
    try:
        output_path = validate_output_path(output_path)
        
        if os.path.exists(output_path):
            overwrite = input(f"File '{output_path}' already exists. Overwrite? [y/N]: ").strip().lower()
            if overwrite != 'y':
                print("Operation cancelled.")
                sys.exit(0)
        
        generate_qr_code(text, output_path, scale)
        print(f"QR code successfully generated: {output_path}")
        
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except RuntimeError as re:
        print(f"Error: {re}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()