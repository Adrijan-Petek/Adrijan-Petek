import random
from datetime import datetime
from pathlib import Path

# Folder with visual art images (PNG/JPG)
ART_FOLDER = Path(".github/readme-art")

# Daily quotes
FUN_QUOTES = [
    "Code, coffee, repeat ☕💻",
    "Every day is a good day to code 🚀",
    "Memes make coding better 😎",
    "Keep calm and deploy on Mobb Chain 🔗",
    "Cats > Bugs 🐱"
]

# Header image
HEADER_IMAGE = "./github-header.png"

def get_random_art():
    arts = list(ART_FOLDER.glob("*.*"))
    if not arts:
        return ""
    return random.choice(arts)

def generate_readme():
    date_today = datetime.utcnow().strftime("%Y-%m-%d")
    art_image = get_random_art()
    quote = random.choice(FUN_QUOTES)
    
    content = f"""![Header]({HEADER_IMAGE})

# 👋 Hi, I'm Adrijan Petek  

🚀 **Builder | Full-Stack Developer | Crypto Enthusiast**  
Currently working on [Mobb Chain](https://mobbchain.xyz) and experimenting with Farcaster mini apps 🌐.

---

## 🎨 Daily Visual Art
![Daily Art]({art_image})  

💡 *{quote}*

---

_Last updated on {date_today} UTC_

⭐️ From [Adrijan-Petek](https://github.com/Adrijan-Petek)
"""
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ README.md updated with daily art!")

if __name__ == "__main__":
    generate_readme()
