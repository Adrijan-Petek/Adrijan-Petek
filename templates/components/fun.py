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
        "https://media.giphy.com/media/3o72FfM5HJydzafgUE/giphy.gif",
        "https://media.giphy.com/media/3o7aD2vscsx8lPRyI0/giphy.gif",
        "https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif",
        "https://media.giphy.com/media/3o7TKsQ8UQ4l4LhGis/giphy.gif",
        "https://media.giphy.com/media/3o7TKwxYkeW0ZvTqsU/giphy.gif",
        "https://media.giphy.com/media/3o7TKtipfPVLkfQdAI/giphy.gif",
        "https://media.giphy.com/media/3o7TKsQ8UQ4l4LhGis/giphy.gif"
    ]

def get_programming_gifs():
    """Return programming-related GIFs"""
    return [
        "https://media.giphy.com/media/LmNwrBhejkK9EFP504/giphy.gif",  # Coding cat
        "https://media.giphy.com/media/coxQHKASG60HrHtvkt/giphy.gif",  # Developer
        "https://media.giphy.com/media/ZVik7pBtu9dNS/giphy.gif",      # Computer cat
        "https://media.giphy.com/media/l0HU7JI1m1eEwz7Kw/giphy.gif",  # Typing cat
        "https://media.giphy.com/media/3o7aTskHEUdgCQAXde/giphy.gif", # Keyboard cat
    ]

def generate(config, daily_content):
    try:
        today = datetime.now()
        day_of_year = today.timetuple().tm_yday
        random.seed(day_of_year)
        
        # Alternate between cat GIFs and programming GIFs
        if day_of_year % 2 == 0:
            gif_url = random.choice(get_cat_gifs())
            alt_text = "Random Cat"
        else:
            gif_url = random.choice(get_programming_gifs())
            alt_text = "Programming Fun"
        
        challenge_types = ['function', 'class', 'algorithm', 'UI component', 'API endpoint', 'smart contract']
        languages = ['Python', 'TypeScript', 'Solidity', 'JavaScript', 'Java', 'Rust']
        
        return f"""
## ✨ Fun Section

![{alt_text}]({gif_url})  
*"{daily_content['fun_fact']}"*  

**Quote of the Day**: "{daily_content['daily_quote']}" 💭

### 🎲 Today's Developer Challenge:
Try implementing a **{random.choice(challenge_types)}** using **{random.choice(languages)}**!

### 🔥 Developer Meme
![Dev Meme](https://programming-memes-images.s3.amazonaws.com/meme-{random.randint(1, 50)}.jpg)

---
"""
    except Exception as e:
        # Fallback if there's any error
        return f"""
## ✨ Fun Section
*"{daily_content['fun_fact']}"*  

**Quote of the Day**: "{daily_content['daily_quote']}" 💭

### 🎲 Today's Developer Challenge:
Try implementing a new function using Python!

---
"""
