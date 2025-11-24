def generate(config, daily_content):
    """Generate GitHub stats and metrics section"""
    from .header import get_daily_contribution_color
    import random
    from datetime import datetime
    
    # Get contribution color
    today = datetime.now()
    day_of_year = today.timetuple().tm_yday
    random.seed(day_of_year)
    contribution_color = get_daily_contribution_color()
    
    # Build enhanced tech stack with colors
    tech_badges = []
    tech_colors = {
        "Python": "3776AB",
        "TypeScript": "3178C6",
        "JavaScript": "F7DF1E",
        "Java": "007396",
        "HTML5": "E34C26",
        "CSS3": "1572B6",
        "VS Code": "007ACC",
        "Solidity": "363636",
        "Ethereum": "627EEA",
        "GitHub": "181717"
    }
    
    for tech in config.get('tech_stack', []):
        color = tech_colors.get(tech, "000000")
        logo = tech.lower().replace(" ", "-")
        logo_color = "white" if tech not in ["JavaScript", "HTML5"] else "black"
        tech_badges.append(
            f"![{tech}](https://img.shields.io/badge/{tech.replace(' ', '%20')}-{color}?style=for-the-badge&logo={logo}&logoColor={logo_color})"
        )
    
    tech_stack = " ".join(tech_badges)
    
    # Social badges with colors
    social_badges = []
    social = config.get('social', {})
    if social.get("x"):
        social_badges.append(f"[![X](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)]({social['x']})")
    if social.get("zora"):
        social_badges.append(f"[![Zora](https://img.shields.io/badge/Zora-FFB400?style=for-the-badge&logo=zora&logoColor=black)]({social['zora']})")
    if social.get("farcaster"):
        social_badges.append(f"[![Farcaster](https://img.shields.io/badge/Farcaster-8A63D2?style=for-the-badge&logo=farcaster&logoColor=white)]({social['farcaster']})")
    if config.get('user', {}).get("website"):
        social_badges.append(f"[![Website](https://img.shields.io/badge/Website-4158D0?style=for-the-badge&logo=html5&logoColor=white)]({config['user']['website']})")
    
    social_links = " ".join(social_badges)
    
    github_user = config['user']['github']
    theme = daily_content['color_theme']

    # Stats & Streak configuration (allow opt-in overrides from config.json)
    stats_conf = config.get('stats', {})
    streak_conf = stats_conf.get('streak', {})

    # Build streak extra params from config (URI-encode values)
    from urllib.parse import quote_plus
    extra_streak_params = ""
    if isinstance(streak_conf, dict):
      for key, val in streak_conf.items():
        # Skip empty/None values
        if val is None or val == "":
          continue
        # for boolean True/False, use lowercase string
        if isinstance(val, bool):
          val_str = str(val).lower()
        else:
          val_str = str(val)
        extra_streak_params += f"&{quote_plus(key)}={quote_plus(val_str)}"
    
    # Compose theme-aware URLs for dark & light (GitHub theme-aware tags)
    stats_repo_link = "https://github.com/anuraghazra/github-readme-stats"
    activity_repo_link = "https://github.com/ashutosh00710/github-readme-activity-graph"
    streak_base_url = f"https://streak-stats.demolab.com/?user={github_user}&theme={theme}" + extra_streak_params
    dark_stats_url = f"https://github-readme-stats.vercel.app/api?username={github_user}&show_icons=true&theme=dark"
    light_stats_url = f"https://github-readme-stats.vercel.app/api?username={github_user}&show_icons=true&theme=default"
    dark_top_langs = f"https://github-readme-stats.vercel.app/api/top-langs/?username={github_user}&layout=compact&theme=dark"
    light_top_langs = f"https://github-readme-stats.vercel.app/api/top-langs/?username={github_user}&layout=compact&theme=default"

    return f"""
## 🛠️ Tech Stack

<div align="center">

### Languages & Frameworks
{tech_stack}

</div>

## 🌐 Connect With Me

<div align="center">

{social_links}

</div>

## 📈 GitHub Stats

<div align="center">

### 📊 GitHub Overview

<!-- Dark theme stats (shown on GitHub dark mode) -->
[![GitHub Stats-Dark]({dark_stats_url}#gh-dark-mode-only)]({stats_repo_link})
<!-- Light theme stats (shown on GitHub light mode) -->
[![GitHub Stats-Light]({light_stats_url}#gh-light-mode-only)]({stats_repo_link})

<!-- Top languages theme-aware -->
[![Top Languages-Dark]({dark_top_langs}#gh-dark-mode-only)]({stats_repo_link})
[![Top Languages-Light]({light_top_langs}#gh-light-mode-only)]({stats_repo_link})

### 🔥 Contribution Streak

[![GitHub Streak]({streak_base_url})](https://git.io/streak-stats)

### 📈 Contribution Activity

<!-- Theme-aware contribution graph (dark/light) -->
[![GitHub Activity Graph-Dark](https://github-readme-activity-graph.vercel.app/graph?username={github_user}&theme=dark#gh-dark-mode-only)]({activity_repo_link})
[![GitHub Activity Graph-Light](https://github-readme-activity-graph.vercel.app/graph?username={github_user}&theme=default#gh-light-mode-only)]({activity_repo_link})

### 🏆 Achievements & Expertise

<table align="center">
  <tr>
    <td align="center" width="33%">
      <img src="https://img.shields.io/badge/Full_Stack-Expert-2563EB?style=for-the-badge&logo=stackshare&logoColor=white" alt="Full Stack Expert" />
    </td>
    <td align="center" width="33%">
      <img src="https://img.shields.io/badge/Blockchain-Web3-7C3AED?style=for-the-badge&logo=ethereum&logoColor=white" alt="Blockchain Developer" />
    </td>
    <td align="center" width="33%">
      <img src="https://img.shields.io/badge/Smart_Contracts-Solidity-363636?style=for-the-badge&logo=solidity&logoColor=white" alt="Smart Contracts" />
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="https://img.shields.io/badge/DevOps-Professional-EA580C?style=for-the-badge&logo=docker&logoColor=white" alt="DevOps Professional" />
    </td>
    <td align="center">
      <img src="https://img.shields.io/badge/Cloud-AWS-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="AWS Expert" />
    </td>
    <td align="center">
      <img src="https://img.shields.io/badge/Security-Advanced-BE123C?style=for-the-badge&logo=shield&logoColor=white" alt="Security" />
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="https://img.shields.io/badge/API_Design-RESTful-0891B2?style=for-the-badge&logo=fastapi&logoColor=white" alt="API Design" />
    </td>
    <td align="center">
      <img src="https://img.shields.io/badge/Performance-Optimization-16A34A?style=for-the-badge&logo=lightning&logoColor=white" alt="Performance" />
    </td>
    <td align="center">
      <img src="https://img.shields.io/badge/Code_Quality-Clean_Code-65A30D?style=for-the-badge&logo=codeclimate&logoColor=white" alt="Code Quality" />
    </td>
  </tr>
</table>

### 📌 Activity Snapshot

<table align="center">
  <tr>
    <td align="center">
      <h3>💬 Commits</h3>
      <img src="https://img.shields.io/badge/500%2B-65A30D?style=flat-square&logo=git&logoColor=white" alt="Commits" />
    </td>
    <td align="center">
      <h3>📁 Projects</h3>
      <img src="https://img.shields.io/badge/25%2B-C2410C?style=flat-square&logo=github&logoColor=white" alt="Projects" />
    </td>
    <td align="center">
      <h3>⭐ Contributions</h3>
      <img src="https://img.shields.io/badge/100%2B-7C2D12?style=flat-square&logo=github-sponsors&logoColor=white" alt="Contributions" />
    </td>
  </tr>
</table>

</div>

---
"""

