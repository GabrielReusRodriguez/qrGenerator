#!/usr/bin/env python3
"""
Setup script for qrGenerator package
"""

from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="qrGenerator",
    version="1.1.0",
    description="A simple QR code generator library and CLI tool",
    author="qrGenerator",
    author_email="",
    url="",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=[
        req for req in requirements if req and not req.startswith("#")
    ],
    entry_points={
        "console_scripts": [
            "qr-generator=qrGenerator.qrGenerator:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Utilities",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
    ],
)
