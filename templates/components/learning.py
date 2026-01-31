def generate(config, daily_content):
    border = "1px solid rgba(14,165,233,0.35)"
    bg = "rgba(14,165,233,0.04)"
    return f"""
## 🧭 About

<div style="border:{border}; border-radius:14px; padding:16px; background:{bg};">
  <p><strong>Full-stack Web3 developer</strong> focused on building decentralized applications, on-chain tools, and creative digital experiences.</p>
  <ul>
    <li>Code, creativity, and on-chain craft.</li>
    <li>Working with Python, Solidity, TypeScript, JavaScript, and more — shipped with intention.</li>
    <li>Currently exploring Farcaster mini-apps, Base blockchain, smart contracts, decentralized fundraising, NFT minting, and sybil/farm detection tools.</li>
    <li>Building in public and documenting the journey.</li>
  </ul>
</div>

## 🧰 Skills

<div style="border:{border}; border-radius:14px; padding:16px; background:{bg};">
  <p><strong>Core</strong></p>
  <p>
    <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" />
    <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
    <img alt="Solidity" src="https://img.shields.io/badge/Solidity-363636?style=for-the-badge&logo=solidity&logoColor=white" />
    <img alt="React" src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" />
    <img alt="Next.js" src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white" />
  </p>
  <table width="100%" cellspacing="0" cellpadding="6">
    <tr><td width="35%">TypeScript</td><td><progress value="90" max="100"></progress></td></tr>
    <tr><td>Python</td><td><progress value="85" max="100"></progress></td></tr>
    <tr><td>Solidity</td><td><progress value="80" max="100"></progress></td></tr>
    <tr><td>React/Next.js</td><td><progress value="85" max="100"></progress></td></tr>
    <tr><td>Web3</td><td><progress value="80" max="100"></progress></td></tr>
  </table>
</div>

<details>
<summary><strong>🎯 Current Focus</strong></summary>

<div style="border:{border}; border-radius:14px; padding:16px; background:{bg}; margin-top:10px;">
  <ul>
    <li>Decentralized mini-apps on Farcaster and Base</li>
    <li>On-chain gaming, meme tools, faith-sharing apps, fundraising platforms</li>
    <li>Tools to detect coordinated Sybil attacks and farm behavior</li>
    <li>Full-stack Web3 development (React, Next.js, wagmi, OnchainKit, Farcaster SDK)</li>
  </ul>
</div>
</details>

<details>
<summary><strong>📌 Key Projects (Pinned)</strong></summary>

<div style="border:{border}; border-radius:14px; padding:16px; background:{bg}; margin-top:10px;">
  <ul>
    <li><strong>crypto-landing-page</strong> (TypeScript) — Modern landing page template for crypto projects</li>
    <li><strong>crypto-self-learning-bot</strong> (Python) — Template for ML-based crypto trading bot with data processing, Random Forest model, and backtesting</li>
    <li><strong>joybit</strong> (TypeScript) — Decentralized gaming platform on Base with JOYB token economy and multiple games</li>
    <li><strong>mememint</strong> (TypeScript) — Farcaster Mini App for meme creation, leaderboard tracking, and NFT minting on Base</li>
    <li><strong>yeshua-christ</strong> (TypeScript) — Mini app for sharing faith, Gospel, and biblical content</li>
    <li><strong>RaiseFunds</strong> (TypeScript) — Decentralized fundraising on Farcaster with on-chain creation, sharing, and donations</li>
  </ul>
</div>
</details>

<details>
<summary><strong>📈 Recent Activity</strong></summary>

<div style="border:{border}; border-radius:14px; padding:16px; background:{bg}; margin-top:10px;">
  <ul>
    <li>1,537 contributions in the last year</li>
    <li>Heavy focus in January 2026: 549 commits across 15+ repositories</li>
    <li>Active development on sybil-shield (detection tool), Base-related full-stack apps, and mini-app experiments</li>
  </ul>
</div>
</details>

<details>
<summary><strong>🛠️ Tools & Technologies</strong></summary>

<div style="border:{border}; border-radius:14px; padding:16px; background:{bg}; margin-top:10px;">
  <ul>
    <li><strong>Languages</strong>: Python, Solidity, TypeScript, JavaScript</li>
    <li><strong>Blockchains</strong>: Base, Ethereum</li>
    <li><strong>Frameworks</strong>: Next.js, React, Tailwind CSS</li>
    <li><strong>Web3</strong>: wagmi, OnchainKit, Farcaster SDK, ethers/viem</li>
    <li><strong>Other</strong>: Graph analysis (Cytoscape.js), local-first apps, behavioral pattern detection</li>
  </ul>
</div>
</details>
""".strip() + "\n"
