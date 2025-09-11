#!/usr/bin/env python3
"""
Dynamic GitHub Profile Generator
Generates a unique README.md every day with different content
"""

import os
import json
import random
import glob
from datetime import datetime
from templates.components import header, learning, projects, stats, fun

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
                "linkedin": "https://linkedin.com/in/yourprofile"
            }
        }

def generate_daily_content():
    """Generate content that changes daily"""
    today = datetime.now()
    day_of_year = today.timetuple().tm_yday
    
    # Different content based on day of year
    random.seed(day_of_year)
    
    return {
        "color_theme": random.choice(["tokyonight", "radical", "dark", "merko", "onedark"]),
        "fun_fact": random.choice(fun.get_fun_facts()),
        "daily_quote": random.choice(fun.get_quotes()),
        "spotlight_project": random.choice(projects.get_projects())["name"],
        "learning_focus": random.choice(learning.get_learning_topics())
    }

def main():
    """Main function to generate the README"""
    print("🚀 Generating dynamic GitHub profile...")
    
    # Load configuration
    config = load_config()
    
    # Generate daily content
    daily_content = generate_daily_content()
    
    # Build the README content
    content = header.generate(config, daily_content)
    content += learning.generate(config, daily_content)
    content += projects.generate(config, daily_content)
    content += stats.generate(config, daily_content)
    content += fun.generate(config, daily_content)
    
    # Add footer
    content += f"\n---\n\n⭐️ **Last Updated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  \n"
    content += "*This README updates daily with new content!* ✨\n"
    
    # Write to README.md
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)
    
    print("✅ README.md generated successfully!")
    print("🎉 Your profile now has fresh daily content!")

if __name__ == "__main__":
    main()
