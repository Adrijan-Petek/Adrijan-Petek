import random
from datetime import datetime

def get_fun_facts():
    return [
        "I believe every project gets better with memes 😎",
        "I can solve a Rubik's cube in under 2 minutes!",
        "I once coded for 36 hours straight during a hackathon",
        "My first programming language was Python 🐍",
        "I'm passionate about decentralized technologies",
        "I enjoy contributing to open source projects",
        "I'm a night owl coder 🌙",
        "Coffee is my primary fuel source ☕"
    ]

def get_quotes():
    return [
        "The only way to learn programming is by writing programs.",
        "Code is like humor. When you have to explain it, it's bad.",
        "First, solve the problem. Then, write the code.",
        "The best error message is the one that never shows up.",
        "Programming isn't about what you know; it's about what you can figure out.",
        "The most disastrous thing that you can ever learn is your first programming language.",
        "Truth can only be found in one place: the code.",
        "Any fool can write code that a computer can understand. Good programmers write code that humans can understand."
    ]

def get_cat_gifs():
    """Return reliable cat GIF URLs"""
    return [
        "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif",
        "https://media.giphy.com/media/13CoXDiaCcCoyk/giphy.gif",
        "https://media.giphy.com/media/jpbnoe3UIa8TU8LM13/giphy.gif",
        "https://media.giphy.com/media/5i7umUqAOYYEw/giphy.gif",
        "https://media.giphy.com/media/VRKheDy4DkBMrQm66p/giphy.gif",
    ]

def get_programming_memes():
    """Return reliable programming meme URLs"""
    return [
        "https://i.redd.it/6y5v2hb5f0q61.jpg",
        "https://i.redd.it/9qeb3d5y5jq61.jpg",
        "https://i.redd.it/iznunu4f8jq61.jpg",
        "https://i.redd.it/6fg0b0h98jq61.jpg",
        "https://i.redd.it/9eb22v48cjq61.jpg",
        "https://i.redd.it/6n1j1e3y8jq61.jpg",
        "https://i.redd.it/9qeb3d5y5jq61.jpg",
        "https://i.redd.it/iznunu4f8jq61.jpg",
    ]

def generate(config, daily_content):
    try:
        today = datetime.now()
        day_of_year = today.timetuple().tm_yday
        random.seed(day_of_year)
        
        # Alternate between cat GIFs and programming memes
        if day_of_year % 2 == 0:
            media_url = random.choice(get_cat_gifs())
            alt_text = "Random Cat"
            media_type = "gif"
        else:
            media_url = random.choice(get_programming_memes())
            alt_text = "Programming Meme"
            media_type = "meme"
        
        challenge_types = ['function', 'class', 'algorithm', 'UI component', 'API endpoint', 'smart contract']
        languages = ['Python', 'TypeScript', 'Solidity', 'JavaScript', 'Java', 'Rust']
        
        return f"""
## ✨ Fun Section

![{alt_text}]({media_url})  
*"{daily_content['fun_fact']}"*  

**Quote of the Day**: "{daily_content['daily_quote']}" 💭

### 🎲 Today's Developer Challenge:
Try implementing a **{random.choice(challenge_types)}** using **{random.choice(languages)}**!

### 🔥 Developer Meme of the Day
![Dev Meme]({random.choice(get_programming_memes())})

---
"""
    except Exception as e:
        # Fallback if there's any error
        print(f"Error in fun section: {e}")
        return f"""
## ✨ Fun Section
*"{daily_content['fun_fact']}"*  

**Quote of the Day**: "{daily_content['daily_quote']}" 💭

### 🎲 Today's Developer Challenge:
Try implementing a new function using Python!

---
"""
