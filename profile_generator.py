#!/usr/bin/env python3
"""
Dynamic GitHub Profile Generator
Generates a unique README.md every day with different content

Repository: https://github.com/Adrijan-Petek/Adrijan-Petek.git
Last updated: 2025-12-09 11:00:00 UTC
"""

import os
import json
import random
import glob
from datetime import datetime
from templates.components import header, learning, projects, stats  # , fun


def load_config():
    """Load configuration from JSON file"""
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        # Default configuration
        return {
            "user": {
                "name": "Adrijan Petek",
                "github": "Adrijan-Petek",
                "website": "https://www.mobbchain.xyz",
                "learning_repo": "https://github.com/Adrijan-Petek/python-beginners"
            },
            "social": {
                "farcaster": "https://farcaster.xyz/adrijan",
                "x": "https://x.com/adrijan_petek",
                "zora": "https://zora.co/@adrijan"
            }
        }


def generate_daily_content():
    """Generate content that changes daily"""
    today = datetime.now()
    day_of_year = today.timetuple().tm_yday

    # Different content based on day of year
    random.seed(day_of_year)

    return {
        "color_theme": "tokyonight",  # Fixed to black theme
        "spotlight_project": random.choice(projects.get_projects())["name"],
        "learning_focus": random.choice(learning.get_learning_topics()),
        "theme": {
            "primary": "#000000",
            "secondary": "#1a1a1a",
            "accent": "#333333",
            "text": "#ffffff",
            "background": "#0d1117"
        }
    }


def main():
    """Main function to generate the README"""
    print("🚀 Generating dynamic GitHub profile...")

    # Load configuration
    config = load_config()

    # Generate daily content
    daily_content = generate_daily_content()

    # Use template-based generation for comprehensive README
    print("📄 Generating comprehensive README with templates...")

    content = header.generate(config, daily_content)
    content += learning.generate(config, daily_content)
    content += projects.generate(config, daily_content)
    content += stats.generate(config, daily_content)
    # content += fun.generate(config, daily_content)  # Temporarily disabled due to file corruption

    # Add footer
    content += f"\n---\n\n⭐️ **Last Updated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  \n"
    content += "*This README updates daily with new content!* ✨\n"

    # Write to README.md
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

    print("✅ README.md generated successfully!")
    print("🎉 Your profile now has fresh daily content!")


def update_html_dynamic_content(html_content, config, daily_content):
    """Update dynamic content in the HTML README"""
    import re
    from datetime import datetime

    # Update the last updated timestamp
    current_time = datetime.now().strftime('%B %d, %Y')
    html_content = re.sub(
        r'⭐️ <strong>Last Updated:</strong> [^<]+',
        f'⭐️ <strong>Last Updated:</strong> {current_time}',
        html_content
    )

    # Update the spotlight project if available
    if 'spotlight_project' in daily_content:
        project_name = daily_content['spotlight_project']
        spotlight_html = f'''
        <div style="background: linear-gradient(135deg, rgba(255, 107, 107, 0.1), rgba(78, 205, 196, 0.1)); border: 1px solid rgba(255, 107, 107, 0.3); border-radius: 15px; padding: 20px; margin: 20px 0; text-align: center;">
            <h3 style="color: #ff6b6b; margin-bottom: 10px;">🌟 Spotlight Project</h3>
            <p style="color: #a0aec0; margin-bottom: 0; font-size: 1.1rem; font-weight: 500;">{project_name}</p>
        </div>
        '''

        # Insert spotlight after the current focus section
        html_content = re.sub(
            r'(<div style="background: linear-gradient[^>]+>.*?🎯 Current Focus:[^<]+.*?</div>)',
            r'\1' + spotlight_html,
            html_content,
            flags=re.DOTALL
        )

    # Update daily quote if available
    if 'daily_quote' in daily_content:
        quote = daily_content['daily_quote']
        html_content = re.sub(
            r'<p style="color: #a0aec0; margin-bottom: 0;">Deep diving into DeFi protocols[^<]*</p>',
            f'<p style="color: #a0aec0; margin-bottom: 0;">{quote}</p>',
            html_content
        )

    return html_content


if __name__ == "__main__":
    main()
