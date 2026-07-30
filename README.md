# 🤖 AI News Briefing Agent

> 一键部署的飞书 AI 每日早报机器人 —— 每天早上 9 点,自动抓取 AI 领域最新资讯,经 LLM 摘要后推送到飞书群。

## ✨ 这是什么

一个基于 Hermes Agent 框架的自动化资讯机器人。它会在每天固定时间:
1. 用 Tavily / Exa 搜索 AI 领域最新新闻
2. 用 LLM 提取要点、生成中文摘要
3. 通过飞书 Webhook 推送到指定群聊

面试官 30 秒就能看懂:这是一个真正在跑的 Agent 产品,不是玩具 Demo。

## 🚀 部署步骤

### 前置准备
- Hermes Agent 运行环境
- Tavily API Key(或 Exa API Key)
- 飞书自定义机器人 Webhook URL

### 1. 配置定时任务(Hermes Cron)

在 Hermes 中创建一个 cron 任务:

```yaml
schedule: "0 9 * * *"  # 每天早上 9 点
agent: ai-news-briefing
prompt: |
  搜索今天 AI 领域的 5 条最重要新闻,
  每条生成 100 字以内的中文摘要,
  按重要性排序后推送到飞书群。
```

### 2. 配置搜索源

```bash
TAVILY_API_KEY=tvly-xxxxx
# 或
EXA_API_KEY=exa-xxxxx
```

### 3. 配置飞书 Webhook

在飞书群中添加自定义机器人,获取 Webhook URL:

```bash
FEISHU_WEBHOOK_URL=https://open.feishu.cn/open-apis/bot/v2/hook/xxxxx
```

### 4. 启动

```bash
python main.py
```

## 📱 推送内容示例

每天早上 9:00,飞书群会收到如下消息:

```
📰 AI 日报 | 2026-07-30

1️⃣ OpenAI 发布 GPT-5,多模态推理能力大幅提升
   GPT-5 在 MMLU、GPQA 等 benchmark 上刷新纪录,
   新增「深度思考」模式,支持 1M token 上下文。
   来源:OpenAI Blog

2️⃣ Anthropic 推出 Claude 4,编程能力对标人类高级工程师
   SWE-bench 通过率达 72%,支持 200K 上下文窗口,
   新增 Artifacts 实时协作功能。
   来源:Anthropic

3️⃣ Google DeepMind 发布 Gemini 2.0 Ultra
   原生多模态架构,支持视频实时理解,
   在 MMMU 基准上达到 85% 准确率。
   来源:Google AI Blog

4️⃣ Meta 开源 Llama 4,405B 参数模型免费可用
   性能对标 GPT-4,支持商业用途,
   已在 Hugging Face 上线。
   来源:Meta AI

5️⃣ Agent 框架 LangGraph 1.0 正式发布
   支持复杂多 Agent 编排、状态管理、
   人机协作节点,生产可用。
   来源:LangChain Blog

— 由 AI News Briefing Agent 自动生成
```

## 🛠 技术栈

| 组件 | 技术 |
|------|------|
| Agent 框架 | Hermes |
| 搜索引擎 | Tavily / Exa |
| LLM | GPT-4o / Claude |
| 推送渠道 | 飞书 Webhook |
| 定时调度 | Hermes Cron |
| 语言 | Python 3.11+ |

## 📁 项目结构

```
ai-news-briefing-agent/
├── main.py              # 入口
├── agents/
│   └── briefing.py      # 早报 Agent 逻辑
├── tools/
│   ├── search.py        # Tavily/Exa 搜索封装
│   ├── summarize.py     # LLM 摘要
│   └── feishu.py        # 飞书推送
├── config/
│   └── settings.yaml    # 配置文件
├── prompts/
│   └── briefing.txt     # 提示词模板
├── .env.example
└── requirements.txt
```

## 📄 License

MIT
