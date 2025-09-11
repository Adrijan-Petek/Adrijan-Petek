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
        {"border": "12px", "shadow": "0 6px 12px rgba(79, 70, 229, 0.3)", "border_color": "#4F46E5", "filter": "brightness(1.05)"},
        {"border": "10px", "shadow": "0 8px 20px rgba(0,0,0,0.4)", "transform": "rotate(-1deg)", "filter": "contrast(1.1)"},
        {"border": "8px", "shadow": "0 4px 8px rgba(0,0,0,0.2)", "border_style": "dashed", "border_color": "#6366F1", "filter": "saturate(1.2)"},
        {"border": "20px", "shadow": "0 10px 25px rgba(139, 92, 246, 0.3)", "border_color": "#8B5CF6", "filter": "hue-rotate(10deg)"},
        {"border": "0px", "shadow": "0 12px 30px rgba(0,0,0,0.5)", "filter": "sepia(0.2)"},
        {"border": "25px", "shadow": "none", "border_color": "#10B981", "filter": "drop-shadow(0 8px 16px rgba(16, 185, 129, 0.3))"}
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

def get_daily_emoji_divider():
    """Return different emoji dividers each day"""
    dividers = [
        "⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️",
        "✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨",
        "🌟🌠🌟🌠🌟🌠🌟🌠🌟🌠🌟🌠🌟🌠🌟🌠🌟🌠🌟🌠🌟🌠🌟🌠",
        "🚀💫🚀💫🚀💫🚀💫🚀💫🚀💫🚀💫🚀💫🚀💫🚀💫",
        "⭐🔥⭐🔥⭐🔥⭐🔥⭐🔥⭐🔥⭐🔥⭐🔥⭐🔥⭐🔥⭐🔥",
        "🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰",
        "🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯"
    ]
    return random.choice(dividers)

def generate(config, daily_content):
    today = datetime.now()
    day_of_year = today.timetuple().tm_yday
    random.seed(day_of_year)
    
    banner_style = get_daily_banner_style()
    daily_intro = get_daily_intro()
    emoji_divider = get_daily_emoji_divider()
    
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

<div align="center">

{emoji_divider}

# 👋 Hi, I'm {config['user']['name']}

{daily_intro}

Currently working on [Mobb Chain]({config['user']['website']}) and experimenting with Farcaster mini apps 🌐.  
I document my learning journey in Python, Solidity, Web Development, and Blockchain projects in this repository and others 📂 [python-beginners]({config['user']['learning_repo']}).  

**Connect with me:** [X/Twitter]({config['social']['x']}) • [LinkedIn]({config['social']['linkedin']}) • [Farcaster]({config['social']['farcaster']})

</div>

---
"""
