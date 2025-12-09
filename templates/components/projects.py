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
        },
        {
            "name": "Super Based Cube",
            "url": "https://remix.gg/g/18a5445b-b15f-4bf5-a6d6-219c376633a0",
            "description": "3D puzzle game on Farcade"
        },
        {
            "name": "BYTE RACERS",
            "url": "https://remix.gg/g/f3da7626-351a-49cc-9fd5-e839018be4bb",
            "description": "Racing game on Farcade"
        },
        {
            "name": "Base Defenders",
            "url": "https://remix.gg/g/cfa6ed04-a2ec-4a82-866c-268b93774287",
            "description": "Tower defense game on Farcade"
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
