"""
Test configuration and utilities for Dynamic GitHub Profile Generator tests
"""

import json
import tempfile
from pathlib import Path
from typing import Dict, Any


def create_test_config(**overrides) -> str:
    """Create a temporary test configuration file"""
    base_config = {
        "user": {
            "name": "Test User",
            "github": "testuser",
            "website": "https://test.com",
            "learning_repo": "https://github.com/testuser/learning"
        },
        "social": {
            "twitter": "https://twitter.com/testuser",
            "linkedin": "https://linkedin.com/in/testuser"
        },
        "tech_stack": ["Python", "JavaScript"],
        "learning_paths": {
            "python": ["Basics", "OOP"],
            "javascript": ["ES6+", "React"]
        }
    }

    # Apply overrides
    config = {**base_config, **overrides}

    # Create temporary file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump(config, f, indent=2)
        return f.name


def load_test_config(config_path: str) -> Dict[str, Any]:
    """Load configuration from test file"""
    with open(config_path, 'r') as f:
        return json.load(f)


def cleanup_test_file(file_path: str):
    """Clean up temporary test file"""
    Path(file_path).unlink(missing_ok=True)


# Test constants
TEST_USER_CONFIG = {
    "name": "Test Developer",
    "github": "testdev",
    "website": "https://test.dev",
    "learning_repo": "https://github.com/testdev/learning-journey"
}

TEST_SOCIAL_CONFIG = {
    "twitter": "https://twitter.com/testdev",
    "linkedin": "https://linkedin.com/in/testdev",
    "devto": "https://dev.to/testdev"
}

TEST_TECH_STACK = [
    "Python", "JavaScript", "React", "Node.js",
    "Docker", "AWS", "PostgreSQL", "MongoDB"
]

TEST_LEARNING_PATHS = {
    "python": ["Basics", "Data Structures", "Algorithms", "Web Frameworks"],
    "javascript": ["ES6+", "React", "Node.js", "TypeScript"],
    "cloud": ["AWS", "Docker", "Kubernetes", "CI/CD"]
}