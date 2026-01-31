def get_projects(config=None):
    if config and isinstance(config.get("projects"), list) and config["projects"]:
        return config["projects"]

    return [
        {
            "name": "Python Beginners",
            "url": "https://github.com/Adrijan-Petek/python-beginners",
            "description": "Step-by-step Python tutorials",
        },
        {
            "name": "Farcaster Mini Apps",
            "url": "https://farcaster.xyz/adrijan",
            "description": "Exploring decentralized applications",
        },
        {
            "name": "Joybit",
            "url": "https://joybit.vercel.app/",
            "description": "Interactive gaming platform",
        },
        {
            "name": "Mememint",
            "url": "https://mememint-one.vercel.app/",
            "description": "NFT minting platform",
        },
        {
            "name": "Super Based Cube",
            "url": "https://remix.gg/g/18a5445b-b15f-4bf5-a6d6-219c376633a0",
            "description": "3D puzzle game on Farcade",
        },
        {
            "name": "BYTE RACERS",
            "url": "https://remix.gg/g/f3da7626-351a-49cc-9fd5-e839018be4bb",
            "description": "Racing game on Farcade",
        },
        {
            "name": "Base Defenders",
            "url": "https://remix.gg/g/cfa6ed04-a2ec-4a82-866c-268b93774287",
            "description": "Tower defense game on Farcade",
        },
    ]


def generate(config, daily_content):
    projects_list = get_projects(config)

    def card(project):
        if not project:
            return "&nbsp;"
        description = project.get("description") or ""
        return (
            '<div style="border:1px solid rgba(14,165,233,0.35); border-radius:14px; padding:14px; background:rgba(14,165,233,0.04);">'
            f'<div style="font-weight:700; font-size:1.05em; margin-bottom:6px;"><a href="{project["url"]}">{project["name"]}</a></div>'
            f'<div style="color:#9ca3af;">{description}</div>'
            "</div>"
        )

    rows = []
    for idx in range(0, len(projects_list), 3):
        cols = [
            projects_list[idx] if idx < len(projects_list) else None,
            projects_list[idx + 1] if idx + 1 < len(projects_list) else None,
            projects_list[idx + 2] if idx + 2 < len(projects_list) else None,
        ]
        rows.append(
            "<tr>"
            f'<td width="33.3%" valign="top">{card(cols[0])}</td>'
            f'<td width="33.3%" valign="top">{card(cols[1])}</td>'
            f'<td width="33.3%" valign="top">{card(cols[2])}</td>'
            "</tr>"
        )

    return (
        "## 🚀 Featured Projects\n\n"
        '<table width="100%" cellspacing="0" cellpadding="6">\n'
        + "\n".join(rows)
        + "\n</table>\n"
    )
