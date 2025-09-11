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
    """Return reliable cat GIF URLs from giphy"""
    return [
        "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif",
        "https://media.giphy.com/media/13CoXDiaCcCoyk/giphy.gif",
        "https://media.giphy.com/media/jpbnoe3UIa8TU8LM13/giphy.gif",
        "https://media.giphy.com/media/5i7umUqAOYYEw/giphy.gif",
        "https://media.giphy.com/media/VRKheDy4DkBMrQm66p/giphy.gif",
        "https://media.giphy.com/media/3o72FfM5HJydzafgUE/giphy.gif",
        "https://media.giphy.com/media/3o7aD2vscsx8lPRyI0/giphy.gif",
        "https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif"
    ]

def get_programming_memes():
    """Return reliable programming meme URLs from imgur and other trusted sources"""
    return [
        "https://i.imgur.com/B0qYQaV.png",  # Programming meme 1
        "https://i.imgur.com/uUj7C3V.png",  # Programming meme 2
        "https://i.imgur.com/3Q7Yc4x.png",  # Programming meme 3
        "https://i.imgur.com/9E0A7Tk.png",  # Programming meme 4
        "https://i.imgur.com/5M2Ww0a.png",  # Programming meme 5
        "https://i.imgur.com/8K3vL4Z.png",  # Programming meme 6
        "https://i.imgur.com/2F4x8J9.png",  # Programming meme 7
        "https://i.imgur.com/6H9qL3R.png",  # Programming meme 8
        "https://i.imgur.com/4T2vW7c.png",  # Programming meme 9
        "https://i.imgur.com/7J8kP1M.png",  # Programming meme 10
        "https://i.imgur.com/1K3bV9N.png",  # Programming meme 11
        "https://i.imgur.com/9L2rW4X.png"   # Programming meme 12
    ]

def get_dev_challenges():
    """Return development challenges"""
    challenges = [
        {"type": "API endpoint", "language": "Python", "description": "Create a REST API endpoint with FastAPI"},
        {"type": "smart contract", "language": "Solidity", "description": "Build an ERC-20 token contract"},
        {"type": "UI component", "language": "TypeScript", "description": "Create a responsive React component"},
        {"type": "algorithm", "language": "Python", "description": "Implement a sorting algorithm from scratch"},
        {"type": "function", "language": "JavaScript", "description": "Write a pure function with unit tests"},
        {"type": "class", "language": "Java", "description": "Design a class with inheritance and polymorphism"}
    ]
    return random.choice(challenges)

def generate(config, daily_content):
    try:
        today = datetime.now()
        day_of_year = today.timetuple().tm_yday
        random.seed(day_of_year)
        
        # Get media content
        if day_of_year % 2 == 0:
            media_url = random.choice(get_cat_gifs())
            alt_text = "Daily Cat"
            media_caption = "😺 Here's your daily dose of cuteness!"
        else:
            media_url = random.choice(get_programming_memes())
            alt_text = "Dev Meme"
            media_caption = "😂 Programming humor of the day!"
        
        # Get challenge
        challenge = get_dev_challenges()
        
        return f"""
## ✨ Fun Section

### {media_caption}
![{alt_text}]({media_url})  

*"{daily_content['fun_fact']}"*  

**💭 Quote of the Day**: "{daily_content['daily_quote']}"

### 🎲 Today's Developer Challenge:
**Build a {challenge['type']}** using **{challenge['language']}**  
*{challenge['description']}*

### 🔥 Coding Tip:
{random.choice([
    "Always write tests for your code!",
    "Keep your functions small and focused.",
    "Document your code as you write it.",
    "Use version control for every project.",
    "Learn to read error messages carefully.",
    "Take breaks to avoid burnout."
])}

---
"""
    except Exception as e:
        # Fallback if there's any error
        print(f"Error in fun section: {e}")
        return f"""
## ✨ Fun Section

*"{daily_content['fun_fact']}"*  

**💭 Quote of the Day**: "{daily_content['daily_quote']}"

### 🎲 Today's Developer Challenge:
Try implementing a new API endpoint using Python with FastAPI!

### 🔥 Coding Tip:
Always write tests for your code - it saves time in the long run!

---
"""
