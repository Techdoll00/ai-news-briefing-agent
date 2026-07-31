<p align="center">
  <img src="https://img.shields.io/badge/Status-Running%20Daily-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Built%20With-Hermes%20Agent-7B68EE?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Delivery-Feishu-3370FF?style=for-the-badge" />
</p>

# 🤖 I Wake Up at 9 AM Every Morning to Read the Internet for You

Not a metaphor. This agent runs a cron job, searches GitHub Trending + the web, and delivers a curated AI briefing to my Feishu — every single day since July 2026.

**Why?** Because after leaving my internship at Style3D, I realized the fastest way to fall behind in AI is to stop paying attention. So I built something that pays attention for me.

---

## 📰 What It Looks Like

> 🌅 早安宝贝～☀️💕 **2026年7月29日**
>
> 🐙 **GitHub 精选**
> - affaan-m/ECC ⭐234K — Agent harness 性能优化系统
> - microsoft/agent-governance-toolkit ⭐5K — 微软官方 Agent 治理工具包
> - virgiliojr94/book-to-skill ⭐10.6K — PDF 直接转 Agent skill
>
> 🤖 **Agent 动态**
> - Anthropic 公开反对完全开放权重模型 — HN 榜首 998分
> - 法国监管报告：DeepSeek 被列为 Agent 市场"挑战者"
>
> 🎯 **秋招雷达**
> - 阿里云 Agent Infra 工程师（杭州，招 2000 人，AI 岗超 80%）
> - 淘天集团 AI Agent 优化工程师（杭州，500元/天）
>
> 爱你哟～ (◕‿◕✿)

*This is not a mockup. These are real outputs saved in [`samples/`](samples/).*

---

## 🏗️ How It Works

```
9:00 AM → Cron fires → GitHub Trending → Tavily → Exa → DeepSeek → Feishu
```

| Step | What Happens | Tool |
|------|-------------|------|
| 1 | Scrape GitHub Trending, filter AI/Agent repos | Python |
| 2 | Search web for latest AI agent ecosystem news | [Tavily](https://tavily.com) + [Exa](https://exa.ai) |
| 3 | Search for AI job listings in Hangzhou | Tavily + Exa |
| 4 | LLM curates, connects dots, writes in my style | DeepSeek V4 Pro |
| 5 | Push to Feishu DM + save to `samples/` | Feishu API |

---

## 🚀 Run Your Own (5 Minutes)

```bash
git clone https://github.com/Techdoll00/ai-news-briefing-agent
cd ai-news-briefing-agent
cp config.example.yaml config.yaml
# Fill in your Tavily, Exa, DeepSeek keys
pip install requests pyyaml
python main.py
```

No Docker. No database. No framework. Just Python + 3 API keys.

---

## 🤔 Why I Built This

After 4 months as an AI Product Intern, I left my job and realized:

- Twitter takes 2 hours/day to stay informed — and you still get second-hand takes
- Most "AI newsletters" are link dumps with zero curation
- Nobody connects the news back to *your specific situation*

So I built an agent that:

✅ Reads the internet for me  
✅ Filters for what I actually care about (Agent products, evaluation, hiring)  
✅ Connects dots back to my experience (Style3D, Hermes, job search)  
✅ Has personality — reads like a friend wrote it  

**One month later, I haven't missed a day.**

---

## 🛠️ Tech Stack

| Layer | Choice | Why |
|-------|--------|-----|
| Agent Framework | Hermes Agent | 75 built-in skills, cron, multi-platform |
| Search | Tavily + Exa | Semantic + keyword, fallback when one fails |
| LLM | DeepSeek V4 Pro | Best price/quality ratio for Chinese content |
| Delivery | Feishu/Lark | Native Markdown, mobile-friendly |
| Hosting | Tencent Cloud VPS | 2-core, 4GB, Hangzhou |
| Proxy | mihomo | Global web access |

---

## 📂 Project Structure

```
├── main.py                 # Standalone runner (Tavily + Exa + DeepSeek)
├── prompt.py               # System prompt (the "personality" layer)
├── prompt.md               # Full Hermes cron config
├── config.example.yaml     # Fill in your keys
├── samples/                # Real daily outputs
└── README.md               # This file
```

---

## 🤝 Real Talk

This project is **not** a polished SaaS product. It's a working agent that runs every day on a 2-core VPS. Some days the search fails. Sometimes the LLM output is too long for Feishu's message limit.

But it works. It's real. And it proves something I believe deeply:

> **The best way to demonstrate you can build AI products is to build one that serves you first.**

---

<p align="center">
  <sub>Built with ☕ and occasional server crashes in Hangzhou · <a href="https://github.com/Techdoll00">Kin Liao</a></sub>
</p>
