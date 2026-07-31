#!/usr/bin/env python3
"""AI News Briefing Agent — standalone runner.

Usage:
    pip install requests python-dotenv
    cp config.example.yaml config.yaml  # fill in your keys
    python main.py
"""

import os
import sys
import json
import requests
from datetime import datetime, timezone, timedelta

# Timezone
CST = timezone(timedelta(hours=8))

# ── Config ──────────────────────────────────────────────
CONFIG = {}
CONFIG_PATH = os.environ.get("BRIEFING_CONFIG", "config.yaml")

try:
    import yaml
    with open(CONFIG_PATH) as f:
        CONFIG = yaml.safe_load(f)
except ImportError:
    print("⚠️  PyYAML not installed. Using env vars only.")
    CONFIG = {
        "tavily": {"api_key": os.environ.get("TAVILY_API_KEY")},
        "exa": {"api_key": os.environ.get("EXA_API_KEY")},
        "deepseek": {"api_key": os.environ.get("DEEPSEEK_API_KEY"), "model": "deepseek-v4-pro"},
        "feishu": {"webhook_url": os.environ.get("FEISHU_WEBHOOK_URL")},
    }


def search_tavily(query: str) -> list:
    """Search with Tavily."""
    api_key = CONFIG.get("tavily", {}).get("api_key")
    if not api_key:
        return []
    r = requests.post(
        "https://api.tavily.com/search",
        json={"query": query, "max_results": 5},
        headers={"Authorization": f"Bearer {api_key}"},
        timeout=30,
    )
    if r.status_code != 200:
        print(f"  Tavily error: {r.status_code}")
        return []
    return r.json().get("results", [])[:3]


def search_exa(query: str) -> list:
    """Search with Exa (semantic)."""
    api_key = CONFIG.get("exa", {}).get("api_key")
    if not api_key:
        return []
    r = requests.post(
        "https://api.exa.ai/search",
        json={"query": query, "num_results": 3},
        headers={"Authorization": f"Bearer {api_key}"},
        timeout=30,
    )
    if r.status_code != 200:
        print(f"  Exa error: {r.status_code}")
        return []
    return r.json().get("results", [])[:3]


def get_github_trending() -> list:
    """Scrape GitHub trending (lightweight — falls back gracefully)."""
    try:
        r = requests.get("https://github.com/trending?since=daily", timeout=15)
        # Simple extraction of repo names from HTML
        repos = []
        for line in r.text.split("\n"):
            if 'href="/' in line and "/stargazers" not in line:
                # Rough parsing — in production, use BeautifulSoup
                parts = line.split('href="/')
                if len(parts) > 1:
                    path = parts[1].split('"')[0]
                    if path.count("/") == 1 and " " not in path:
                        repos.append(path)
        return list(set(repos))[:8]
    except Exception as e:
        print(f"  GitHub trending error: {e}")
        return []


def call_llm(prompt: str, context: str) -> str:
    """Call DeepSeek to generate the briefing."""
    api_key = CONFIG.get("deepseek", {}).get("api_key")
    model = CONFIG.get("deepseek", {}).get("model", "deepseek-v4-pro")
    if not api_key:
        raise RuntimeError("DEEPSEEK_API_KEY not configured")

    r = requests.post(
        "https://api.deepseek.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "messages": [
                {"role": "system", "content": prompt},
                {"role": "user", "content": f"Today's raw research:\n\n{context}\n\nGenerate the briefing now."},
            ],
            "temperature": 0.7,
            "max_tokens": 3000,
        },
        timeout=120,
    )
    if r.status_code != 200:
        raise RuntimeError(f"LLM error: {r.status_code} {r.text[:200]}")
    return r.json()["choices"][0]["message"]["content"]


def send_feishu(content: str):
    """Send briefing to Feishu via webhook."""
    webhook = CONFIG.get("feishu", {}).get("webhook_url")
    if not webhook:
        print("⚠️  No Feishu webhook configured. Printing to stdout.\n")
        print(content)
        return

    # Simple text message
    payload = {
        "msg_type": "text",
        "content": {"text": content[:4096]},  # Feishu limit
    }
    r = requests.post(webhook, json=payload, timeout=10)
    if r.status_code != 200:
        print(f"  Feishu error: {r.status_code}")
    else:
        print("  ✅ Sent to Feishu")


def main():
    print(f"🤖 AI News Briefing Agent — {datetime.now(CST).strftime('%Y-%m-%d %H:%M')} CST")
    print("=" * 50)

    # 1. Collect data
    print("\n🔍 Searching...")
    github = get_github_trending()
    print(f"  GitHub: {len(github)} trending repos")

    agent_news = search_tavily("AI agent framework launch 2026") + search_exa("AI agent ecosystem news 2026")
    print(f"  Agent news: {len(agent_news)} articles")

    jobs = search_tavily("杭州 AI agent 招聘 2026") + search_exa("Hangzhou AI jobs 2026")
    print(f"  Jobs: {len(jobs)} listings")

    # 2. Build context
    context_parts = []
    if github:
        context_parts.append("## GitHub Trending\n" + "\n".join(f"- {r}" for r in github[:5]))
    if agent_news:
        context_parts.append("## Agent News\n" + "\n".join(
            f"- [{a.get('title','')}]({a.get('url','')})" for a in agent_news[:3]
        ))
    if jobs:
        context_parts.append("## Jobs\n" + "\n".join(
            f"- [{j.get('title','')}]({j.get('url','')})" for j in jobs[:2]
        ))
    context = "\n\n".join(context_parts)

    # 3. Generate briefing
    print("\n🧠 Generating...")
    from prompt import SYSTEM_PROMPT
    briefing = call_llm(SYSTEM_PROMPT, context)

    # 4. Deliver
    print("\n📨 Delivering...")
    send_feishu(briefing)

    # 5. Save to samples
    os.makedirs("samples", exist_ok=True)
    date_str = datetime.now(CST).strftime("%Y-%m-%d")
    with open(f"samples/{date_str}.md", "w") as f:
        f.write(briefing)
    print(f"  💾 Saved to samples/{date_str}.md")

    print("\n✅ Done!")


if __name__ == "__main__":
    main()
