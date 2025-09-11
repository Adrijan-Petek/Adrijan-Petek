def get_fun_facts():
    return [
        "I believe every project gets better with memes 😎",
        "I can solve a Rubik's cube in under 2 minutes!",
        "I once coded for 36 hours straight during a hackathon",
        "My first programming language was Python 🐍",
        "I'm passionate about decentralized technologies",
        "I enjoy contributing to open source projects"
    ]

def get_quotes():
    return [
        "The only way to learn programming is by writing programs.",
        "Code is like humor. When you have to explain it, it's bad.",
        "First, solve the problem. Then, write the code.",
        "The best error message is the one that never shows up.",
        "Programming isn't about what you know; it's about what you can figure out."
    ]

def generate(config, daily_content):
    # Different cat images based on day of week
    cat_types = ["gif", "jpg", "png"]
    cat_url = f"https://cataas.com/cat/{random.choice(cat_types)}"
    
    return f"""
## ✨ Fun Section
![Random Cat]({cat_url})  
*"{daily_content['fun_fact']}"*  

**Quote of the Day**: "{daily_content['daily_quote']}" 💭

### 🎲 Today's Developer Challenge:
Try implementing a {random.choice(['function', 'class', 'algorithm', 'UI component'])} using {random.choice(['Python', 'TypeScript', 'Solidity'])}!

---
"""
