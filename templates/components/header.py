import random
from datetime import datetime

def get_header_images():
    """Return a list of header image URLs"""
    return [
        "https://images.unsplash.com/photo-1542831371-29b0f74f9713?w=800&q=80",  # Code
        "https://images.unsplash.com/photo-1627398242454-45a1465c2479?w=800&q=80",  # Blockchain
        "https://images.unsplash.com/photo-1633356122544-f134324a6cee?w=800&q=80",  # React
        "https://images.unsplash.com/photo-1555949963-aa79dcee981c?w=800&q=80",  # TypeScript
        "https://images.unsplash.com/photo-1546054454-aa26e2b734c7?w=800&q=80",  # Python
    ]

def get_banner_style():
    """Return different banner styles"""
    styles = [
        "border-radius: 15px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);",
        "border-radius: 10px; border: 3px solid #2D3748;",
        "border-radius: 20px; box-shadow: 0 6px 12px rgba(0,0,0,0.3); transform: rotate(-1deg);",
        "border: 2px dashed #4A5568; border-radius: 8px;",
        "border-radius: 12px; box-shadow: 0 8px 16px rgba(0,0,0,0.4);"
    ]
    return random.choice(styles)

def generate(config, daily_content):
    today = datetime.now()
    day_of_year = today.timetuple().tm_yday
    random.seed(day_of_year)
    
    header_image = random.choice(get_header_images())
    banner_style = get_banner_style()
    
    return f"""
<div align="center">
  <img src="{header_image}" alt="Header" style="width: 100%; max-height: 300px; object-fit: cover; {banner_style}" />
</div>

{daily_content['ascii_art']}

# 👋 Hi, I'm {config['user']['name']}  

🚀 **Builder | Full-Stack Developer | Crypto Enthusiast**  
Currently working on [Mobb Chain]({config['user']['website']}) and experimenting with Farcaster mini apps 🌐.  
I document my learning journey in Python, Solidity, Web Development, and Blockchain projects in this repository and others 📂 [python-beginners]({config['user']['learning_repo']}).  

---

"""
