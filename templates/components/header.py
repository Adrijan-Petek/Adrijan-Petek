import random
from datetime import datetime

def get_daily_banner():
    """Return different text banners each day"""
    banners = [
        """
<div align="center">

# 🚀 Adrijan Petek 
### **Full-Stack Developer | Blockchain Enthusiast**
⭐️ Building the future of web3 at [Mobb Chain](https://www.mobbchain.xyz)

</div>
""",
        """
<div align="center">

# 💻 Code • Create • Innovate
### **Passionate about Python, Solidity, and Web Development**
🌐 Exploring the future of decentralized applications

</div>
""",
        """
<div align="center">

# 🔥 Turning Ideas into Reality
### **Blockchain Developer & Crypto Enthusiast**
🚀 Daily coding adventures and learning journeys

</div>
""",
        """
<div align="center">

# ⚡ Energy Through Code
### **Building solutions that make a difference**
🎯 Focused on Python, Web3, and innovative tech

</div>
"""
    ]
    return random.choice(banners)

def generate(config, daily_content):
    today = datetime.now()
    day_of_year = today.timetuple().tm_yday
    random.seed(day_of_year)
    
    banner = get_daily_banner()
    
    return f"""
{banner}

{daily_content['ascii_art']}

# 👋 Hi, I'm {config['user']['name']}  

🚀 **Builder | Full-Stack Developer | Crypto Enthusiast**  
Currently working on [Mobb Chain]({config['user']['website']}) and experimenting with Farcaster mini apps 🌐.  
I document my learning journey in Python, Solidity, Web Development, and Blockchain projects in this repository and others 📂 [python-beginners]({config['user']['learning_repo']}).  

---

"""
