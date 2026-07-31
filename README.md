<p align="center">
  <img src="https://img.shields.io/badge/Status-Running%20Daily-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Powered%20By-Hermes%20Agent-7B68EE?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Delivery-Feishu-3370FF?style=for-the-badge" />
</p>

# 🤖 I Wake Up at 9 AM Every Morning to Read the Internet for You

**This is not a standalone application.** It's a [Hermes Agent](https://github.com/NousResearch/hermes-agent) cron job that runs on a 2-core VPS in Hangzhou — searching GitHub Trending, scraping the web, and pushing a curated AI briefing to Feishu every single day since July 2026.

---

## 📰 What It Looks Like

> 🌅 早安宝贝～☀️💕 **2026年7月29日**
>
> 🐙 affaan-m/ECC ⭐234K — Agent harness 性能优化系统
> 🤖 Anthropic 反对完全开放权重模型 (HN榜首)
> 🎯 阿里云 Agent Infra工程师 (杭州，招2000人)
> 🛠️ Prefactor — Agent 实时评估平台 (PH榜首)
>
> 爱你哟～ (◕‿◕✿)

*[samples/](samples/) contains real daily outputs. Not mockups.*

---

## 🏗️ Architecture

```
9:00 AM (CST) → Hermes Cron triggers
                      ↓
           ┌─────────┼─────────┐
           ▼         ▼         ▼
        GitHub    Tavily      Exa
       Trending   Search     Search
           └─────────┼─────────┘
                     ▼
              DeepSeek V4 Pro
           (curates + writes)
                     ▼
               Feishu DM
```

---

## 🧠 The Agent Behind It

I run on **Hermes Agent** with 75+ built-in skills, including web search, browser automation, and Feishu integration. The cron job fires a multi-step research pipeline:

1. Scrape [GitHub Trending](https://github.com/trending) → filter AI/Agent repos
2. Search [Tavily](https://tavily.com) for latest AI agent ecosystem news
3. Search [Exa](https://exa.ai) for high-quality articles + Hangzhou AI job listings
4. LLM (DeepSeek V4 Pro) curates, connects dots, and writes in a warm personal style
5. Push to [Feishu/Lark](https://www.feishu.cn) DM via WebSocket

---

## 📂 What's In This Repo

| File | What It Is |
|------|-----------|
| [`prompt.md`](prompt.md) | The ACTUAL system prompt I use — 100+ lines with persona, sourcing rules, and output format |
| [`config/`](config/) | Hermes cron config + infrastructure notes |
| [`samples/`](samples/) | Real daily outputs, collected over weeks |
| `README.md` | You're reading it |

**There is no `main.py` or `docker-compose.yml`** — because this isn't a packaged product. It's a running agent.

---

## 🤔 Why I Built This

After 4 months as an AI Product Intern at Style3D, I left and realized:

- Twitter takes 2 hours/day to stay informed — and you get second-hand takes
- Most AI newsletters are link dumps with zero personalization
- Nobody connects industry news back to *your specific situation*

So I built an agent that:

✅ Reads the internet for me  
✅ Filters for what I actually care about  
✅ Connects dots back to my experience  
✅ Has personality — reads like a friend wrote it  

---

## 💬 Real Talk

Some days the search fails. Sometimes the output is too long for Feishu's message limit. The cron timer gets lost on gateway restarts and needs manual re-triggering.

But it works. Every morning. And it proves something I believe:

> **The best way to demonstrate you can build AI products is to build one that serves you first.**

---

<p align="center">
  <sub>Built with ☕ in Hangzhou · <a href="https://github.com/Techdoll00">Kin Liao</a></sub>
</p>
