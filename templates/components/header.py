def generate(config, daily_content):
    return f"""
{daily_content['ascii_art']}

# 👋 Hi, I'm {config['user']['name']}  

🚀 **Builder | Full-Stack Developer | Crypto Enthusiast**  
Currently working on [Mobb Chain]({config['user']['website']}) and experimenting with Farcaster mini apps 🌐.  
I document my learning journey in Python, Solidity, Web Development, and Blockchain projects in this repository and others 📂 [python-beginners]({config['user']['learning_repo']}).  

---

"""
