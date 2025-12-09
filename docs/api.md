# API Documentation

<!-- Repository: https://github.com/Adrijan-Petek/Adrijan-Petek.git -->
<!-- Last updated: 2025-12-09 11:00:00 UTC -->

## Overview

The Dynamic GitHub Profile Generator provides a simple API for generating personalized GitHub profile READMEs programmatically.

## Core Functions

### `load_config() -> dict`

Loads configuration from `config.json` file.

**Returns:**
- Dictionary containing configuration data

**Raises:**
- `FileNotFoundError`: If config.json is not found
- `json.JSONDecodeError`: If config.json is invalid JSON

**Example:**
```python
from profile_generator import load_config

config = load_config()
print(config['user']['name'])
```

### `generate_daily_content() -> dict`

Generates content that changes daily based on the current date.

**Returns:**
- Dictionary with daily content including:
  - `color_theme`: Selected theme for the day
  - `spotlight_project`: Featured project name
  - `learning_focus`: Current learning topic

**Example:**
```python
from profile_generator import generate_daily_content

content = generate_daily_content()
print(f"Today's theme: {content['color_theme']}")
```

### `main() -> None`

Main entry point that generates the complete README.md file.

**Side Effects:**
- Writes to `README.md` file
- Prints progress messages to stdout

**Example:**
```python
from profile_generator import main

# Generate README
main()
print("README generated successfully!")
```

## Template System

### Component Structure

All template components follow the same interface:

```python
def generate(config: dict, daily_content: dict) -> str:
    """
    Generate HTML/markdown content for this component.

    Args:
        config: User configuration dictionary
        daily_content: Daily varying content dictionary

    Returns:
        String containing the component's content
    """
    return "Component content here"
```

### Available Components

#### Header Component (`templates.components.header`)

Generates the profile header with:
- Typing animation
- Banner images
- User introduction
- Social links

#### Learning Component (`templates.components.learning`)

Displays learning progress with:
- Technology categories
- Progress indicators
- Current focus areas

#### Projects Component (`templates.components.projects`)

Showcases featured projects with:
- Project descriptions
- Links to repositories
- Dynamic spotlight selection

#### Stats Component (`templates.components.stats`)

GitHub statistics display with:
- Contribution graphs
- Achievement badges
- Activity metrics

## Configuration Schema

### User Configuration

```json
{
  "user": {
    "name": "string",           // Required: Full display name
    "github": "string",         // Required: GitHub username
    "website": "string",        // Optional: Personal website
    "learning_repo": "string"   // Optional: Learning repository URL
  }
}
```

### Social Links

```json
{
  "social": {
    "twitter": "string",        // Twitter profile URL
    "linkedin": "string",       // LinkedIn profile URL
    "devto": "string",          // Dev.to profile URL
    "farcaster": "string"       // Farcaster profile URL
  }
}
```

### Tech Stack

```json
{
  "tech_stack": ["string"],      // Array of technology names
}
```

### Learning Paths

```json
{
  "learning_paths": {
    "category": ["topic1", "topic2"]  // Category-based learning topics
  }
}
```

## Error Handling

The generator includes comprehensive error handling:

- **Configuration Errors**: Invalid JSON or missing required fields
- **File System Errors**: Missing template files or permission issues
- **Network Errors**: Failed external API calls (future feature)
- **Template Errors**: Invalid template syntax or missing components

## Performance Considerations

- **Memory Usage**: Minimal memory footprint (< 50MB)
- **Execution Time**: < 2 seconds for typical configurations
- **File I/O**: Optimized for frequent reads/writes
- **Caching**: Daily content cached to avoid recalculation

## Extensibility

### Adding Custom Components

1. Create a new file in `templates/components/`
2. Implement the `generate(config, daily_content)` function
3. Import and add to the main generator
4. Update configuration schema if needed

### Custom Themes

1. Add theme definitions to daily content generation
2. Update template components to use theme variables
3. Test across different GitHub display modes

## Testing

Run the test suite:

```bash
# Unit tests
pytest tests/

# With coverage
pytest --cov=. --cov-report=html

# Specific test
pytest tests/test_generator.py::TestConfig::test_load_config
```

## Troubleshooting

### Common Issues

**"config.json not found"**
- Ensure `config.json` exists in the project root
- Copy from `config.example.json` if needed

**"Template import error"**
- Check that all template files exist
- Verify Python path includes project directory

**"Permission denied"**
- Ensure write permissions for README.md
- Check file system permissions

### Debug Mode

Enable debug logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Version History

- **2.1.0**: Enhanced API documentation, improved error handling
- **2.0.0**: Complete API redesign, modular architecture
- **1.5.0**: Basic API stabilization
- **1.0.0**: Initial API release