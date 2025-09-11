def generate(config, daily_content):
    tech_badges = []
    for tech in config['tech_stack']:
        if tech == "VS Code":
            tech_badges.append("![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)")
        else:
            # URL encode spaces for badges
            tech_name = tech.replace(" ", "%20")
            tech_badges.append(f"![{tech}](https://img.shields.io/badge/{tech_name}-000000?style=for-the-badge&logo={tech.lower().replace(' ', '-')}&logoColor=white)")
    
    tech_stack = " ".join(tech_badges)
    
    # Social badges
    social_badges = []
    if "x" in config['social']:
        social_badges.append(f"[![X](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)]({config['social']['x']})")
    if "linkedin" in config['social']:
        social_badges.append(f"[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)]({config['social']['linkedin']})")
    if "farcaster" in config['social']:
        social_badges.append(f"[![Farcaster](https://img.shields.io/badge/Farcaster-8A63D2?style=for-the-badge&logo=farcaster&logoColor=white)]({config['social']['farcaster']})")
    
    social_links = " ".join(social_badges)
    
    return f"""
## 🛠️ Tech Stack
{tech_stack}

## 🌐 Connect With Me
{social_links}

## 📈 GitHub Stats
![GitHub stats](https://github-readme-stats.vercel.app/api?username={config['user']['github']}&show_icons=true&theme={daily_content['color_theme']}&count_private=true)  
![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username={config['user']['github']}&layout=compact&theme={daily_content['color_theme']}&hide=html,css)

---
"""
