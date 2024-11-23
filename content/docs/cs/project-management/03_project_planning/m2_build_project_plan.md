---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 302
# ============================================================

# ========== Basic metadata ==========
title: Build Project Plan
date: 2024-07-19
draft: false

authors:
  - admin
tags:
  - project-management
categories:
  - Project Management
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

## Building a Project Plan

### Components of a project plan

At the center of the project plan: **project schedule**

Most project plans contain five basic elements

- **Tasks**
- **Milestones**
- **People**
  - Each team member should understand their role and the tasks they're responsible for completing.
  - Make sure that everyone is clear on their assigned tasks frees you up to focus on managing the project and creates a sense of personal responsibility for members of the team
- **Documentation**
  - RACI chart
  - Charter, which clearly defines the project and outlines the details needed to reach your goals
  - Documents like your budget and risk management plan.
- **Time**

In addition, you should also include the following components in your project plan: 

- Scope and goals (captured initially in your **project charter**)
- Work Breakdown Structure (WBS)
  - Breaks the work down into more manageable pieces
  - The tasks should be visible in one place with clear descriptions, owners, and due dates. 
    -> This will allow you and your team to understand who is responsible for which tasks and when each task is supposed to be completed.
- Budget 
- Management plans
  - *E.g.*, change management plan, risk management plan, and communication plan



## Using Estimation to Set Project Timelines

### Making realistic time estimates

<mark>**Time estimation**</mark>: A prediction of the total amount of time required to complete a task.

<mark>**Effort estimation**</mark>: A a prediction of the amount and difficulty of active work required to complete a task.

{{% callout  note %}}
Difference between effort and time estimation:
- Effort quantifies the amount of time it will take a person to complete work on a task
- Time refers to the overall duration of the task from start to finish. That includes inactive time.

{{% /callout %}}

<span style="color: #d65d48;">Unrealistic effort estimates happen when you've *underestimate* the amount of time it'll take to complete a task!</span>

**How to avoid making unrealistic or inaccurate effort estimates?**

- Communicate with teammates assigned to each task
  - Your teammates will have the most realistic understanding of the amount of work required to complete a task and should be able to provide you with the best estimate.
- Ask follow-up questions, or even gently push back on their estimate, as needed.

- Add buffer in your time schedule
  - <mark>**Buffer**</mark>: Extra time added to the end of a task or a project to account for unexpected slowdowns or delays in work progress.
    - **Task buffer**: Extra time tacked on to a specific task
      - Should be used primarily for tasks that are out of the project team's control
      - Should be used more sparingly for tasks within the project team's control
    - **Project buffer**: Extra time to the overall project schedule
      - You can add extra time as a buffer towards the end of your project schedule. Then you can use that extra time as needed throughout the project. 

{{% callout  note %}}

**Key takeaway**

- Be realistic when estimating time and effort for a project. 
- Take the time to carefully evaluate potential risks and the impact on the work, and talk to your team members about these challenges. 
- Don’t be afraid to escalate potential concerns to management. 
- Optimism is a trait of a great project manager and leader, but it can adversely affect your projects when it comes to time estimation. 

{{% /callout %}}

### Overcoming the planning fallacy

The **planning fallacy** describes our tendency to underestimate the amount of time it will take to complete a task, as well as the costs and risks associated with that task, due to **optimism bias**. Optimism bias is when a person believes that they are *less likely* to experience a negative event.

The planning fallacy can happen to anyone, regardless of whether or not they have experience completing similar tasks. In project management, you may be brand new to this kind of project or you may have managed tons of similar projects before, you still need to be careful not to underestimate the time it will take to complete each task on this particular project. 

As a project manager, you should aim to balance being aware of the planning fallacy with keeping an optimistic attitude about the project, even as things change. **Be optimistically realistic: Push for the best outcomes while planning for the proper time it may take to accomplish each task.**

### Capacity planning and the critical path

<mark>**Capacity**</mark>: The amount of work that the people or resources assigned to the project can reasonably complete in a set period of time.

<mark>**Capacity planning**</mark>: The act of allocating people and resources to project tasks, and determining whether or not you have the necessary resources required to complete the work on time.

<mark>**Critical path**</mark>: The list of project milestones that you must reach in order to meet the project goal on schedule, as well as the mandatory tasks that contribute to the completion of each milestone.

- Includes the bare minimum number of tasks and milestones you need to reach your project goal.

> *Example*
>
> *Tasks on the critical path for launching Project Plant Pals might include hiring plant vendors, developing a new website, and fulfilling deliveries. A task like adding flowers to your product lineup is nice to have, but might not have much impact on the overall success of your project because this task isn't crucial to your launch. These tasks aren't part of the critical path.*

**To determine the critical path of a project**

1. Start by listing all the tasks required to complete the project and the milestones they feed into, which is a perfect time to think back to your [work breakdown structure (WBS)]({{< relref "m1_begin_planning_phase.md/#creating-a-work-breakdown-structure" >}})
2. Determine which tasks on the list absolutely can't begin until another task is complete ("dependency")
3. Work with your team to make time estimates for each task, and map each task from start to finish. The longest path is your critical path. 

**Factors that can impact capacity and capacity planning**

- Identify which task can happen in parallel (happen at the same time as other tasks) and which can happen sequentially (must happen in a specific order)

> *Example*
>
> *A sequential task for your Plant Pals project may include needing budget approval before hiring a vendor.* 
>
> *And two parallel tasks might include hiring delivery drivers and the development of a website. These tasks have no relationship to one another, as they focus on different portions of the project, and can be completed by different members of the team. That means that one task can begin even if the other task hasn't been completed, and so the work to complete these tasks can happen at the same time.*

- Determine which project tasks have a fixed start date
- Determine which project tasks have an earliest start date
- Identify if a task has float (a.k.a. slack)
  - <mark>**Float**</mark>: The amount of time you can wait to begin a task before it impacts the project schedule and threatens the project outcome
  - These are high priority tasks that have low to no wiggle room
  - Task on the critical path should have <u>ZERO</u> float

#### Why the critical path is critical?

The critical path

- Helps you determine the essential tasks that need to be completed on your project to meet your end goal and how long each task will take
- Provides a quick reference for critical tasks by revealing which tasks will impact your project completion date negatively if their scheduled finish dates are late or missed
- Helps you define the resources you need, your project baselines, and any flexibility you have in the schedule

### Creating a critical path

You can think of the critical path as a framework that tells you, the project manager, where you are, where you are headed, and when you will get there. 

General steps for creating a critical path that are applicable to most projects

1. **Capture all tasks** 

   - Use the key planning documents you have created (such as WBS)
   - Main goal: make sure that you aren’t missing a key piece of work that is required to complete your project. 
   - Focus on the essential, “need to do” tasks, rather than the “nice to do” tasks that aren’t essential for the completion of the project.

2. **Set dependencies **

   - Figure out which tasks must be completed before other tasks can start
   - Ask:
     - Which task needs to take place before this task?
     - Which task can be finished at the same time as this task?
     - Which task needs to happen right after this task?

3. **Create a network diagram**

   - The network diagram help visualize
     - The path of the work from the start of the project (excavation) to the end of the project (flooring)
     - Which tasks can be performed in parallel and in sequence
     - Which non-essential tasks are NOT on the critical path

   Example: building the structure of a house

   ![截屏2024-11-17 23.01.34](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/%E6%88%AA%E5%B1%8F2024-11-17%2023.01.34.png)

4. **Make time estimates**
   - After determining tasks and dependencies, consult key stakeholders to get accurate time estimates for each task
   - Time estimates can be reviewed and updated throughout the project, as necessary. 
5. **Find the critical path**
   - Add up the durations for all of your “essential” tasks and calculate the longest possible path, you can determine your critical path
   - Only include the tasks that, if they go unfinished, will impact the project’s finish date
   - Two common approaches
     - **Forward pass**
       - Start at the <u>beginning</u> of your project task list and add up the duration of the tasks on the critical path to the end of your project. 
       - When using this approach, start with the first task you have identified that needs to be completed before anything else can start. 
     - **Backward pass**
       - Start with the <u>final</u> task or milestone and move backwards through your schedule to determine the shortest path to completion. 
       - When there is a hard deadline, working backwards can help you determine which tasks are actually critical. 
       - You may be able to cut some tasks—or complete them later—in order to meet your deadline. 

{{% callout  note %}}

Read more about each of these concepts and critical path calculation methods in the following articles:

- [How to Use the Critical Path Method for Complete Beginners](https://www.workamajig.com/blog/critical-path-method)
- [Critical Path Method: A Project Management Essential](https://www.wrike.com/blog/critical-path-is-easy-as-123/)

{{% /callout %}}

### Getting accurate time estimates from your team

Use soft skills to gather accurate estimates from your teammates

{{< spoiler text="Asking the right questions" >}}

- Ask effective, open-ended questions that lead to the answers you're seeking

  - Open-ended question: A question that cannot be answered with a yes or a no.
  - The answer provides the relevant details of what you need to know.

  > Example
  >
  > You've discussed the design of the new website with your web designer, and you'd like to know how long it will take them to mock up designs for your review.
  >
  > Asking question like, "Can you complete the mock-ups in one week?" is a closed-ended question and might elicit a simple yes or no answer, which doesn't tell you much about the task of designing a website or about your teammate's working style.
  >
  > You might ask the web designer something like, "How long does it typically take you to mock up a website design like this one?" This is an open-ended question and is more likely to elicit a more detailed response. From there, you can ask follow up questions like, "how complex are the steps to complete this task?" "What are the risks associated with this task?" And, "when do you think you can have this ready?"

- By asking your teammates effective, open-ended questions about their assigned tasks, you can learn more about how they work and what they do. As you have more of these conversations, you will develop a better sense of your teammates roles and their tasks, and you will be able to rely less on your team to make accurate estimates.

{{< /spoiler >}}

{{< spoiler text="Negotiating effectively" >}}

- Can help you influence a team member to make your project their priority, by collaborating to find an outcome that works for everyone.

- Example

  > Imagine that the website designer estimates it will take them two weeks to mock up the website design for review. But perhaps you were hoping that the estimate might be closer to one week. To arrive at an estimate that works for both you and the designer, you might gently challenge the estimate by asking follow-up questions. Perhaps you'd ask if their estimate includes mocking up designs for multiple pages. If so, you might ask if the designer is able to share one or two pages with you sooner than their proposed deadline.

- By negotiating effectively with your teammates, you can create a sense of shared ownership over the project outcomes and create a schedule that aligns with everyone's workload.

{{< /spoiler >}}

{{< spoiler text="Practicing empathy" >}}

- <mark>**Empathy**</mark>: A person's ability to relate to the thoughts and feelings of others

- Practicing empathy at work can be a very effective way to build trust with your team

  - When you're discussing estimates with the team, you might practice empathy by asking each person about their workload, including work outside of your project and the overall work-life balance.
  - You might also ask if they've scheduled vacation or leave during the duration of the project, or if there are crucial holidays in which they won't be working

  This can help you avoid assigning tasks when teammates are unable to complete them on time.

{{< /spoiler >}}

## Utilizing Tools to Build a Project Plan

### Developing a project schedule

An **anchor** of a good project plan is a clear schedule containing all the tasks of a project, their owners, and when they need to be completed. Once you have your project schedule, you can build a solid plan around that schedule using tools like spreadsheets and Asana.

<mark>Gantt chart</mark>: A horizontal bar chart that maps out a project schedule.

- A highly visual representation of a projects tasks with clear breakdowns of who's responsible for the work and when those tasks are due
- Almost like calendars: Gantt charts feature the start and end dates of each task, and the bars align with how much time is devoted to each of those tasks.

Example:

![截屏2024-11-19 23.24.55](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/%E6%88%AA%E5%B1%8F2024-11-19%2023.24.55.png)

A straightforward way to make a Gantt chart is using the spreadsheet.

- Organize your left columns by items like task title, task owner, start date, due date, duration, and percent of task complete. Include relevant information in the rows below, organized by start date.
- On the right side of your sheet, you'll order your columns by the weeks estimated to complete the project from start to finish. In the rows below that, you'll include bars representing the dates when certain tasks will take place.

### Project plan best practices

{{< spoiler text="Carefully review deliverables, milestones, and tasks" >}}

During the initiation phase, you'll recall that you created a project charter with important information regarding your project, like your goal, scope, and deliverables. When a project enters the planning phase, your plans become more granular. 

You'll need to break down every deliverable into milestones and tasks to ensure that you and your team have a clear picture of what needs to be done to meet your project's goals. Your plan revolves around completing each and every tiny task, so you should take your time to get this piece right.

{{< /spoiler >}}

{{< spoiler text="Give yourself time to plan" >}}

- Using the strategies like effort estimation and capacity planning can help you and your team get a realistic sense of how long the project will take and when you'll be able to hit your milestones. 
- It's also important to allow for buffer time, since projects rarely go exactly as planned.

{{< /spoiler >}}

{{< spoiler text="Recognizing and planning for the inevitable: things will go wrong" >}}

- Buffer is a helpful tool for mitigating issues related to slowdowns in progress

{{< /spoiler >}}

{{< spoiler text="Staying curious" >}}

- It's so important to sit down with your teammates during a planning phase and ask lots and lots of questions
- To keep the project running smoothly, it's also important to understand the expectations, priorities, risk assessments, and communication styles of your stakeholders and vendors.

{{< /spoiler >}}

{{< spoiler text="Championing your plan" >}}

To achieve buy-in from your teammates and stakeholders on your project plan, champion it! Tell your team why it benefits them to stay on top of the plan. By doing so, you may influence your teammates to stay on track and update the plan regularly.

{{< /spoiler >}}

### Creating a project plan: Tools and templates

Regardless of what tool you use, be sure to include this key information: 

- **Task ID numbers** or **task names**
  You might end up with dozens, hundreds, or even thousands of tasks in a project. Assigning a task ID or name makes it easy to find and reference a task when communicating with team members and stakeholders. 
- **Task durations**
  A task duration is the amount of time you estimate that task should take. Adding task durations to your project plan helps you organize and prioritize the tasks in the project to help ensure you hit your goal on time. 
- **Start and finish dates** 
  Including start and finish dates for each task helps you track whether you are progressing on time or not. 
- **Who is responsible for what** 
  Including each team member’s role and responsibilities helps promote clarity and efficiency. As a best practice, assign an owner to each task, as well.

#### Using a spreadsheet to build a project plan

Spreadsheets are an excellent tool to use for project plans, particularly for projects that are less complex and that have a clear assignment of tasks.

Templates:

- [Smartsheet: Project Plan Templates for Microsoft Word](https://www.smartsheet.com/content/project-plan-templates)
- [Smartsheet: Project Plan Templates for Google Sheets](https://www.smartsheet.com/free-google-docs-templates-google-timeline-templates)
- Google Project Plan Timeline Template](https://docs.google.com/spreadsheets/d/1TauRTFipsWDWGqaw6tmqJeknKhVI5IjR5jJvBfVzfGw/template/preview)
- [Microsoft Gantt Chart Template](https://create.microsoft.com/en-us/template/simple-gantt-chart-4bf6b793-490f-4623-84ca-c9c6251a91fc)

### Kanban boards

**Kanban boards** are a visual tool used to manage tasks and workflows. Kanban boards can be created on whiteboards, magnetic boards, poster boards, computer programs, and more. Tasks associated with the project are written on cards. These cards are placed in columns, which represent the progress made. 

Although Kanban boards are useful for all kinds of projects, they are typically most suitable for project teams working in an **Agile** project management approach. 

#### Purposes

- Give a quick visual understanding of work details and provide critical task information.
- Facilitate handoffs between stakeholders, such as between development and testing resources or between team members who work on related tasks.
- Help with capturing metrics and improving workflows.

#### Using a Kanban board

Before creating a board, it is best practice to **gather the necessary information and lay out key elements**, such as tasks, status, dates, and durations.

Example

![image-20241123140607612](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/image-20241123140607612.png)

- Each colored rectangle is associated with a task. The tasks are represented horizontally across the effort timeline. 
- Each column represents where the task is in relation to its completion. 
  - So as a task is started, it will move from *to do*, to *in progress*. 
  - When the project is almost ready to be released or complete, it will move to *testing*. 
  - When it is tested and approved, it will move to *done*.

#### Creating cards

When using physical cards, teams often use both sides. Here is what both sides of the card should include:

**Front**

- **Title and unique identifier:** Make sure you have a quick reference for tasks and ID numbers.
- **Description of work:** Briefly describe the task to be accomplished. Remember that this is intended to be captured on something no larger than an index card.
- **Estimation of effort:** Estimate the amount of work it will take to complete the task. For example, you can write “small,” “medium,” or “large” to indicate the level of effort you think that task will involve. 
- **Who is assigned to the task:** Indicate who is responsible for completing the task; ideally, one person per card.

**Back** 

- **Start date:** Include the start date of the task for use in metrics, tracking, and ensuring that your time estimate is accurate.
- **Blocked days:** Indicate which days your task may be halted. A task can become blocked if it can’t continue to be worked on. For example, if you were supposed to receive a deliverable and it hasn’t been delivered yet, then your day may be blocked for this particular task.
- **Finish date:** As with any plan, it is important to track when the task is supposed to be finished. This allows you to ensure that your project is still on track to reach the end goal.