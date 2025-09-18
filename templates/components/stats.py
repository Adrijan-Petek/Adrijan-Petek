def generate(config, daily_content):
    # Import contribution color function
    from .header import get_daily_contribution_color
    import random
    from datetime import datetime
    
    # Get contribution color
    today = datetime.now()
    day_of_year = today.timetuple().tm_yday
    random.seed(day_of_year)
    contribution_color = get_daily_contribution_color()
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

<!-- Contribution Graph (replacing streak) -->
<div align="center" style="margin: 20px 0;">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username={config['user']['github']}&theme={contribution_color}&hide_border=true&bg_color=00000000&height=300" alt="GitHub Contribution Graph" />
</div>

<!-- GitHub Streak -->
<div align="center" style="margin: 20px 0;">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user={config['user']['github']}&theme={daily_content['color_theme']}&hide_border=true&background=00000000" alt="GitHub Streak" />
</div>

<!-- Custom Achievement Badges (replacing languages) -->
<div align="center" style="margin: 20px 0;">
  <h3>🏆 Achievements & Skills</h3>
  <table>
    <tr>
      <td align="center">
        <img src="https://img.shields.io/badge/Full_Stack-Expert-2563EB?style=for-the-badge&logo=stackshare&logoColor=white" alt="Full Stack Expert" />
      </td>
      <td align="center">
        <img src="https://img.shields.io/badge/Blockchain-Web3-7C3AED?style=for-the-badge&logo=ethereum&logoColor=white" alt="Blockchain Developer" />
      </td>
      <td align="center">
        <img src="https://img.shields.io/badge/AI_ML-Advanced-16A34A?style=for-the-badge&logo=tensorflow&logoColor=white" alt="AI/ML Expert" />
      </td>
    </tr>
    <tr>
      <td align="center">
        <img src="https://img.shields.io/badge/DevOps-Professional-EA580C?style=for-the-badge&logo=docker&logoColor=white" alt="DevOps Professional" />
      </td>
      <td align="center">
        <img src="https://img.shields.io/badge/Cloud_AWS-Expert-0891B2?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="AWS Expert" />
      </td>
      <td align="center">
        <img src="https://img.shields.io/badge/Security-Advanced-BE123C?style=for-the-badge&logo=shield&logoColor=white" alt="Security Expert" />
      </td>
    </tr>
  </table>
</div>

<!-- Coding Activity Metrics -->
<div align="center" style="margin: 20px 0;">
  <h3>📊 Coding Activity</h3>
  <table>
    <tr>
      <td align="center">
        <img src="https://img.shields.io/badge/Commits-500%2B-65A30D?style=for-the-badge&logo=git&logoColor=white" alt="Commits" />
      </td>
      <td align="center">
        <img src="https://img.shields.io/badge/Projects-25%2B-C2410C?style=for-the-badge&logo=github&logoColor=white" alt="Projects" />
      </td>
      <td align="center">
        <img src="https://img.shields.io/badge/Contributions-100%2B-7C2D12?style=for-the-badge&logo=github-sponsors&logoColor=white" alt="Contributions" />
      </td>
    </tr>
  </table>
</div>

</div>

</div>

---
"""

