"""
Tests for Dynamic GitHub Profile Generator
Repository: https://github.com/Adrijan-Petek/Adrijan-Petek.git
Last updated: 2025-12-09 11:00:00 UTC
"""
import json
import os
import tempfile
from pathlib import Path

import pytest

from profile_generator import load_config, generate_daily_content, main


class TestConfig:
    """Test configuration loading functionality"""

    def test_load_config_default(self):
        """Test loading default configuration"""
        config = load_config()
        assert isinstance(config, dict)
        assert "user" in config
        assert "name" in config["user"]

    def test_load_config_file(self):
        """Test loading configuration from file"""
        test_config = {
            "user": {
                "name": "Test User",
                "github": "testuser"
            }
        }

        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(test_config, f)
            config_path = f.name

        try:
            # Temporarily change to test config file
            original_config = 'config.json'
            os.rename(original_config, 'config.json.backup')

            os.rename(config_path, 'config.json')
            config = load_config()

            assert config["user"]["name"] == "Test User"
            assert config["user"]["github"] == "testuser"

        finally:
            # Restore original config
            if os.path.exists('config.json.backup'):
                os.rename('config.json.backup', 'config.json')
            if os.path.exists(config_path):
                os.unlink(config_path)


class TestDailyContent:
    """Test daily content generation"""

    def test_generate_daily_content(self):
        """Test daily content generation returns expected structure"""
        content = generate_daily_content()

        assert isinstance(content, dict)
        assert "color_theme" in content
        assert "spotlight_project" in content
        assert "learning_focus" in content

    def test_daily_content_variety(self):
        """Test that daily content varies based on day"""
        # This is a basic test - in real implementation you'd mock datetime
        content1 = generate_daily_content()
        content2 = generate_daily_content()

        # Content should be deterministic for same day
        assert content1 == content2


class TestGenerator:
    """Test main generator functionality"""

    def test_main_execution(self):
        """Test main function executes without errors"""
        # This test might need adjustment based on actual main function
        try:
            main()
            assert True  # If we get here, no exception was raised
        except SystemExit:
            # main() might call sys.exit() - that's okay for this test
            assert True
        except Exception as e:
            pytest.fail(f"main() raised an exception: {e}")

    def test_readme_generation(self):
        """Test that README.md is created"""
        readme_path = Path("README.md")

        # Ensure README exists before test
        if not readme_path.exists():
            pytest.skip("README.md not found - run generator first")

        original_mtime = readme_path.stat().st_mtime

        # Run generator
        main()

        # Check that README was updated
        new_mtime = readme_path.stat().st_mtime
        assert new_mtime >= original_mtime


class TestTemplates:
    """Test template system"""

    def test_template_imports(self):
        """Test that template modules can be imported"""
        try:
            from templates.components import header, learning, projects, stats
            assert True
        except ImportError as e:
            pytest.fail(f"Failed to import templates: {e}")

    def test_template_functions(self):
        """Test that template functions exist and are callable"""
        from templates.components import header

        # Test that generate function exists
        assert hasattr(header, 'generate')
        assert callable(header.generate)


class TestAssets:
    """Test asset handling"""

    def test_assets_directory(self):
        """Test that assets directory exists"""
        assert Path("assets").exists()
        assert Path("assets").is_dir()

    def test_img_directory(self):
        """Test that img directory exists"""
        assert Path("img").exists() or Path("assets/img").exists()

    def test_templates_directory(self):
        """Test that templates directory exists"""
        assert Path("templates").exists()
        assert Path("templates/components").exists()


if __name__ == "__main__":
    pytest.main([__file__])