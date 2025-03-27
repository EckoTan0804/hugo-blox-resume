---
# ===== Title, summary, and position in the left sidebar =====
linktitle: Replication Method  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 405 # Position in the left sidebar
# ============================================================

# ========== Basic metadata ==========
title: Replication Method of ETFs
date: 2025-03-07
draft: false
authors:
  - admin
tags:
  - ETF
  - ETF-selection
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
disable_comment: false
commentable: true  # Allow visitors to comment? Supported by the Page, Post, and Book content types.
editable: false  # Allow visitors to edit the page? Supported by the Page, Post, and Book content types.

# Optional header image (relative to `assets/media/` folder).
header:
    caption: 
    image:  
---

{{% callout note %}}
## 💡Take Away
To replicate an index, there are 3 different methods:

- **Physical replication** buys the index in the same weighting. Such replication is called fully replicating ETFs.
- With **sampling**, the ETF provider only buys a selection of the securities. They exclude those with a very small share in the index.
- **Swap** ETFs providers enter into a swap agreement with a financial institution. Swap ETFs are mainly used in niche ETFs.

{{% /callout %}}

ETFs aim to replicate the performance of an index as accurately as possible. There are different ways to achieve this goal. The method by which an ETF bundles and represents price movements is called the **replication method**. You can read about the replication method of an ETF in its factsheet.

An index can be replicated by an ETF in three different ways. The deciding factors are **how accessible the securities are and how expensive they are**. If a stock is on a market that is difficult to access from abroad, ETF providers need to be creative. ETF providers choose between 

- physical replication
- optimized sampling
- synthetic replication

## Physical Replication

Physically replicating ETFs track the index by **purchasing all the securities included in it**. Because these ETFs mirror the index exactly, they are referred to as **fully replicating** or **full-replication ETFs**.

*Example: If an ETF aims to physically replicate the DAX, it buys all 40 stocks included in the index. The weighting of each stock in the index determines its proportion within the ETF. If a company drops out of the DAX and another one is added, the ETF sells the outgoing stock and buys shares of the newly included company. The same applies when there is a rebalancing within the DAX.*

Each transaction incurs fees, which affect the Total Expense Ratio (TER) of the fund. These fees are deducted from the fund’s assets and impact its performance. 

- In niche markets and for hard-to-replicate securities, costs are often higher than for Dow Jones stocks or those from similarly established indices. 
- The DAX, with its 40 components, is relatively manageable, keeping costs low. 
- However, global ETFs containing hundreds or even thousands of securities face higher costs, making physical replication more suitable for smaller indices.

## Sampling

Sampling is an **advanced form of physical replication**.

- The ETF still purchases securities physically, but only a representative subset. With this "sample," the provider makes a <u>preselection</u>, which is why this approach is also called **optimized sampling** or **optimized physical replication**.
- Instead of including all the securities in the index, the ETF invests only in the most significant ones. 
  - A security is considered important if it has a high weighting in the index. 
  - Illiquid securities or those with a very small share of the index are disregarded.

- *Example: in the MSCI Emerging Markets Index, many stocks have a weighting of just 0.01%. This index includes stocks from countries with less liquid and accessible markets compared to Europe or the US. An ETF using the sampling method ignores these minor components since they have minimal impact on overall index performance. This approach helps ETF providers reduce transaction costs.*

## Synthetic Replication

Some markets are difficult to access due to low liquidity or regulatory restrictions. This includes asset classes such as commodities or money market interest rates. However, investors still want to gain exposure to these indices through an ETF. In such cases, an ETF can replicate an index using a **swap agreement**.

- The ETF provider enters into a swap deal with a counterparty, usually a major financial institution. The counterparty holds the desired assets, while the ETF itself maintains an independent collateral portfolio.
- The two parties sign a contract: the ETF provider delivers the return of the collateral portfolio to the counterparty and, in exchange, receives the return of the target index.

{{< spoiler text="Example" >}}
Let’s say you invest in a synthetic MSCI China ETF, but the ETF does not directly purchase Chinese stocks. Instead, the process works as follows:

This ETF might hold European corporate bonds as its collateral portfolio.

The ETF provider signs a swap agreement with a bank (e.g., Deutsche Bank), which agrees to provide the returns of the MSCI China Index. In return, the ETF provider gives the bank the returns generated by the collateral portfolio (the European bonds).

As a result, the price of your ETF moves in line with the MSCI China Index, even though the ETF itself does not own any Chinese stocks.

{{< /spoiler >}}

The value difference between the two portfolios must not exceed 10% under **EU regulations**. 

- If the **swap portfolio** is at **€100** and the **collateral portfolio** is at **€110**, the swap must be executed at this point at the latest. The same applies if the swap portfolio is at **€100** and the collateral portfolio drops to **€90**.
- Most ETF providers execute swaps **well before** reaching the 10% threshold.
- With swap-based ETFs, there is always counterparty risk, meaning the possibility that the financial institution involved in the swap could go bankrupt. However, both parties provide collateral, which is usually more valuable than the swap transaction itself, reducing the overall risk.

## Comparison of Replication Methods

| **Replication Method**            | **Description**                                              | **Typical Distribution Type** | **Application Examples**                                     |
| --------------------------------- | ------------------------------------------------------------ | ----------------------------- | ------------------------------------------------------------ |
| **Physical Full Replication**     | The index is replicated with **all** its constituent securities in the same proportions. | Distributing or accumulating  | Small indices with a high proportion of blue-chip stocks: DAX, Euro Stoxx 50, Dow Jones 30 |
| **Optimized Sampling (Physical)** | The ETF replicates the index with a selection of the **most important** index securities. | Distributing or accumulating  | Larger number of blue-chip stocks: MSCI World, MSCI Emerging Markets |
| **Synthetic (Swap ETFs)**         | The index is replicated through **swap agreements**.         | Primarily accumulating        | Niche markets and specialty ETFs: FTSE Vietnam, MSCI Emerging Markets, Leverage or Short ETFs |

## Which replication method is the best?

- The replication methods have little impact on ETF performance. The replication method also doesn’t make a difference in terms of taxes. 

- Physically replicating ETFs are a good choice because they replicate indices so accurately.
- If you want to invest in niche markets, you often can’t avoid swap ETFs.

{{% callout  warning %}}
**Good to know**: ETFs and the associated underlying portfolios are considered special assets in Germany. However, the outstanding swap difference is not. If the counterparty goes bankrupt, the ETF could, in the worst case, lose the outstanding swap return. Although the likelihood is low, you should check what collateral the respective ETF has deposited.
{{% /callout %}}

## Reference

- [ETF Replikationsmethoden im Vergleich](https://www.finanzfluss.de/etf-handbuch/replikationsmethoden/)