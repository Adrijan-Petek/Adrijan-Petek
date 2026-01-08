def generate(config, daily_content):
    """Generate an optional support section.

    Controlled by `config["support"]`.
    """
    support = config.get("support", {}) or {}

    # Show section if explicitly enabled or if any URLs are present
    enabled = support.get("enabled")

    creator_url = support.get("creator_coin_uniswap_url") or support.get("creator_coin_url")
    image_url = support.get("image_coin_uniswap_url") or support.get("image_coin_url")

    if enabled is False:
        return ""

    if enabled is not True and not (creator_url or image_url):
        return ""

    title = support.get("title") or "## 💜 Support"
    intro = support.get("intro") or (
        "If you’d like to support my work, you can pick up my coins on Uniswap (Base)."
    )

    creator_label = support.get("creator_coin_label") or "Creator Coin"
    image_label = support.get("image_coin_label") or "Image Coin"

    lines = [title, "", intro, ""]

    if creator_url:
        lines.append(f"- [{creator_label} — Buy on Uniswap (Base)]({creator_url})")
    if image_url:
        lines.append(f"- [{image_label} — Buy on Uniswap (Base)]({image_url})")

    closing = support.get("closing")
    if closing:
        lines.extend(["", closing])

    lines.extend(["", "---", ""])

    return "\n".join(lines)
