def generate(config, daily_content):
    tech_badges = []
    for tech in config.get('tech_stack', []):
        if tech == "VS Code":
            tech_badges.append("![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)")
        else:
            # URL encode spaces for badges
            tech_name = tech.replace(" ", "%20")
            logo = tech.lower().replace(" ", "-")
            tech_badges.append(
                f"![{tech}](https://img.shields.io/badge/{tech_name}-000000?style=for-the-badge&logo={logo}&logoColor=white)"
            )
    
    tech_stack = " ".join(tech_badges)
    
    # Social badges (Zora instead of LinkedIn)
    social_badges = []
    social = config.get('social', {})
    if social.get("x"):
        social_badges.append(f"[![X](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)]({social['x']})")
    if social.get("zora"):
        # Shields might not have an official Zora logo; including logo=zora is harmless if absent.
        social_badges.append(f"[![Zora](https://img.shields.io/badge/Zora-000000?style=for-the-badge&logo=zora&logoColor=white)]({social['zora']})")
    if social.get("farcaster"):
        social_badges.append(f"[![Farcaster](https://img.shields.io/badge/Farcaster-8A63D2?style=for-the-badge&logo=farcaster&logoColor=white)]({social['farcaster']})")
    
    social_links = " ".join(social_badges)
    
    return f"""
## 🛠️ Tech Stack
{tech_stack}

## 🌐 Connect With Me
{social_links}

## 📈 GitHub Stats
<div align="center">

<!-- GitHub Stats and Top Languages in same row -->
<table>
  <tr>
    <td>
      <img src="https://github-readme-stats.vercel.app/api?username={config['user']['github']}&show_icons=true&theme={daily_content['color_theme']}&count_private=true&hide_border=true&bg_color=00000000" alt="GitHub Stats" />
    </td>
    <td>
      <img src="https://github-readme-stats.vercel.app/api/top-langs/?username={config['user']['github']}&layout=compact&theme={daily_content['color_theme']}&hide_border=true&bg_color=00000000&hide=html,css" alt="Top Languages" />
    </td>
  </tr>
</table>

<!-- GitHub Streak with additional stats to fill space -->
<table>
  <tr>
    <td>
      <img src="https://github-readme-streak-stats.herokuapp.com/?user={config['user']['github']}&theme={daily_content['color_theme']}&hide_border=true&background=00000000" alt="GitHub Streak" />
    </td>
    <td>
      <img src="https://github-readme-stats.vercel.app/api?username={config['user']['github']}&show_icons=false&theme={daily_content['color_theme']}&hide_border=true&bg_color=00000000&hide_title=true&hide_rank=true&count_private=true" alt="GitHub Stats Compact" />
    </td>
    <td>
      <img src="https://github-readme-stats.vercel.app/api/top-langs/?username={config['user']['github']}&layout=donut&theme={daily_content['color_theme']}&hide_border=true&bg_color=00000000&hide=html,css" alt="Top Languages Donut" />
    </td>
  </tr>
</table>

<!-- Activity Graph -->
<div align="center" style="margin-top: 20px;">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username={config['user']['github']}&theme={daily_content['color_theme']}&hide_border=true&bg_color=00000000" alt="GitHub Activity Graph" />
</div>

</div>

---
"""

