---
# ===== Title, summary, and position in the left sidebar =====
linktitle: Organizing Work and Knowledge  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 102 # Position in the left sidebar
# ============================================================

# ========== Basic metadata ==========
title: Organizing Work and Knowledge
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

## Introduction to Projects


### What are projects?

{{< youtube GJ5jTgcbRHA >}}

**Projects are self-contained workspaces** with their own memory, chat histories, knowledge bases, and customized instructions. Think of them as dedicated environments for specific work streams.

Projects are ideal for s

- toring knowledge Claude should reference
- organizing related chats around a specific topic or work area, 
- collaborating with team members who need access to the same shared context

#### When to use projects

Projects are particularly valuable when you're working on something ***ongoing***—not just a one-off question. Consider creating a project when you have a workflow with:

- **Reference materials you'll use *repeatedly*** (meeting notes, survey results, reports, historical data, etc.)
- ***Consistent* requirements** for how Claude should respond (always use formal language, always cite sources, always follow our template)
- **Team collaboration needs** where multiple people should work from the same foundation

### Creating projects

1. Set up project

2. Add project instructions to tell Claude how to behave across all conversations in this project
  
    - Good project instructions typically include:

      | Instruction | Example |
      | :--- | :--- |
      | **Context about what you're working on** | *"This project is for creating marketing content for our B2B software product."* |
      | **Process instructions** | *"First consider a blog structure that will entice this audience, then write the draft."* |
      | **Tone and style preferences** | *"Use a professional but conversational tone. Avoid jargon when possible."* |
      | **Specific requirements** | *"Always include a call-to-action at the end of marketing copy."* |
    
    - You can also use project instructions to automate workflows (Think of instructions as programming Claude's behavior for this project.)
      
       - E.g., *"When I upload a meeting transcript, create a structured summary using this template."*

3. Build knowledge base 
  
    - Knowledge base is where you upload documents that Claude should reference
    
    - What to upload:
      
       - Reference documents
       
       - Background materials
       
       - Technical documentation or specifications
       
       - Examples of work you want Claude to emulate
       

  {{% callout note %}}
  **Pro tip:** Name your files descriptively. Claude uses file names to understand and retrieve the right information.
  {{% /callout %}}

4. Working within project
  
   Once your project is set up, you can start chatting with Claude. Each conversation within the project automatically has access to your knowledge base and follows your project instructions.


### Examples

{{< spoiler text="Q4 product launch" >}}
Upload your product specs, competitive analysis, and messaging brainstorming notes. Claude will have this context top of mind for any inquiry or document draft.
{{< /spoiler >}}

{{< spoiler text="Research support" >}}
Centralize your competitive review, user research data, and customer feedback. Claude can help you synthesize sources, draft reports, and maintain consistency across recommendations.
{{< /spoiler >}}

{{< spoiler text="Client account hub" >}}
Keep your client's brand guidelines, past deliverables, and communication history in one place. Set instructions so Claude matches their tone and references their specific context when creating proposals or reports.
{{< /spoiler >}}

{{< spoiler text="Event planning workspace" >}}
Upload venue contracts, speaker bios, and attendee data. Claude can help generate run-of-show documents, attendee communications, and post-event reports that stay consistent with your event's theme.
{{< /spoiler >}}

{{< spoiler text="Job description generator" >}}
Gather past job descriptions, team charters, and internal headcount request docs. Work with Claude to draft job descriptions that reflect your team's actual work and culture.
{{< /spoiler >}}


### Best practices for projects

{{< spoiler text="Start focused, then expand" >}}
Begin with a specific use case rather than trying to create one project for everything. You can always add more content as you go.
{{< /spoiler >}}

{{< spoiler text="Keep your knowledge base current" >}}
Outdated documents can lead to outdated responses. Review and update your project knowledge periodically.
{{< /spoiler >}}

{{< spoiler text="Write clear instructions" >}}
Be specific about what you want. Vague instructions lead to inconsistent results.
{{< /spoiler >}}

{{< spoiler text="Name your documents descriptively" >}}
(e.g., 'Q4-2025-Sales-Report.pdf' not 'report.pdf') and group related files together. Claude uses filenames and proximity to understand relationships between documents.
{{< /spoiler >}}

{{< spoiler text="Reference documents by name" >}}
When asking questions, you can mention specific documents to help Claude focus its search: "Based on our Q3 report, what were the top customer concerns?"
{{< /spoiler >}}


## Creating with Artifacts

### What are artifacts?

Artifacts are standalone, interactive outputs that Claude creates in a dedicated window alongside your conversation.

### Common artifact types

- **Documents**: including markdown, plain text, Word docs, PDFs, PowerPoint, and Excel.

- **Code snippets**: Working code in any programming language.

- **HTML pages:** Complete web pages with HTML, CSS, and JavaScript in a single file.

- **SVG images**

- **Mermaid diagrams:** Flowcharts, sequence diagrams, Gantt charts, org charts, and more.

- **React components**: Interactive UI elements with real functionality—calculators, dashboards, games, data visualizations.

### Creating artifact

Creating an artifact is as simple as having a conversation. Just describe what you want, and Claude will determine whether to present it as an artifact.

If Claude doesn't automatically create an artifact when you expect one, you can explicitly ask: "Create this as an artifact" or "Show me this in an artifact."

### Tips for getting the most from artifacts

{{< spoiler text="Be specific about what you want" >}}
Specify layout preferences, design requirements, style options, and specific functionalities you expect the artifact to have.

Example: "Build a monthly budget tracker where I can input expenses by category, see a pie chart breakdown, and get a warning when I'm over budget" is better than just "Build a budget tracker".

{{< /spoiler >}}

{{< spoiler text="Describe the end user" >}}
Telling Claude who will use the artifact helps it make appropriate design choices.
{{< /spoiler >}}

{{< spoiler text="Iterate incrementally" >}}
Ask Claude to add one feature or make ***one change at a time***. This makes it easier to identify what's working and catch issues early.
{{< /spoiler >}}

{{< spoiler text="Request artifacts when needed" >}}
If you ask for something substantial and Claude responds in the chat instead of creating an artifact, just say "Please create that as an artifact."
{{< /spoiler >}}

## Working with Skills

### What are Skills?

**Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks.** Think of them as ***expertise packages***—they teach Claude how to complete specific tasks in a repeatable way.

### Types of Skills

- **Anthropic Skills** 
   - Created and maintained by Anthropic. 
   - Include enhanced document creation capabilities for Excel, Word, PowerPoint, and PDF files. 
   - Anthropic Skills are available to all paid users and Claude invokes them automatically when relevant—you don't need to do anything special to use them.
- **Custom Skills** are ones you or your organization create for specialized workflows and domain-specific tasks.
   - For example, you might create a skill that applies your company's brand guidelines to presentations, structures meeting notes in a specific format, or executes your organization's data analysis workflows.

### Using Skills in practice

You typically don't need to think about them—Claude handles skill selection automatically based on your request.

#### Security considerations

Because Skills can include executable code, it's important to use them thoughtfully:

- Only install custom Skills from trusted sources
- Anthropic's built-in Skills are tested and maintained by Anthropic
- Custom Skills you upload are private to your individual account
- If you're installing a custom Skill from an external source, review its contents before use to understand what it does.

### Creating custom skills

Custom Skills let you teach Claude your specific workflows, brand guidelines, and ways of working—so Claude can apply that knowledge automatically whenever it's relevant.

The easiest way to create a custom Skill is through **conversation with Claude itself**. You don't need to write code or manually create files—Claude handles the technical structure for you.

1. **Start a new chat** and tell Claude what you want to create.
    - E.g., *"I want to create a skill for writing quarterly business reviews" or "I need a skill that applies our brand guidelines to presentations."*

2. **Answer Claude's questions.**

   Claude will interview you about your workflow, asking things like: What should this skill do? What makes good output for this type of work? Can you give examples of when you'd use this skill?

3.  **Upload reference materials** if you have them (templates, style guides, brand assets, or examples of work, etc.).

4. **Save your skill.** When finished, Claude generates a file containing your properly structured skill. All you have to do is save it and the skill will be ready for Claude to use.

### Skills vs. Projects

Think of it this way: **projects store knowledge, skills perform tasks**.

- **Projects** are knowledge hubs. 
  
   - They hold the reference materials Claude needs to understand your work—project specs, meeting notes, research documents. 
   
   - When you upload files to a project, Claude draws on that information across every conversation within that project.

- **Skills** are procedural machines. 
  
   - They encode *how* Claude should execute a task—the specific steps, order of operations, and methodology you want followed every time. 
     
   - Skills shine when you have repeatable workflows you want Claude to run consistently.

The two features complement each other: A skill can reference knowledge stored in a project. The project provides the *what* (information), the skill provides the *how* (process).

|                 | Projects                                                   | Skills                                                                |
| --------------- | ---------------------------------------------------------- | --------------------------------------------------------------------- |
| **Purpose**     | Store knowledge Claude references                          | Define processes Claude executes                                      |
| **Best for**    | Long-term context, reference materials, team collaboration | Repeatable workflows, multi-step tasks, consistent methodology        |
| **Example**     | Customer hub, research buddy, feedback generator           | Process guidelines (like brand or legal), Blog drafting, PDF creation |
| **Persistence** | Knowledge available across all chats in the project        | Instructions applied when the skill is invoked                        |

{{< spoiler text="Example" >}}
If we think of Claude as a digital employee, **a Project is his "dedicated office" that stores all the background knowledge (the What)**—such as medical data and design specs for a "Cat Health App"—ensuring he always has access to these reference materials whenever he is in this office. On the other hand, **a Skill is a "standard operating procedure (the How)" that he has mastered**—such as a structured workflow for crafting social media posts by extracting selling points, adding emojis, and generating catchy headlines. When you ask him to write a post within the "Cat App Office (Project)," he instantly runs his "content creation assembly line (Skill)," flawlessly processing the professional cat data from the project into a highly engaging, structured, and polished output.
{{< /spoiler >}}
