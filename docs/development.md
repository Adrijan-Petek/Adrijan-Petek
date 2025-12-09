# Development Guide

<!-- Repository: https://github.com/Adrijan-Petek/Adrijan-Petek.git -->
<!-- Last updated: 2025-12-09 11:00:00 UTC -->

## 🚀 Getting Started

Welcome to the Dynamic GitHub Profile Generator development team! This guide will help you set up your development environment and start contributing.

### Prerequisites

- **Python**: 3.7 or higher
- **Git**: Latest version
- **Editor**: VS Code recommended (with Python extensions)

### Quick Setup

```bash
# 1. Fork and clone the repository
git clone https://github.com/your-username/dynamic-profile-generator.git
cd dynamic-profile-generator

# 2. Set up virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install development dependencies
pip install -r requirements-dev.txt

# 4. Install pre-commit hooks
pre-commit install

# 5. Run initial tests
pytest

# 6. Start developing!
```

## 🏗️ Project Structure

```
dynamic-profile-generator/
├── 📁 docs/                    # Documentation
│   ├── api.md                 # API reference
│   └── development.md         # This file
├── 📁 tests/                  # Test suite
│   ├── __init__.py
│   ├── conftest.py           # Test configuration
│   └── test_generator.py     # Main tests
├── 📁 templates/              # Template system
│   └── 📁 components/         # Modular components
│       ├── header.py         # Header section
│       ├── learning.py       # Learning progress
│       ├── projects.py       # Featured projects
│       └── stats.py          # GitHub statistics
├── 📁 assets/                 # Static assets
│   └── 📁 img/               # Banner images
├── 📄 profile_generator.py    # Main generator script
├── 📄 config.json            # Configuration file
├── 📄 pyproject.toml         # Project metadata
├── 📄 requirements-dev.txt   # Development dependencies
└── 📄 README.md              # Project documentation
```

## 🔧 Development Workflow

### 1. Choose an Issue

- Check [GitHub Issues](https://github.com/your-username/dynamic-profile-generator/issues) for open tasks
- Look for issues labeled `good first issue` or `help wanted`
- Comment on the issue to indicate you're working on it

### 2. Create a Branch

```bash
# Create and switch to feature branch
git checkout -b feature/your-feature-name

# Or for bug fixes
git checkout -b bugfix/issue-number-description
```

### 3. Make Changes

- Follow the [coding standards](#coding-standards)
- Write tests for new features
- Update documentation as needed
- Keep commits small and focused

### 4. Test Your Changes

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific tests
pytest tests/test_generator.py -v

# Run linting
black .
flake8 .
mypy .
```

### 5. Commit Your Changes

```bash
# Stage your changes
git add .

# Commit with descriptive message
git commit -m "✨ Add new feature: description"

# Push to your branch
git push origin feature/your-feature-name
```

### 6. Create Pull Request

- Go to GitHub and create a PR
- Fill out the PR template completely
- Request review from maintainers
- Address any feedback

## 📝 Coding Standards

### Python Style

We follow **PEP 8** with these tools:

- **Black**: Code formatting (88 character line length)
- **isort**: Import sorting
- **flake8**: Linting
- **mypy**: Type checking

### Code Quality

```python
# ✅ Good: Clear, descriptive names
def generate_profile_readme(config: dict, daily_content: dict) -> str:
    """Generate a complete GitHub profile README."""
    pass

# ❌ Bad: Unclear names and no type hints
def gen_readme(c, dc):
    pass
```

### Documentation

```python
def load_config() -> dict:
    """
    Load configuration from JSON file.

    Returns:
        Dictionary containing parsed configuration data.

    Raises:
        FileNotFoundError: If config.json doesn't exist.
        json.JSONDecodeError: If config.json contains invalid JSON.
    """
    pass
```

### Error Handling

```python
def safe_load_config() -> dict:
    """Load configuration with proper error handling."""
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.warning("config.json not found, using defaults")
        return get_default_config()
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in config.json: {e}")
        raise ConfigurationError("Invalid configuration file") from e
```

## 🧪 Testing

### Test Structure

```python
import pytest
from profile_generator import load_config

class TestConfigLoading:
    """Test configuration loading functionality."""

    def test_load_valid_config(self):
        """Test loading a valid configuration file."""
        config = load_config()
        assert isinstance(config, dict)
        assert "user" in config

    def test_load_missing_config(self):
        """Test behavior when config file is missing."""
        # Test implementation
        pass

    @pytest.mark.parametrize("invalid_json", [
        "{invalid json}",
        '{"incomplete": json}',
        "",
    ])
    def test_load_invalid_json(self, invalid_json):
        """Test handling of invalid JSON."""
        # Test implementation
        pass
```

### Running Tests

```bash
# All tests
pytest

# Verbose output
pytest -v

# With coverage
pytest --cov=. --cov-report=html

# Specific test file
pytest tests/test_generator.py

# Specific test
pytest tests/test_generator.py::TestConfig::test_load_config

# Run failed tests only
pytest --lf

# Stop on first failure
pytest -x
```

### Test Coverage

Aim for >90% code coverage:

```bash
# Generate coverage report
pytest --cov=. --cov-report=html

# Open report in browser
open htmlcov/index.html
```

## 🎨 Template Development

### Component Interface

All template components must implement:

```python
def generate(config: dict, daily_content: dict) -> str:
    """
    Generate component content.

    Args:
        config: User configuration dictionary
        daily_content: Daily varying content

    Returns:
        String containing component HTML/markdown
    """
    pass
```

### Best Practices

- **Responsive Design**: Ensure mobile compatibility
- **Accessibility**: Use semantic HTML, alt text for images
- **Performance**: Minimize external requests
- **Maintainability**: Keep components focused and reusable

### Example Component

```python
def generate(config, daily_content):
    """Generate header component."""
    user = config.get('user', {})
    name = user.get('name', 'Developer')

    return f"""
    <div align="center">
        <h1>👋 Hi, I'm {name}!</h1>
        <p>🚀 Building amazing things with code</p>
    </div>
    """
```

## 🔄 Continuous Integration

### GitHub Actions

The project uses GitHub Actions for CI/CD:

- **Tests**: Run on every push and PR
- **Linting**: Code quality checks
- **Coverage**: Test coverage reporting
- **Release**: Automated publishing

### Local CI

Run the same checks locally:

```bash
# Run pre-commit hooks
pre-commit run --all-files

# Or install and run
pre-commit install
pre-commit run
```

## 📚 Documentation

### Types of Documentation

- **README.md**: User-facing project documentation
- **API Docs**: Technical API reference (`docs/api.md`)
- **Development Guide**: This file
- **Code Comments**: Inline documentation
- **CHANGELOG.md**: Version history

### Documentation Standards

- Use **Markdown** for all documentation
- Keep language clear and concise
- Include code examples where helpful
- Update docs with code changes

## 🚀 Deployment

### Local Testing

```bash
# Generate test README
python profile_generator.py

# Check output
cat README.md
```

### GitHub Pages (Future)

```bash
# Build documentation
mkdocs build

# Serve locally
mkdocs serve
```

### PyPI Publishing

```bash
# Build package
python -m build

# Upload to test PyPI
twine upload --repository testpypi dist/*

# Upload to production PyPI
twine upload dist/*
```

## 🤝 Contributing Guidelines

### Communication

- **Issues**: Bug reports and feature requests
- **Discussions**: General questions and ideas
- **Pull Requests**: Code contributions
- **Discord**: Real-time chat (coming soon!)

### Code Review Process

1. **Automated Checks**: CI must pass
2. **Peer Review**: At least one maintainer review
3. **Testing**: All tests must pass
4. **Documentation**: Docs updated if needed
5. **Merge**: Squash and merge approved PRs

### Recognition

Contributors are recognized through:
- GitHub contributor statistics
- CHANGELOG.md mentions
- Release notes
- Special acknowledgments

## 🆘 Getting Help

### Resources

- **Documentation**: Check `docs/` directory
- **Issues**: Search existing GitHub issues
- **Discussions**: Ask the community
- **Code**: Read the source code

### Asking Questions

When asking for help:

1. **Be Specific**: Include error messages, code snippets
2. **Provide Context**: Describe what you're trying to do
3. **Show Attempts**: Include what you've tried
4. **Use Examples**: Provide minimal reproducible examples

### Common Issues

**"Module not found"**
```bash
# Ensure you're in the right directory
cd /path/to/dynamic-profile-generator

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements-dev.txt
```

**"Tests failing"**
```bash
# Update dependencies
pip install -r requirements-dev.txt --upgrade

# Clear cache
pytest --cache-clear

# Run specific failing test
pytest tests/test_generator.py::TestClass::test_method -v
```

## 🎯 Next Steps

1. **Explore the Codebase**: Read through the main generator
2. **Run the Tests**: Get familiar with the test suite
3. **Try a Small Change**: Fix a bug or add a test
4. **Contribute**: Submit your first pull request!

---

Happy coding! 🎉

*Built with ❤️ by the open source community*