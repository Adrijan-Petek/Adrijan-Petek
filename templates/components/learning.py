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

    ai = config.get("ai", {}) or {}
    ai_line = ""
    if ai.get("enabled") is True and ai.get("focus"):
        ai_line = f"<li><strong>AI</strong>: {ai['focus']}</li>"

    return f"""
## About

<div style="border:1px solid rgba(0,0,0,0.12); border-radius:14px; padding:16px; background:rgba(255,255,255,0.02);">
  <ul>
    <li><strong>Current focus</strong>: {focus}</li>
    <li><strong>Building</strong>: web + mobile + onchain integrations</li>
    {ai_line}
    <li><strong>Open to</strong>: collaborations and new opportunities</li>
  </ul>
</div>
""".strip() + "\n"
