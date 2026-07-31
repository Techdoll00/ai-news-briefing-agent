# 🤖 AI News Briefing Agent

> I am Huanhuan's AI news briefing agent. Every morning at 9:00 AM CST, I scan GitHub Trending and the web, then deliver a curated AI daily briefing to his Feishu DM.

## Architecture

```
GitHub Trending → Tavily → Exa → DeepSeek V4 Pro → Feishu Message
```

| Component | Tool |
|-----------|------|
| Agent Framework | Hermes Agent |
| Web Search | Tavily + Exa |
| LLM | DeepSeek V4 Pro |
| Delivery | Feishu/Lark API |
| Scheduling | Hermes Cron (systemd on VPS) |
| Infrastructure | Tencent Cloud 2-core 4GB, Hangzhou |

## What Goes Into Each Briefing

| Section | Source |
|---------|--------|
| 🐙 GitHub Highlights | GitHub Trending (AI/Agent/DevTools filtered) |
| 🤖 Agent Ecosystem | Tavily + Exa web search |
| 🎯 Hiring Signals | Search for Hangzhou AI job listings |
| 🛠️ Tool of the Day | Product Hunt / Hacker News |
| 🧩 Knowledge Connection | Ties news back to reader's experience |

## Sample Output

> 🌅 早安宝贝～☀️💕 2026年7月30日
>
> 🐙 affaan-m/ECC ⭐234K — Agent harness 性能优化系统
> 🤖 Anthropic 反对完全开放权重模型 (HN榜首)
> 🎯 阿里云 Agent Infra工程师 (杭州，招2000人)
> 🛠️ Prefactor — Agent 实时评估平台 (PH榜首)
>
> 爱你哟～ (◕‿◕✿)

## Why This Exists

Most AI news aggregators summarize headlines. This agent:

- Curates for one specific person — every item filtered for relevance
- Connects dots — ties news back to the reader's real experience
- Has personality — reads like a friend wrote it

Built as a demonstration of "Agent Productization" — from idea to daily-running autonomous system.

## Full Prompt

See [prompt.md](prompt.md) for the complete system prompt and cron configuration.

---

*Running daily since July 2026 on a 2-core 4GB VPS in Hangzhou.*
