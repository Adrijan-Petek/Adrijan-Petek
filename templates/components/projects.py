def get_projects():
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
    projects_list = get_projects()

    rows = []
    for idx in range(0, len(projects_list), 2):
        left = projects_list[idx]
        right = projects_list[idx + 1] if idx + 1 < len(projects_list) else None

        def card(p):
            if not p:
                return "&nbsp;"
            return (
                '<div style="border:1px solid rgba(0,0,0,0.12); border-radius:14px; padding:14px; background:rgba(255,255,255,0.02);">'
                f'<div style="font-weight:700; font-size:1.05em; margin-bottom:6px;"><a href="{p["url"]}">{p["name"]}</a></div>'
                f'<div style="color:#9ca3af;">{p["description"]}</div>'
                "</div>"
            )

        rows.append(
            "<tr>"
            f'<td width="50%" valign="top">{card(left)}</td>'
            f'<td width="50%" valign="top">{card(right)}</td>'
            "</tr>"
        )

    return (
        "## Featured projects\n\n"
        '<table width="100%" cellspacing="0" cellpadding="6">\n'
        + "\n".join(rows)
        + "\n</table>\n"
    )
