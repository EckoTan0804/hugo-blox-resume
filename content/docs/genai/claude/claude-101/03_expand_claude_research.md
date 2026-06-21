---
# ===== Title, summary, and position in the left sidebar =====
linktitle: Expand Claude Research  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 103 # Position in the left sidebar
# ============================================================

# ========== Basic metadata ==========
title: Expand Claude Research
date: 2026-06-02
draft: false
authors:
  - admin
tags:
  - Claude
  - GenAI
  - LLM
categories:
  - GenAI
toc: true # Show table of contents
# ====================================

# ========== Advanced metadata =========
profile: false  # Show author profile?
reading_time: true # Show estimated reading time?
share: true  # Show social sharing links?
featured: true
comments: true  # Show comments?
disable_comment: false
commentable: true  # Allow visitors to comment? Supported by the Page, Post, and Book content types.
editable: false  # Allow visitors to edit the page? Supported by the Page, Post, and Book content types.

# Optional header image (relative to `assets/media/` folder).
header:
  caption: 
  image:  
---

## Connecting Tools


### What are connectors?

- Connectors transform Claude **from an assistant into an informed collaborator** by giving Claude access to the same tools, data, and context that you use every day. -> Instead of starting every conversation from scratch, Claude can work directly with your *actual* information.

- Connectors allow Claude to read information and perform actions on your behalf.

- The **Model Context Protocol (MCP)** powers connectors. 
  
  - MCP is like USB-C for AI—a universal standard that allows Claude to connect to many different applications through a *single, consistent* interface.
  
  - Following this open standard, developers can build connectors for any tool, and those connectors work seamlessly with Claude.

- Two types of connectors: **web connectors** and **desktop extensions**. 
  
  - **Web connectors** link Claude to cloud services like Google Drive, Notion, Slack, and Asana.
  
  - **Desktop extensions** run locally on your computer through the Claude Desktop app, giving Claude access to local files and native applications.

### Finding and connecting tools

Anthropic maintains a directory of recommended connectors at claude.ai/directory. The directory is organized into two tabs:

- **Web:** Cloud services and applications (Gmail, Notion, Slack, Asana, Linear, Stripe, and many more)
- **Desktop extensions:** Local tools that run on your computer through the Claude Desktop app

### Using connectors in work

Once you've connected your tools, Claude considers them when responding to your requests.

Some practical ways to use connected tools:

**Project management (Asana, Linear, Jira)**

- "What are my highest priority tasks due this week?"
- "Create a new task for reviewing the Q4 budget proposal"
- "Summarize the status of our product launch project"

**Communication (Slack, Gmail)**

- "Find the email thread where we discussed the vendor contract"
- "Draft a reply to the latest message in the #marketing channel"
- "What did the team decide about the timeline in yesterday's discussion?"

**Documentation (Notion, Google Drive, Confluence)**

- "Search our documentation for our brand voice guidelines"
- "Summarize the meeting notes from last week's product review"
- "What does our style guide say about using contractions?"

**Business tools (Stripe, PayPal, Salesforce)**

- "Show me revenue trends for the past quarter"
- "What's the status of the Acme Corp opportunity?"
- "List recent transactions over $1,000"

### Security and permissions

Important considerations:

- **Scoped access:** Permissions are specific to what the connector needs and you can toggle individual permissions on and off within each application's menu.
- **Claude sees what you see:** Claude can only access data *you* have access to. Connecting your work email doesn't give Claude access to your CEO's inbox—only your own.
- **Revocable at any time:** You can disconnect a service through Claude's settings or through the third-party service's security settings. Just as with Skills, you can also find or build custom connectors. Exercise the same caution — only install connectors from trusted sources.

## Enterprise Search

## Research Mode for Deep Dives

### What is Research?

Research is an advanced feature that transforms Claude from a conversational assistant into a systematic investigator. 

- When you enable Research, Claude doesn't just answer your question—**it explores it from multiple angles, synthesizing information from across the web and your connected integrations.** -> Think of it as having a skilled research assistant who can help gathering information, cross-referencing sources, and compiling a comprehensive report.

- Research is particularly valuable when you need *more than a quick answer*. It's designed for situations where a thorough understanding requires pulling together information from multiple sources, comparing different perspectives, and synthesizing findings into actionable insights.

### When to use Research

**Use Research when you need:**

- Comprehensive reports that synthesize information from multiple sources
- In-depth analysis across the web and your connected integrations (like Google Workspace)
- Thorough investigations that would typically require hours of manual work
- Comparative analysis, such as evaluating competitors or vendor options
- Reports with citations you can verify

**Research is ideal for tasks like:**

- Market analysis and competitive research
- Planning complex projects, like team offsites or product launches
- Synthesizing information from your email, calendar, and documents
- Creating technical documentation that draws from multiple sources
- Preparing briefings that require current, verified information

**Consider web search instead when:**

- You need a quick, specific fact (like today's stock price or a company's address)
- The answer requires only one or two sources
- Speed matters more than comprehensiveness

**Consider extended thinking instead when:**

- You need deep reasoning on a complex problem that doesn't require external information
- You're working on mathematical problems, code debugging, or logical analysis
- The answer comes from reasoning through a problem rather than gathering information

**Consider enterprise search instead when:**

- You need answers that draw from your organization's internal knowledge — documents, Slack threads, emails, meeting notes
- You're onboarding and want to quickly find how your company handles something (like policies, processes, or past decisions)
- You're asking a question that's specific to your company, not the public web

### How Research works

Enable Research = Activate an agentic, multi-step process that goes far beyond a simple web search

Claude autonomously decides what to search next based on what it has already found, pursuing leads and filling gaps *without* you needing to direct each step.

1. **Claude plans its approach.** When Research is enabled, extended thinking automatically activates. This lets Claude break down your request, identify what information it needs, and plan how to investigate different angles of your question.

2.  **Claude conducts multiple searches.** Rather than running a single search, Claude conducts many searches that build on each other. It determines what to investigate next based on what it finds, pursuing promising leads and filling in gaps.

3. **Claude synthesizes findings.** After gathering information from multiple sources—including the web and any connected integrations like Gmail, Google Calendar, or Google Drive—Claude compiles everything into a comprehensive, well-organized report.

4. **Claude provides citations.** Every claim in Research reports links back to its source, making it easy to verify information and dig deeper when needed.

### Tips for effective Research prompts

- **Be specific about your goals.** Instead of "Tell me about the EV market," try "Analyze the electric vehicle battery market—identify key players, technology trends, and supply chain challenges that might affect investment decisions."
- **Specify the sections or structure you want.** Claude will organize its findings around the structure you provide. For example: "Compare venue options for a team offsite including: location and accessibility, meeting space and amenities, catering options, and pricing considerations."
- **Include relevant constraints.** Budget ranges, timelines, geographic requirements, and other parameters help Claude focus its research on relevant options.
- **Ask Claude to help refine your prompt.** If you're not sure how to frame your research question, you can even ask Claude to help you write a better Research prompt before enabling the feature.

### Working with connected integrations

When you have Google Workspace or other integrations connected, Research becomes even more powerful. Claude can pull context from your emails, calendar, and documents alongside web research.
