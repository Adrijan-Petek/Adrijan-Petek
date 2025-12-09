# Contributing to Dynamic GitHub Profile Generator

<!-- Repository: https://github.com/Adrijan-Petek/Adrijan-Petek.git -->
<!-- Last updated: 2025-12-09 11:00:00 UTC -->

<div align="center">

## 🌟 Welcome Contributors!

Thank you for your interest in contributing to the **Dynamic GitHub Profile Generator**! We welcome contributions from developers of all skill levels.

[![GitHub contributors](https://img.shields.io/github/contributors/your-username/dynamic-profile-generator?style=for-the-badge&color=blue)](https://github.com/your-username/dynamic-profile-generator/graphs/contributors)
[![GitHub issues](https://img.shields.io/github/issues/your-username/dynamic-profile-generator?style=for-the-badge&color=green)](https://github.com/your-username/dynamic-profile-generator/issues)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](https://github.com/your-username/dynamic-profile-generator/pulls)

---

</div>

## 🚀 Quick Start for Contributors

### 1. **Fork & Clone**
```bash
git clone https://github.com/your-username/dynamic-profile-generator.git
cd dynamic-profile-generator
```

### 2. **Set Up Development Environment**
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install
```

### 3. **Run Tests**
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=.

# Run specific test
pytest tests/test_generator.py
```

### 4. **Make Your Changes**
```bash
# Create feature branch
git checkout -b feature/amazing-feature

# Make your changes...
# Add tests for new features
# Update documentation

# Run tests and linting
pytest
black .
flake8 .
```

### 5. **Submit Pull Request**
```bash
# Commit changes
git add .
git commit -m "✨ Add amazing feature"

# Push to your fork
git push origin feature/amazing-feature

# Create PR on GitHub
```

---

## 📋 Contribution Guidelines

### 🐛 **Reporting Bugs**

1. **Check existing issues** - Search before creating new issues
2. **Use issue templates** - Fill out all required fields
3. **Provide details** - Include steps to reproduce, expected vs actual behavior
4. **Add labels** - Help categorize your issue

### ✨ **Feature Requests**

1. **Describe the problem** - Explain what you're trying to solve
2. **Provide context** - Why is this feature needed?
3. **Suggest implementation** - If you have ideas, share them
4. **Use cases** - Describe how this would be used

### 🔧 **Code Contributions**

#### **Code Style**
- Follow **PEP 8** standards
- Use **Black** for code formatting
- Write descriptive commit messages
- Add docstrings to functions and classes

#### **Testing**
- Write tests for new features
- Ensure all tests pass
- Maintain or improve code coverage
- Test edge cases and error conditions

#### **Documentation**
- Update README if needed
- Add docstrings to new functions
- Update type hints
- Keep examples current

---

## 🎯 **Types of Contributions**

### 🌟 **Code Contributions**
- Bug fixes
- New features
- Performance improvements
- Code refactoring

### 📚 **Documentation**
- README improvements
- Code comments
- Usage examples
- API documentation

### 🎨 **Design & UX**
- Template improvements
- UI/UX enhancements
- New themes
- Responsive design

### 🧪 **Testing**
- Unit tests
- Integration tests
- End-to-end tests
- Test coverage improvements

### 🌐 **Community**
- Issue triage
- Community support
- Documentation translation
- Community outreach

---

## 🏗️ **Development Workflow**

### **Branch Naming Convention**
```
feature/add-new-template
bugfix/fix-banner-rotation
docs/update-readme
test/add-component-tests
refactor/cleanup-code
```

### **Commit Message Format**
```
✨ Add new feature (for new features)
🐛 Fix bug description (for bug fixes)
📚 Update documentation (for docs)
🧪 Add tests (for testing)
🔧 Refactor code (for refactoring)
```

### **Pull Request Process**
1. **Create PR** from your feature branch
2. **Fill out PR template** completely
3. **Link related issues** if applicable
4. **Request review** from maintainers
5. **Address feedback** and make changes
6. **Get approval** and merge

---

## 🧪 **Testing Guidelines**

### **Running Tests**
```bash
# All tests
pytest

# With coverage
pytest --cov=. --cov-report=html

# Specific test file
pytest tests/test_generator.py

# Specific test
pytest tests/test_generator.py::test_generate_readme
```

### **Writing Tests**
```python
import pytest
from profile_generator import generate_readme

def test_generate_readme_basic():
    """Test basic README generation"""
    config = {"user": {"name": "Test User"}}
    result = generate_readme(config)

    assert "Test User" in result
    assert isinstance(result, str)

def test_generate_readme_with_social():
    """Test README generation with social links"""
    config = {
        "user": {"name": "Test User"},
        "social": {"github": "testuser"}
    }
    result = generate_readme(config)

    assert "github.com/testuser" in result
```

---

## 🎨 **Design Guidelines**

### **Template Structure**
- Use semantic HTML
- Ensure mobile responsiveness
- Follow accessibility guidelines
- Maintain consistent styling

### **Color Scheme**
- Primary: `#A855F7` (Purple)
- Secondary: `#6366F1` (Indigo)
- Success: `#10B981` (Emerald)
- Warning: `#F59E0B` (Amber)
- Error: `#EF4444` (Red)

### **Typography**
- Headers: Use emoji + descriptive text
- Body: Clear, concise language
- Code: Proper syntax highlighting
- Links: Descriptive anchor text

---

## 📞 **Getting Help**

### **Communication Channels**
- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: General questions and ideas
- **Discord**: Real-time chat (coming soon!)

### **Asking Questions**
- Check existing documentation first
- Search existing issues/discussions
- Provide context and code examples
- Be specific about your problem

---

## 🙏 **Code of Conduct**

This project follows our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to:

- Be respectful and inclusive
- Focus on constructive feedback
- Accept responsibility for mistakes
- Show empathy towards others
- Help create a positive environment

---

## 🎉 **Recognition**

Contributors will be recognized through:
- **GitHub Contributors** page
- **CHANGELOG.md** entries
- **Release notes** mentions
- **Special acknowledgments** for major contributions

---

<div align="center">

## 📚 **Additional Resources**

- [Project README](README.md)
- [API Documentation](docs/api.md)
- [Development Guide](docs/development.md)
- [Deployment Guide](docs/deployment.md)

---

**Happy Contributing! 🎉**

*Built with ❤️ by the open source community*

</div>