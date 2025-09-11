def generate(config, daily_content):
    tech_stack = " ".join([
        f"![{tech}](https://img.shields.io/badge/{tech}-000000?style=for-the-badge&logo={tech.lower()}&logoColor=white)"
        for tech in config['tech_stack']
    ])
    
    return f"""
## 🛠️ Tech Stack
{tech_stack}

## 📈 GitHub Stats
![GitHub stats](https://github-readme-stats.vercel.app/api?username={config['user']['github']}&show_icons=true&theme={daily_content['color_theme']})  
![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username={config['user']['github']}&layout=compact&theme={daily_content['color_theme']})

---
"""
