import random
from datetime import datetime
import os
import glob

def get_random_banner():
    """Get a random banner image from the img folder"""
    banner_files = glob.glob("img/github-header-banner*.png")
    
    if not banner_files:
        # Fallback if no banner images found
        return None
    
    # Return a random banner file
    return random.choice(banner_files)

def get_daily_banner_style():
    """Return different banner styles each day"""
    styles = [
        {"border": "15px", "shadow": "0 8px 16px rgba(0,0,0,0.3)", "filter": "none"},
        {"border": "12px", "shadow": "0 6px 12px rgba(26, 26, 26, 0.3)", "border_color": "#1a1a1a", "filter": "brightness(1.05)"},
        {"border": "10px", "shadow": "0 8px 20px rgba(0,0,0,0.4)", "transform": "rotate(-1deg)", "filter": "contrast(1.1)"},
        {"border": "8px", "shadow": "0 4px 8px rgba(0,0,0,0.2)", "border_style": "dashed", "border_color": "#333333", "filter": "saturate(1.2)"},
        {"border": "20px", "shadow": "0 10px 25px rgba(51, 51, 51, 0.3)", "border_color": "#000000", "filter": "hue-rotate(10deg)"},
        {"border": "0px", "shadow": "0 12px 30px rgba(0,0,0,0.5)", "filter": "sepia(0.2)"},
        {"border": "25px", "shadow": "none", "border_color": "#1a1a1a", "filter": "drop-shadow(0 8px 16px rgba(26, 26, 26, 0.3))"}
    ]
    return random.choice(styles)

def get_daily_intro():
    """Return different introduction styles each day"""
    intros = [
        "🚀 **Full-Stack Developer | Blockchain Builder | Crypto Enthusiast**",
        "💻 **Ruby | TypeScript | Python Developer**",
        "🔗 **Building the Future of Web3 & Blockchain**",
        "⭐️ **Passionate Coder & Continuous Learner**",
        "🌐 **Creating Innovative Digital Solutions**",
        "⚡ **Full-Stack Developer & Web3 Explorer**",
        "🎯 **Focused on Quality Code & User Experience**",
        "🔥 **Turning Ideas into Production-Ready Applications**"
    ]
    return random.choice(intros)

def get_daily_badges():
    """Return different professional badges each day"""
    badge_sets = [
        "![Profile Views](https://komarev.com/ghpvc/?username=Adrijan-Petek&color=blue&style=for-the-badge) ![GitHub followers](https://img.shields.io/github/followers/Adrijan-Petek?color=blue&style=for-the-badge)",
        "![Stars](https://img.shields.io/github/stars/Adrijan-Petek?color=yellow&style=for-the-badge) ![Forks](https://img.shields.io/github/forks/Adrijan-Petek/python-beginners?color=green&style=for-the-badge)",
        "![Open Source](https://img.shields.io/badge/Open%20Source-❤️-red?style=for-the-badge) ![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=for-the-badge)",
        "![Made with Love](https://img.shields.io/badge/Made%20with-❤️-red?style=for-the-badge) ![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge)",
        "![Blockchain](https://img.shields.io/badge/Blockchain-Web3-blue?style=for-the-badge) ![Smart Contracts](https://img.shields.io/badge/Smart%20Contracts-Solidity-orange?style=for-the-badge)"
    ]
    return random.choice(badge_sets)

def get_daily_typing_color():
    """Return different typing animation colors each day"""
    colors = [
        "2563EB",  # Blue
        "DC2626",  # Red
        "16A34A",  # Green
        "EA580C",  # Orange
        "7C3AED",  # Purple
        "0891B2",  # Cyan
        "BE123C",  # Rose
        "65A30D",  # Lime
        "C2410C",  # Amber
        "7C2D12",  # Brown
        "365314",  # Olive
        "1E40AF",  # Indigo
        "7E22CE",  # Fuchsia
        "0F766E",  # Teal
        "92400E",  # Yellow
        "B91C1C",  # Crimson
        "15803D",  # Emerald
        "C2410C",  # Orange-red
        "6B21A8",  # Violet
        "0369A1"   # Sky blue
    ]
def get_daily_contribution_color():
    """Return different contribution graph colors each day"""
    colors = [
        "github",      # Default GitHub theme
        "github-light", # Light theme
        "dark",        # Dark theme
        "merko",       # Merko theme
        "gruvbox",     # Gruvbox theme
        "tokyo-night", # Tokyo Night theme
        "onedark",     # One Dark theme
        "cobalt",      # Cobalt theme
        "synthwave",   # Synthwave theme
        "high-contrast", # High Contrast theme
        "dracula",     # Dracula theme
        "prussian",    # Prussian theme
        "monokai",     # Monokai theme
        "vue",         # Vue theme
        "vue-dark",    # Vue Dark theme
        "shades-of-purple", # Shades of Purple theme
        "nightowl",    # Night Owl theme
        "buefy",       # Buefy theme
        "blue-green",  # Blue Green theme
        "algolia",     # Algolia theme
        "great-gatsby", # Great Gatsby theme
        "darcula",     # Darcula theme
        "bear",        # Bear theme
        "solarized-dark", # Solarized Dark theme
        "solarized-light", # Solarized Light theme
        "chartreuse-dark", # Chartreuse Dark theme
        "nord",        # Nord theme
        "gotham",      # Gotham theme
        "material",    # Material theme
        "outlook",     # Outlook theme
        "codeSTACKr",  # CodeSTACKr theme
        "rose-pine",   # Rose Pine theme
        "catppuccin-mocha" # Catppuccin Mocha theme
    ]
    return random.choice(colors)

def get_daily_typing_lines():
    """Return different typing animation lines each day"""
    line_sets = [
        "Generate+Beautiful+READMEs;Professional+Documentation;Automated+Repository+Analysis;Social+Media+Integration",
        "Full-Stack+Developer;Blockchain+Builder;Crypto+Enthusiast;Continuous+Learner",
        "Python+Master;TypeScript+Expert;Web3+Innovator;Open+Source+Contributor",
        "Code+Quality+Advocate;UI/UX+Designer;Tech+Blog+Writer;Community+Builder",
        "Smart+Contract+Developer;DApp+Creator;DeFi+Explorer;NFT+Artist",
        "AI+Integration+Specialist;Cloud+Architecture;DevOps+Engineer;Agile+Practitioner",
        "Mobile+App+Developer;Cross-Platform+Expert;Performance+Optimizer;Security+Focused"
    ]
    return random.choice(line_sets)

def get_daily_contribution_color():
    """Return different contribution graph colors each day"""
    colors = [
        "github",      # Default GitHub theme
        "github-light", # Light theme
        "dark",        # Dark theme
        "merko",       # Merko theme
        "gruvbox",     # Gruvbox theme
        "tokyo-night", # Tokyo Night theme
        "onedark",     # One Dark theme
        "cobalt",      # Cobalt theme
        "synthwave",   # Synthwave theme
        "high-contrast", # High Contrast theme
        "dracula",     # Dracula theme
        "prussian",    # Prussian theme
        "monokai",     # Monokai theme
        "vue",         # Vue theme
        "vue-dark",    # Vue Dark theme
        "shades-of-purple", # Shades of Purple theme
        "nightowl",    # Night Owl theme
        "buefy",       # Buefy theme
        "blue-green",  # Blue Green theme
        "algolia",     # Algolia theme
        "great-gatsby", # Great Gatsby theme
        "darcula",     # Darcula theme
        "bear",        # Bear theme
        "solarized-dark", # Solarized Dark theme
        "solarized-light", # Solarized Light theme
        "chartreuse-dark", # Chartreuse Dark theme
        "nord",        # Nord theme
        "gotham",      # Gotham theme
        "material",    # Material theme
        "outlook",     # Outlook theme
        "codeSTACKr",  # CodeSTACKr theme
        "rose-pine",   # Rose Pine theme
        "catppuccin-mocha" # Catppuccin Mocha theme
    ]
    return random.choice(colors)

def generate(config, daily_content):
    today = datetime.now()
    day_of_year = today.timetuple().tm_yday
    random.seed(day_of_year)
    
    banner_style = get_daily_banner_style()
    daily_intro = get_daily_intro()
    daily_badges = get_daily_badges()
    typing_lines = get_daily_typing_lines()
    typing_color = get_daily_typing_color()
    contribution_color = get_daily_contribution_color()
    
    # Get random banner image
    banner_path = get_random_banner()
    banner_html = ""
    
    if banner_path:
        banner_html = f"""
<div align="center">
  <img src="{banner_path}" alt="Header Banner" style="
    width: 100%; 
    max-height: 280px; 
    object-fit: cover; 
    border-radius: {banner_style['border']};
    box-shadow: {banner_style['shadow']};
    {'border: 3px ' + banner_style.get('border_style', 'solid') + ' ' + banner_style.get('border_color', '#2D3748') + ';' if 'border_style' in banner_style or 'border_color' in banner_style else ''}
    {'transform: ' + banner_style.get('transform', '') + ';' if 'transform' in banner_style else ''}
    {'filter: ' + banner_style.get('filter', '') + ';' if 'filter' in banner_style else ''}
    margin-bottom: 1.5rem;
  " />
</div>
"""
    else:
        # Fallback text banner if no images found
        banner_html = """
<div align="center" style="
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 2.5rem;
    border-radius: 15px;
    margin-bottom: 2rem;
    color: white;
    box-shadow: 0 8px 20px rgba(0,0,0,0.2);
">
  <h1 style="margin: 0; font-size: 2.5rem;">🚀 Building the Future</h1>
  <h3 style="margin: 0.5rem 0 0 0; font-weight: 300;">Fullstack developer: Ruby, TypeScript & Python</h3>
</div>
"""
    
    return f"""
{banner_html}

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=32&duration=2800&pause=2000&color=000000&center=true&vCenter=true&width=940&lines={typing_lines}" alt="Typing SVG" />
</p>

<div align="center">

{daily_badges}

# 👋 Hi, I'm {config['user']['name']}

{daily_intro}

Experimenting with **Farcaster mini apps** 🌐 and exploring innovative blockchain solutions.  
I document my learning journey in **Python**, **Solidity**, **Web Development**, and **Blockchain projects** across this repository and others 📂 [python-beginners]({config['user']['learning_repo']}).  

**🌍 Connect with me:** [X/Twitter]({config['social']['x']}) • [Zora Badge]({config['social']['zora']}) • [Farcaster]({config['social']['farcaster']}){' • [Website](' + config['user']['website'] + ')' if config['user'].get('website') else ''}

</div>

---
"""
