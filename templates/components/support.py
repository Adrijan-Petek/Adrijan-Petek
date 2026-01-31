import os


def generate(config, daily_content):
    """Generate an optional support section.

    Controlled by `config["support"]`.
    """
    support = config.get("support", {}) or {}

    enabled = support.get("enabled")
    if enabled is False:
        return ""

    creator_url = support.get("creator_coin_uniswap_url") or support.get("creator_coin_url")
    creator_image = support.get("creator_coin_image") or support.get("creator_coin_image_url")

    if enabled is not True and not (creator_url or creator_image):
        return ""

    title = support.get("title") or "## Support"
    intro = support.get("intro") or "If you’d like to support my work:"
    creator_label = support.get("creator_coin_label") or "Creator Coin"

    lines = [title, "", intro, ""]

    if creator_url or creator_image:
        img_html = ""
        if creator_image and (
            creator_image.startswith("http://")
            or creator_image.startswith("https://")
            or os.path.exists(creator_image)
        ):
            img_html = (
                f'<a href="{creator_url}"><img src="{creator_image}" alt="{creator_label}" '
                'width="96" height="96" style="border-radius: 999px; border: 1px solid rgba(0,0,0,0.12);" /></a>'
            )
        buy_badge = ""
        if creator_url:
            buy_badge = (
                f'<a href="{creator_url}"><img alt="Buy on Uniswap" '
                'src="https://img.shields.io/badge/Buy%20on%20Uniswap-Base-0ea5e9?style=for-the-badge" /></a>'
            )

        lines.append(
            '<div style="border:1px solid rgba(0,0,0,0.12); border-radius:14px; padding:16px; background:rgba(255,255,255,0.02);" align="center">'
        )
        lines.append('<table width="100%" cellspacing="0" cellpadding="6">')
        lines.append("  <tr>")
        left = f"{img_html}<br/><strong>{creator_label}</strong>" if img_html else f"<strong>{creator_label}</strong>"
        right = buy_badge or ""
        lines.append(f'    <td width="50%" align="center">{left}</td>')
        lines.append(f'    <td width="50%" align="center">{right}</td>')
        lines.append("  </tr>")
        lines.append("</table>")
        lines.append("</div>")

    closing = support.get("closing")
    if closing:
        lines.extend(["", closing])

    return "\n".join(lines).strip() + "\n"
