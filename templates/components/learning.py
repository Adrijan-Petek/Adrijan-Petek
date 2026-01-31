def get_learning_topics():
    return [
        "Web3 Integration",
        "Smart Contract Security",
        "TypeScript Advanced Patterns",
        "React Fundamentals",
        "DApp Development",
        "AI Product Engineering",
    ]


def _render_list(items):
    if not items:
        return "<em>—</em>"
    return "<ul>\n" + "\n".join([f"  <li>{i}</li>" for i in items]) + "\n</ul>\n"


def generate(config, daily_content):
    focus = daily_content.get("learning_focus") or "Building"

    core = [
        "TypeScript / Next.js / React",
        "Python",
        "API design and integrations",
        "Performance & security",
        "Product-focused engineering",
    ]
    exploring = [
        "AI-enabled apps (LLMs, tooling, evals)",
        "Solidity / EVM",
        "Onchain integrations",
        "Farcaster mini apps",
        "Smart contract security",
    ]

    ai = config.get("ai", {}) or {}
    if ai.get("enabled") is True and ai.get("focus"):
        exploring.insert(0, ai["focus"])

    content = "## About\n\n"
    content += f"- Current focus: **{focus}**\n"
    content += "- Open to: collaborations and new opportunities\n\n"

    content += """<table width="100%">
  <tr>
    <td width="50%" valign="top">
      <h3>Core</h3>
"""
    content += _render_list(core)
    content += """
    </td>
    <td width="50%" valign="top">
      <h3>Exploring</h3>
"""
    content += _render_list(exploring)
    content += """
    </td>
  </tr>
</table>
"""

    return content
