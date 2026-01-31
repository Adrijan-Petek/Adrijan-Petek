from typing import Optional


def _badge(label: str, color: str, logo: Optional[str] = None, logo_color: str = "white") -> str:
    label_escaped = label.replace(" ", "%20")
    logo_part = f"&logo={logo}" if logo else ""
    return (
        f"![{label}](https://img.shields.io/badge/{label_escaped}-{color}"
        f"?style=for-the-badge{logo_part}&logoColor={logo_color})"
    )


def _tech_badge(tech: str) -> str:
    tech_map = {
        "TypeScript": ("3178C6", "typescript", "white"),
        "JavaScript": ("F7DF1E", "javascript", "black"),
        "Python": ("3776AB", "python", "white"),
        "Next.js": ("000000", "nextdotjs", "white"),
        "React": ("61DAFB", "react", "black"),
        "Node.js": ("339933", "nodedotjs", "white"),
        "FastAPI": ("009688", "fastapi", "white"),
        "PostgreSQL": ("4169E1", "postgresql", "white"),
        "MongoDB": ("47A248", "mongodb", "white"),
        "Docker": ("2496ED", "docker", "white"),
        "AWS": ("FF9900", "amazonaws", "black"),
        "Tailwind CSS": ("06B6D4", "tailwindcss", "white"),
        "Vercel": ("000000", "vercel", "white"),
        "Solidity": ("363636", "solidity", "white"),
        "Ethereum": ("627EEA", "ethereum", "white"),
        "GitHub": ("181717", "github", "white"),
    }

    if tech in tech_map:
        color, logo, logo_color = tech_map[tech]
        return _badge(tech, color, logo=logo, logo_color=logo_color)

    return _badge(tech, "111827")


def _ai_badge(name: str) -> str:
    ai_map = {
        "OpenAI API": ("412991", "openai", "white"),
        "Hugging Face": ("FFD21E", "huggingface", "black"),
        "LangChain": ("0F766E", None, "white"),
        "PyTorch": ("EE4C2C", "pytorch", "white"),
        "TensorFlow": ("FF6F00", "tensorflow", "white"),
    }
    if name in ai_map:
        color, logo, logo_color = ai_map[name]
        return _badge(name, color, logo=logo, logo_color=logo_color)
    return _badge(name, "111827")


def generate(config, daily_content):
    github_user = config["user"]["github"]
    theme = daily_content["color_theme"]

    tech_stack = config.get("tech_stack", []) or []
    tech_badges = " ".join([_tech_badge(t) for t in tech_stack])

    ai = config.get("ai", {}) or {}
    ai_enabled = ai.get("enabled") is True
    ai_focus = ai.get("focus")
    ai_stack = ai.get("stack", []) or []
    ai_badges = " ".join([_ai_badge(x) for x in ai_stack]) if ai_stack else ""

    parts = [
        "## Tech stack\n\n"
        + '<div style="border:1px solid rgba(0,0,0,0.12); border-radius:14px; padding:16px; background:rgba(255,255,255,0.02);">\n'
        + '  <div align="center">\n\n'
        + tech_badges
        + "\n\n  </div>\n"
        + "</div>\n",
        "## GitHub stats\n\n"
        + '<div style="border:1px solid rgba(0,0,0,0.12); border-radius:14px; padding:16px; background:rgba(255,255,255,0.02);">\n'
        + '  <div align="center">\n\n'
        + f"![GitHub Stats](https://git-hub-stats-card-generator.vercel.app/api/svg?username={github_user})\n\n"
        + f"[![GitHub Streak](https://github-readme-streak-stats.herokuapp.com/?user={github_user}&theme={theme}&hide_border=true)](https://git.io/streak-stats)\n\n"
        + f"[![GitHub Activity Graph](https://github-readme-activity-graph.vercel.app/graph?username={github_user}&theme={theme})](https://github.com/ashutosh00710/github-readme-activity-graph)\n\n"
        + "  </div>\n"
        + "</div>\n",
    ]

    if ai_enabled:
        focus_line = f"- Focus: **{ai_focus}**\n\n" if ai_focus else ""
        badges_block = ""
        if ai_badges:
            badges_block = (
                '<div align="center">\n\n' + ai_badges + "\n\n</div>\n"
            )
        parts.append(
            "## AI\n\n"
            + '<div style="border:1px solid rgba(0,0,0,0.12); border-radius:14px; padding:16px; background:rgba(255,255,255,0.02);">\n'
            + focus_line
            + badges_block
            + "</div>\n"
        )

    return "\n".join([p.strip() for p in parts if p.strip()]) + "\n"
