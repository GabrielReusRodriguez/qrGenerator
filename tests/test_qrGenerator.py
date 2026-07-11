"""
Tests for QR Generator
"""

import os
import shutil
import tempfile
import unittest
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from qrGenerator import generate_qr_code, validate_output_path


class TestValidateOutputPath(unittest.TestCase):
    """Tests for validate_output_path function"""
    
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_adds_png_extension(self):
        """Test that .png extension is added when not specified"""
        result = validate_output_path(os.path.join(self.temp_dir, "test"))
        self.assertTrue(result.endswith('.png'))
    
    def test_keeps_existing_png_extension(self):
        """Test that existing .png extension is kept"""
        result = validate_output_path(os.path.join(self.temp_dir, "test.png"))
        self.assertEqual(result, os.path.join(self.temp_dir, "test.png"))
    
    def test_creates_parent_directories(self):
        """Test that parent directories are created if they don't exist"""
        nested_path = os.path.join(self.temp_dir, "nested", "dir", "test")
        result = validate_output_path(nested_path)
        self.assertTrue(os.path.exists(os.path.dirname(result)))
    
    def test_handles_svg_extension(self):
        """Test that .svg extension is preserved"""
        result = validate_output_path(os.path.join(self.temp_dir, "test.svg"))
        self.assertTrue(result.endswith('.svg'))


class TestGenerateQRCode(unittest.TestCase):
    """Tests for generate_qr_code function"""
    
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_generates_png_file(self):
        """Test that a PNG file is generated"""
        output_path = os.path.join(self.temp_dir, "test.png")
        generate_qr_code("Hello World", output_path, scale=5)
        self.assertTrue(os.path.exists(output_path))
    
    def test_empty_text_raises_error(self):
        """Test that empty text raises ValueError"""
        output_path = os.path.join(self.temp_dir, "test.png")
        with self.assertRaises(ValueError):
            generate_qr_code("", output_path)
    
    def test_none_text_raises_error(self):
        """Test that None text raises ValueError"""
        output_path = os.path.join(self.temp_dir, "test.png")
        with self.assertRaises(ValueError):
            generate_qr_code(None, output_path)
    
    def test_invalid_scale_raises_error(self):
        """Test that invalid scale raises ValueError"""
        output_path = os.path.join(self.temp_dir, "test.png")
        with self.assertRaises(ValueError):
            generate_qr_code("test", output_path, scale=0)
    
    def test_negative_scale_raises_error(self):
        """Test that negative scale raises ValueError"""
        output_path = os.path.join(self.temp_dir, "test.png")
        with self.assertRaises(ValueError):
            generate_qr_code("test", output_path, scale=-1)
    
    def test_whitespace_only_text_raises_error(self):
        """Test that whitespace-only text raises ValueError"""
        output_path = os.path.join(self.temp_dir, "test.png")
        with self.assertRaises(ValueError):
            generate_qr_code("   ", output_path)


class TestIntegration(unittest.TestCase):
    """Integration tests for the QR generator"""
    
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_full_workflow(self):
        """Test the full workflow: validate path and generate QR"""
        raw_path = os.path.join(self.temp_dir, "qr_output")
        validated_path = validate_output_path(raw_path)
        
        generate_qr_code("Test Content", validated_path, scale=8)
        
        self.assertTrue(os.path.exists(validated_path))
        self.assertTrue(validated_path.endswith('.png'))


if __name__ == '__main__':
    unittest.main()
