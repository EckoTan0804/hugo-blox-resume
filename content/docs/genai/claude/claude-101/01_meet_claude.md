---
# ===== Title, summary, and position in the left sidebar =====
linktitle: Meet Claude  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 101 # Position in the left sidebar
# ============================================================

# ========== Basic metadata ==========
title: Meet Claude
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

**TL;DR**

- **What is Claude:** An AI assistant designed to be a steerable, collaborative thinking partner.
- **Claude's capabilities:** Writing and content creation, research and analysis, coding assistance, problem-solving and reasoning, Learning new things
- **Access:** Available via Claude.ai, Claude Code, Slack, and Excel.
- **Prompting:** Communicate naturally like a coworker. 
  - Provide context / set stage (+ adding context), define tasks, specify rules, and iterate on responses.
  - Personalize claude with *memory* and *styles* to help Claude work better for you.

- **AI Fluency:** Guided by the **4D Framework** (Delegation, Description, Discernment, and Diligence) to evaluate and integrate Claude effectively.

------

## What is Claude

Claude is an **AI assistant** designed to be your thinking partner.

- built to be helpful, harmless, and honest

- more than a chatbot

- designed to be steerable and collaborative

Claude's capabilities

{{< spoiler text="Writing and content creation" >}}
Drafting emails, essays, reports, and creative content with tailored tone and structure.
{{< /spoiler >}}

{{< spoiler text="Research and analysis" >}}

- Summarizing documents, extracting key insights, and performing analysis on text or data.

- Helps you explore research angles, compile findings, and analyze data to surface meaningful insights.

{{< /spoiler >}}

{{< spoiler text="Coding assistance" >}}
Writing, debugging, explaining, and translating code across multiple programming languages.
{{< /spoiler >}}

{{< spoiler text="Problem-solving and reasoning" >}}
Brainstorming ideas, handling complex cognitive tasks, mathematical problems, strategic thinking and analysis, and research
{{< /spoiler >}}

{{< spoiler text="Learning new things" >}}
Explaining complex topics, summarizing concepts, and answering educational queries.
{{< /spoiler >}}

Ways to access Claude

- [Claude.ai](https://claude.ai/): the primary way most people interact with Claude.

- [Claude Code](https://claude.com/product/claude-code): an agentic coding tool that is designed for developers

- [Claude and Slack](https://claude.com/claude-and-slack)

- [Claude for Excel](https://claude.com/claude-for-excel)

## Converation with Claude

The best approach when speaking to Claude is like you would a **coworker—naturally, concisely, and conversationally**.

{{< youtube 0vZ_UVLhSQQ >}}

### Writing effective prompts

1. **Setting the stage**

   - What is your role and what are your objectives? 

   - Is there context about your work that Claude should know about?
2. **Defining the task** 

   - What action do you want Claude to take? 

   - Do you want Claude to write, analyze, build, or something else?
3. **Specifying rules** 

   - What's the style or tone you want Claude to use? 

   - Are there examples that you can attach to show Claude what you're looking for?

Example

> I'm the marketing lead at an indie streaming startup, and we're preparing an investor pitch deck for Series A investors. Can you research the current state of the independent film streaming market and identify key trends, competitor positioning, and growth opportunities? Use current web research with citations and structure it as a professional report of up to 5 pages, with an executive summary, market analysis, competitive landscape, and growth opportunities.

- **Setting the stage**: We tell Claude this is for an investor pitch deck for a new indie streaming app—that's the *context* and *objective*.
- **Defining the task**: We provide the specific *action* (research the market) with relevant *details* (trends, competitors, opportunities).
- **Specifying rules**: We ask for current web research with citations, structured as a professional report—telling Claude exactly what style and format we need.

### Adding context

Uploads, connectors, and custom preferences offer ways to give Claude even more context about your work.

Some practical ways to use file uploads:

- Upload a document and ask Claude to summarize the key points
- Share an image and ask Claude to describe or analyze what it sees
- Attach a spreadsheet and ask Claude to identify trends in the data
- Upload code and ask Claude to explain how it works or find bugs

### Iterating on Claude's responses

Conversations with Claude are meant to be **<u>iterative</u>**.

If Claude's first response isn't quite what you wanted, you have several options:

- **Ask follow-up questions**: Build on Claude's response by asking for more detail, a different angle, or clarification.
  
   - E.g., *"Can you expand on the second point?"* or *"That's helpful, but can you make it more concise?"*

- **Provide feedback**: Tell Claude what you liked and didn't like about its response.

- **Redirect or restart:** If Claude went in a different direction than you intended, simply steer it back.
  
   - E.g., *"Actually, I was asking about X, not Y. Let me clarify..."*
     
   - Worst case, restart your conversation in a new chat to fully refresh the context.

### Personalizing Claude

Two features that help Claude work better for you over time to increase the power of your prompts

- **Memory**: Automatically saves key context from your conversations — your role, preferences, past decisions, and working style — so you don't have to repeat yourself every time you start a new chat.

- **Styles**: let you customize how Claude communicates. Choose from preset options — like concise, formal, or explanatory — or create your own custom style by describing exactly how you want Claude to write.

## Getting Better Results

### Common challenges and how to fix them

As you start working with Claude, you'll likely encounter moments where the response isn't quite what you expected. Here are some of the most common challenges and how to address them:

| Challenge                                                            | What's happening                                                                                                  | Try this                                                                                                                                                                                                                                                                                                                        |
| -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Claude's response is too generic**                                 | Your prompt didn't include enough context about your specific situation                                           | Add details about your audience, role, or constraints. Instead of "Write an email about the project delay," try "Write an email to our enterprise client explaining that the software integration will be delayed by two weeks. They've been patient so far but this is the second delay. Keep it professional but apologetic." |
| **The response is too long (or too short)**                          | Claude is guessing at appropriate length                                                                          | Be *explicit*: "Give me a two-paragraph summary" or "Keep this under 100 words" or "I need a comprehensive analysis—length isn't a concern."                                                                                                                                                                                    |
| **Claude didn't follow my format**                                   | Claude understood *what* you want but not *how* you want it presented                                             | Show, don't just tell. Provide an example of the format, or describe the structure explicitly: "Use bullet points with bold headers for each section."                                                                                                                                                                          |
| **I got confident-sounding information that turned out to be wrong** | Claude occasionally generates plausible but incorrect information, especially with specific facts or niche topics | For high-stakes work, verify key facts independently. Ask Claude to cite sources or indicate confidence level. Enable web search to ground responses in current information.                                                                                                                                                    |
| **The tone isn't right**                                             | Claude defaults to helpful and professional, which may not match your needs                                       | Describe the tone in plain language: "Make this more conversational" or "This should sound authoritative and formal." Provide an example of writing in the style you want.                                                                                                                                                      |

### The iteration mindset

Your first prompt *rarely* produces a perfect result—and that's okay. Think of your initial prompt as the start of a conversation, not a one-shot request.

Effective Claude users:

- **Treat first drafts as starting points.** Review what Claude produces, identify what's working and what isn't, then refine.
- **Give specific feedback.** "Make it shorter" is fine, but "Cut the first two paragraphs and make the conclusion more action-oriented" is better.
- **Know when to start fresh.** If a conversation has gone off track, sometimes it's faster to open a new chat with a clearer prompt than to try to redirect. 

### AI Fluency

AI Fluency is **the ability to collaborate effectively with AI tools**—not just knowing which buttons to click, but developing the judgment to use AI well across different situations.

The **4D Framework for AI Fluency**

{{< spoiler text="Delegation" >}}
- Deciding on what work should be done by humans, what work should be done by AI, and how to distribute tasks between them. 
- Includes understanding your goals, AI capabilities, and making strategic choices about collaboration.
{{< /spoiler >}}

{{< spoiler text="Description" >}}
- Effectively communicating with AI systems. 
- Includes clearly defining outputs, guiding AI processes, and specifying desired AI behaviors and interactions.
{{< /spoiler >}}

{{< spoiler text="Discernment" >}}
- Thoughtfully and critically evaluating AI outputs, processes, behaviors and interactions. 
- Includes assessing quality, accuracy, appropriateness, and determining areas for improvement.
{{< /spoiler >}}

{{< spoiler text="Diligence" >}}
- Using AI responsibly and ethically. 
- Includes making thoughtful choices about AI systems and interactions, maintaining transparency, and taking accountability for AI-assisted work.
{{< /spoiler >}}


### Evaluating Claude for your workflows

As you start integrating Claude into more of your work, you might wonder: how do I know if Claude is actually good at this particular task?

**Evals** (short for evaluations) are a way to develop intuition for assessing Claude's outputs on the tasks that matter to you. They're systematic ways to test how well Claude performs on specific types of tasks that matter to you.

Running simple evals helps you:

- Understand where Claude adds the most value in your workflow
- Identify tasks where you'll need to provide more context or examples
- Build confidence in Claude's outputs for recurring tasks

A simple and practical eval approach:

1. **Gather examples.** Collect 5-10 examples of a task you do regularly—emails you've written, reports you've created, analyses you've done.
2. **Create test prompts.** Write prompts that would generate similar outputs. Include the context you'd naturally have when doing this work.
3. **Compare outputs.** Run your prompts and compare Claude's responses to your examples. Ask yourself:
    - Does Claude capture the key information?
    - Is the tone and style appropriate?
    - What's missing or could be improved?
4. **Refine your approach.** Based on what you learn, adjust your prompts, add examples to show Claude what good looks like, or identify where human review is essential.

## Claude Desktop App

The Claude desktop app gives you three ways to work with Claude: **Chat**, **Cowork**, and **Code**

- **Chat** is the same Claude you know from claude.ai, plus quick entry, screenshots, dictation, and connectors that come from running natively on your computer.

- **Cowork** is an agentic tool — you give it a goal, connect it to your tools and resources, and let it do the work.

- **Code** is for building software, from writing and testing code to deploying it.

|                          | Chat                                                                                             | Cowork                                                                                                          | Code                                                                              |
| ------------------------ | ------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **Optimized for**        | Quicker exchanges: exploring ideas, iterative drafting, quick answers, learning through dialogue | Complex or sustained work: research, analysis, file organization, producing finished documents and deliverables | Building software: writing, testing, running and deploying code                   |
| **Key features**         | Quick entry, dictation                                                                           | Work from local folders, plugins, subagents, scheduled tasks                                                    | Ask/Code/Plan modes, visual diffs, git integration, local and remote environments |
| **Tools and extensions** | Connectors, Skills, Claude in Chrome                                                             | Connectors (local and remote), Skills, Claude in Chrome, Plugins, Computer Use                                  | Connectors, Skills, Claude in Chrome, Plugins, Hooks                              |
