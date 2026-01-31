import random
from datetime import datetime


def generate(config, daily_content):
    """Generate a short daily professional joke/note."""
    today = datetime.now()
    random.seed(today.timetuple().tm_yday)

    notes = [
        "Deployed a smart contract today. It was so immutable it wouldn’t even accept my last-minute changes.",
        "Why did the dApp break up with the database? It needed more decentralization in the relationship.",
        "Blockchain tip of the day: if it can’t be verified, it can’t be trusted.",
        "Shipped a feature in one try. That’s how I know I forgot something.",
        "On-chain tools are like good APIs: boring on the outside, powerful on the inside.",
    ]

    note = random.choice(notes)

    return f"""
## Daily Byte
<hr style="border:0;border-top:1px solid rgba(14,165,233,0.35); margin:10px 0 16px 0;">

<div style="border:1px solid rgba(14,165,233,0.35); border-radius:14px; padding:16px; background:rgba(14,165,233,0.04);">
  <em>{note}</em>
</div>
""".strip() + "\n"
