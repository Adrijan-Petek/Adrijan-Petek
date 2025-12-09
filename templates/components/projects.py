def get_projects():
    return [
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
            "name": "Joybit",
            "url": "https://joybit.vercel.app/",
            "description": "Interactive gaming platform"
        },
        {
            "name": "Mememint",
            "url": "https://mememint-one.vercel.app/",
            "description": "NFT minting platform"
        }
    ]

def generate(config, daily_content):
    projects_list = get_projects()
    
    content = "## 🚀 Featured Projects\n\n"
    content += '<div align="center">\n\n'
    content += '| Project | Description | Link |\n'
    content += '|---------|-------------|------|\n'
    
    for project in projects_list:
        content += f"| {project['name']} | {project['description']} | [Explore]({project['url']}) |\n"
    
    content += "\n</div>\n\n"
    content += "---\n\n"
    return content
