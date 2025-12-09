def get_learning_topics():
    return [
        "Advanced Python OOP", "React Fundamentals", "Smart Contract Security",
        "Web3 Integration", "TypeScript Advanced Patterns", "DApp Development"
    ]

def generate(config, daily_content):
    learning_paths = config['learning_paths']

    content = "## 📚 Learning & Tutorials\n\n"
    content += '<div align="center">\n\n'
    content += '| 🐍 **Python** | 📘 **TypeScript** | 🌐 **Web Dev** | 🔗 **Blockchain** |\n'
    content += '|---------------|----------------|-------------|----------------|\n'

    # Get all learning path items
    python_items = learning_paths['python']
    typescript_items = learning_paths['typescript']
    web_dev_items = learning_paths['web_dev']
    blockchain_items = learning_paths['blockchain']

    # Find the maximum length among all columns
    max_len = max(len(python_items), len(typescript_items), len(web_dev_items), len(blockchain_items))

    # Create rows for the 4-column table
    for i in range(max_len):
        python_item = ""
        typescript_item = ""
        web_dev_item = ""
        blockchain_item = ""

        if i < len(python_items):
            status = "✅" if i < len(python_items) - 2 else "➡️" if i == len(python_items) - 2 else "⏳"
            python_item = f"{status} {python_items[i]}"

        if i < len(typescript_items):
            status = "✅" if i < len(typescript_items) - 2 else "➡️" if i == len(typescript_items) - 2 else "⏳"
            typescript_item = f"{status} {typescript_items[i]}"

        if i < len(web_dev_items):
            status = "✅" if i < len(web_dev_items) - 2 else "➡️" if i == len(web_dev_items) - 2 else "⏳"
            web_dev_item = f"{status} {web_dev_items[i]}"

        if i < len(blockchain_items):
            status = "✅" if i < len(blockchain_items) - 2 else "➡️" if i == len(blockchain_items) - 2 else "⏳"
            blockchain_item = f"{status} {blockchain_items[i]}"

        content += f"| {python_item} | {typescript_item} | {web_dev_item} | {blockchain_item} |\n"

    content += "\n</div>\n\n"
    content += '<p style="color: #888; font-size: 0.9em; margin-top: 15px; text-align: center;">✅ = Completed | ➡️ = In Progress | ⏳ = Planned</p>\n\n'
    content += "### 🎯 Current Focus\n"
    content += f"> **{daily_content['learning_focus']}** & **Web3 Development**\n\n"
    content += "---\n\n"

    return content
