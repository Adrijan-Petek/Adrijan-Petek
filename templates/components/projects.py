def get_projects():
    return [
        {
            "name": "CryptoMobb",
            "url": "https://www.cryptomobb.xyz",
            "description": "Crypto community and learning platform"
        },
        {
            "name": "Python Beginners",
            "url": "https://github.com/Adrijan-Petek/python-beginners",
            "description": "Step-by-step Python tutorials"
        },
        {
            "name": "Farcaster Mini Apps",
            "url": "https://farcaster.xyz/adrijan",
            "description": "Exploring decentralized applications"
        },
        {
            "name": "Mobb Chain",
            "url": "https://www.mobbchain.xyz",
            "description": "Blockchain innovation platform"
        }
    ]

def generate(config, daily_content):
    projects_list = get_projects()
    
    content = "## 🚀 Projects\n\n"
    
    for project in projects_list:
        spotlight = " 🔥" if project["name"] == daily_content["spotlight_project"] else ""
        content += f"- **[{project['name']}]({project['url']})**{spotlight} – {project['description']}\n"
    
    content += "\n---\n\n"
    return content
