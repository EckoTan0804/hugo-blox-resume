---
# ===== Title, summary, and position in the left sidebar =====
linktitle: What Are ETFs  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 103 # Position in the left sidebar
# ============================================================

# ========== Basic metadata ==========
title: What Are ETFs
date: 2025-03-07
draft: false
authors:
  - admin
tags:
  - ETF
  - ETF-theory
categories:
  - finance-essentials
toc: true # Show table of contents
# ====================================

# ========== Advanced metadata =========
profile: false  # Show author profile?
reading_time: true # Show estimated reading time?
share: true  # Show social sharing links?
featured: true
comments: true  # Show comments?
disable_comment: falset
commentable: true  # Allow visitors to comment? Supported by the Page, Post, and Book content types.
editable: false  # Allow visitors to edit the page? Supported by the Page, Post, and Book content types.

# Optional header image (relative to `assets/media/` folder).
header:
    caption: 
    image:  
---

{{% callout  note %}}

## 💡 Take Away

- An **ETF** is a fund that tracks an index, such as the **DAX** or **MSCI World**.
- With ETFs, you can invest in **thousands of companies** with small amounts of money, allowing you to **diversify your portfolio**.
- ETFs are **significantly cheaper** than actively managed investment funds. Their annual expense ratios typically range between **0.05% and 0.7%** of the investment amount.
- ETFs are **ideal for long-term investing** in stock markets.
- ETFs can replicate an index using **physical replication**, **synthetic replication**, or a **combination of both methods**.


{{% /callout %}}

## What is an ETF?

ETFs, short for **Exchange-Traded Funds**, are **index funds** that are traded on stock exchanges. 

- "Exchange-traded" means that a stock exchange acts as a marketplace between you, the buyer, and the fund provider. Other index funds can be purchased directly from the provider. 

-  "Index fund" means that the fund **exactly replicates a stock index**. 

  - In simple terms, a fund is a type of **pooled investment vehicle** where capital (money) is collected and then invested.

  - Since an ETF closely replicates an index, its price moves in parallel with the index. 
    - If the index rises, the ETF generates returns.
    - The value of an ETF falls when the index declines.

## Who Issues ETFs?

ETFs are offered by **fund companies**. The issuer of an ETF is called an **emittent**. Some of the most well-known ETF issuers include **Amundi**, **Xtrackers**, **iShares**, and **Lyxor**.

1. The ETF fund company selects an index 
2. Then it collects money from investors. 
3. Using this money, the company purchases the securities included in the index. 
4. The fund company then issues a security (the ETF) that reflects the performance of the fund. 
5. An ETF security is essentially a certificate representing your share in the ETF. When you buy such a share, your money flows into the fund and is invested in the stocks included in the index. The stock purchases by the fund provider are fully automated.

![ETF_issuing_bg](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/ETF_issuing_bg.png)

## How an ETF Replicates an Index

1. A fund company examines which companies are included in the DAX and their respective weightings.
2. The fund company purchases these stocks.
3. When new companies are added to the index, the fund company expands the fund to include these stocks.Similarly, it sells stocks that are removed from the index.
4. If the fund's volume increases, the ETF provider can buy more shares.

All of this happens—unlike with actively managed funds—fully automatically and without the analysis of fund managers.

![ETF_replicate_index](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/ETF_replicate_index.png)

{{% callout  note %}}

#### **Market Capitalization**

The **market capitalization** of a company is calculated by multiplying the **total number of outstanding shares** by the **current market price** of one share. If a company has many high-priced shares in circulation, it has a **high market capitalization** and is considered valuable.

{{% /callout %}}

{{% callout  note %}}

#### **Free Float**

**Free float** refers to all shares that are **not held by major shareholders** or in large blocks. These shares are accessible to the general public. If a shareholder owns more than **5%** of a company's shares, those shares are no longer considered part of the free float. The higher the proportion of free float shares, the more **liquid** and **tradable** the stock becomes.

{{% /callout %}}

## Replication Methods

The way an ETF replicates its index is called the **replication method**. The goal is to **track the index as accurately as possible while keeping costs low**. The replication method affects the **costs**, **performance**, and **security** of an ETF. There are three main methods:

1. **Physical Replication**
2. **Sampling**
3. **Synthetic Replication**

### Physical Replication

In **physical replication**, the ETF purchases the **stocks included in the index**. If the portfolio exactly matches the index, it is called <u>**full replication**</u> or <u>**direct replication**</u>. This method is particularly useful when an index consists of a manageable number of stocks. For example, a **DAX ETF** can be easily replicated fully through physical replication.

![ETF_physical_replication](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/ETF_physical_replication.png)

#### Sampling

If an index consists of many positions, fully replicating it physically would require a large number of transactions. To remain cost-efficient, the ETF provider purchases only a **subset of the stocks**, specifically those that most influence the index's performance. This method is called **sampling** or **optimized physical replication**. It is a hybrid approach between physical and synthetic replication. Sampling is particularly suitable for an **MSCI World ETF**, which includes over **1,500 positions**.

### Synthetic Replication

In synthetic replication, the ETF provider replicates the index through a **swap agreement** with a financial institution (swap counterparty). The financial institution holds the positions of the ETF, while the ETF provider holds a different portfolio. The ETF provider receives the returns of the ETF positions, and the financial institution receives the returns of the collateral portfolio. Swap-based ETFs are commonly used for niche markets and commodities.

| **Method**    | **How It Works**                                             | **Advantages**                       | **Disadvantages**                    | **Best For**                             |
| :------------ | :----------------------------------------------------------- | :----------------------------------- | :----------------------------------- | :--------------------------------------- |
| **Physical**  | Buys the actual securities in the index.                     | Transparent, no counterparty risk.   | Higher costs for complex indices.    | Indices with few components (e.g., DAX). |
| **Synthetic** | Uses derivatives (e.g., swaps) to replicate index performance. | Cost-effective, precise replication. | Counterparty risk, less transparent. | Niche markets, commodities.              |
| **Hybrid**    | Combines physical and synthetic methods.                     | Balances cost and risk.              | Slightly more complex.               | Indices with mixed accessibility.        |

## Differences Between ETFs and Index Funds

ETFs are a type of **index fund**—with the unique feature of being **exchange-traded**. This means:

- ETFs can be **bought and sold continuously during trading hours** on the stock exchange.
- Traditional index funds are ***not* traded on an exchange**; instead, they are purchased directly from the fund provider.

![ETF_vs_index_fund](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/ETF_vs_index_fund.png)

Both passive index funds and ETFs share the same goal: **to replicate an index as accurately and cost-effectively as possible.** Both have **low fees** because they do not require a fund manager or an analysis team to track market developments.

Which is better?

- ETFs offer greater flexibility, as they can be traded at any time during market hours. However, John Bogle, the inventor of the index fund, warned that this flexibility can be tempting for private investors.
- ETFs are typically used for a **Buy-and-Hold strategy**, meaning you don’t need to trade frequently.

- There are **more ETFs** than index funds, giving you access to a wider range of markets, strategies, and asset classes.

## Differences Between ETFs and Active Funds

| **Aspect**           | **ETFs**                                                     | **Active Funds**                                             |
| :------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| **Management**       | **Passive**: Automatically replicates an index.              | **Active**: Fund managers make investment decisions.         |
| **Performance**      | Tracks the market; often outperforms active funds **long-term**. | Managers aim to beat the market but often underperform.      |
| **Costs**            | Low fees: **TER (Total Expense Ratio)** typically **0.05%–0.7%**. | High fees: Average **1.9%** in Europe (Morningstar).         |
| **Flexibility**      | Limited to index composition; no active stock picking.       | Managers can buy/sell assets based on market analysis.       |
| **Risk of Mistakes** | No human error; follows the index.                           | Managers can make wrong decisions.                           |
| **Transparency**     | Holdings are transparent and match the index.                | Holdings may change frequently, less transparent.            |
| **Best For**         | Long-term investors seeking low-cost, market-matching returns. | Investors willing to pay higher fees for potential outperformance. |

## Reference

- [Was sind ETFs? Exchange Traded Funds erklärt!](https://www.finanzfluss.de/etf-handbuch/etf/)