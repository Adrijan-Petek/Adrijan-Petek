def get_learning_topics():
    return [
        "Advanced Python OOP", "React Fundamentals", "Smart Contract Security",
        "Web3 Integration", "TypeScript Advanced Patterns", "DApp Development"
    ]

def generate(config, daily_content):
    learning_paths = config['learning_paths']
    
    content = "## 🐍 Learning & Tutorials\n\n"
    
    for topic, items in learning_paths.items():
        emoji = "🐍" if topic == "python" else "📘" if topic == "typescript" else "🌐" if topic == "web_dev" else "🔗"
        title = topic.replace("_", " ").title()
        
        content += f"### {emoji} **{title}**\n"
        for i, item in enumerate(items):
            status = "✅" if i < len(items) - 2 else "➡️" if i == len(items) - 2 else "⏳"
            content += f"- {status} {item}\n"
        content += "\n"
    
    content += f"**Today's Focus**: {daily_content['learning_focus']} 🎯\n\n"
    content += "---\n\n"
    
    return content
