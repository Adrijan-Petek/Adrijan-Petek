import glob
import random
from datetime import datetime


def get_random_banner():
    banner_files = glob.glob("img/github-header-banner*.png")
    if not banner_files:
        return None
    return random.choice(banner_files)


def get_daily_banner_style():
    styles = [
        {
            "border_radius": "16px",
            "shadow": "0 10px 24px rgba(0,0,0,0.18)",
            "border_color": "rgba(0,0,0,0.12)",
            "filter": "none",
        },
        {
            "border_radius": "18px",
            "shadow": "0 12px 28px rgba(0,0,0,0.22)",
            "border_color": "rgba(0,0,0,0.10)",
            "filter": "contrast(1.03) saturate(1.05)",
        },
        {
            "border_radius": "14px",
            "shadow": "0 8px 20px rgba(0,0,0,0.16)",
            "border_color": "rgba(0,0,0,0.14)",
            "filter": "brightness(1.02)",
        },
    ]
    return random.choice(styles)


def get_daily_intro():
    intros = [
        "**Mobile app developer · Web3 builder**",
        "**TypeScript · Python · Solidity**",
        "**Shipping production-ready apps**",
    ]
    return random.choice(intros)


def get_daily_typing_color():
    colors = [
        "2563EB",
        "DC2626",
        "16A34A",
        "EA580C",
        "7C3AED",
        "0891B2",
        "BE123C",
        "65A30D",
        "1E40AF",
        "0F766E",
        "6B21A8",
        "0369A1",
    ]
    return random.choice(colors)


def get_daily_typing_lines():
    line_sets = [
        "Mobile+App+Developer;Web3+Builder;TypeScript+%2F+Python;Shipping+to+Production",
        "Cross-Platform+Apps;Clean+UX;Solidity+%2F+EVM;Performance+%26+Security",
        "AI+Enabled+Apps;Onchain+Integrations;Product+Engineering;Always+Shipping",
    ]
    return random.choice(line_sets)


def get_daily_contribution_color():
    colors = [
        "github",
        "github-light",
        "dark",
        "merko",
        "gruvbox",
        "tokyo-night",
        "onedark",
        "cobalt",
        "dracula",
        "nord",
        "rose-pine",
        "catppuccin-mocha",
    ]
    return random.choice(colors)


def generate(config, daily_content):
    today = datetime.now()
    random.seed(today.timetuple().tm_yday)

    banner_style = get_daily_banner_style()
    banner_path = "img/github-header-banner.png"
    if not glob.glob(banner_path):
        banner_path = get_random_banner()

    banner_html = ""
    if banner_path:
        banner_html = f"""
<div align="center">
  <img src="{banner_path}" alt="Header Banner" style="
    width: 100%;
    max-height: 240px;
    object-fit: cover;
    border-radius: {banner_style['border_radius']};
    box-shadow: {banner_style['shadow']};
    border: 1px solid {banner_style['border_color']};
    filter: {banner_style['filter']};
    margin-bottom: 1.25rem;
  " />
</div>
"""

    daily_intro = get_daily_intro()
    typing_lines = get_daily_typing_lines()
    typing_color = get_daily_typing_color()

    social = config.get("social", {}) or {}
    typing_enabled = social.get("typing_svg_enabled") is True

    typing_html = ""
    if typing_enabled:
        typing_html = f"""
<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=22&duration=2800&pause=2000&color={typing_color}&center=true&vCenter=true&width=920&lines={typing_lines}" alt="Typing SVG" />
</p>
"""

    github_user = config.get("user", {}).get("github", "")
    badges = []
    if github_user:
        badges.append(
            f"![Profile Views](https://komarev.com/ghpvc/?username={github_user}&color=0ea5e9&style=for-the-badge)"
        )
        badges.append(
            f"![Followers](https://img.shields.io/github/followers/{github_user}?color=0ea5e9&style=for-the-badge)"
        )
        badges.append(
            f"![Stars](https://img.shields.io/github/stars/{github_user}?color=f59e0b&style=for-the-badge)"
        )
    badges_line = " ".join(badges)

    website = config.get("user", {}).get("website")
    tagline = config.get("user", {}).get("tagline")
    links = []
    if social.get("x"):
        links.append(f"[X/Twitter]({social['x']})")
    if social.get("zora"):
        links.append(f"[Zora]({social['zora']})")
    if social.get("farcaster"):
        links.append(f"[Farcaster]({social['farcaster']})")
    if social.get("base_profile"):
        links.append(f"[Base Profile]({social['base_profile']})")
    if social.get("base_invite"):
        links.append(f"[Base Invite]({social['base_invite']})")
    if social.get("farcaster_invite"):
        links.append(f"[Farcaster Invite]({social['farcaster_invite']})")
    if social.get("zora_invite"):
        links.append(f"[Zora Invite]({social['zora_invite']})")
    if social.get("self_referral"):
        links.append(f"[Self Referral]({social['self_referral']})")
    if website:
        links.append(f"[Website]({website})")

    links_line = " · ".join(links)

    return f"""
{banner_html}
{typing_html}
<div align="center" style="margin-top: 6px;">

# {config['user']['name']}

{tagline or daily_intro}

Building and shipping applications with a focus on performance, security, and clean UX.

{badges_line}

{links_line}

</div>
""".lstrip()
