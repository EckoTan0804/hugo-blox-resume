---
# ===== Title, summary, and position in the left sidebar =====
linktitle: Regional Weighting  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 303 # Position in the left sidebar
# ============================================================

# ========== Basic metadata ==========
title: Regional Weighting in the World Portfolio
date: 2025-03-07
draft: false
authors:
  - admin
tags:
  - ETF
  - ETF-strategy
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

{{% callout  note %}}

## 💡Take Away

- The method used to weight countries and companies in an index can lead to differences in performance. Most (global) indices are weighted by market capitalization, meaning they are based on the value of publicly traded companies.

- As a result, there may be discrepancies compared to a country’s actual economic output, which is reflected in its Gross Domestic Product (GDP).

- MSCI indices like the MSCI World or MSCI ACWI tend to have an overweight allocation to U.S. stocks compared to the U.S. share of global GDP.

- To balance out such overweight allocations, regionally focused indices can be used, such as the STOXX Europe 600, which specializes in European companies with small, mid, and large market capitalizations.

{{% /callout %}}

## Indices Are Usually Weighted by Market Capitalization

Most global indices, such as the MSCI ACWI, track the global economy based on **market capitalization**. This means they automatically weight companies according to their value on the stock exchange. The formula for market capitalization is:
$$
\text{market capitalization} = \text{\#outstanding shares} \times \text{stock price}
$$

- For a country’s economy, market capitalization represents **the total value of all publicly listed companies**.

- The weighting of different countries in global indices like the MSCI World is determined by the total market capitalization of the included companies.

- Advantage: **automatic rebalancing**

  - Countries and companies are classified primarily based on their market capitalization

    *E.g., if a country transitions from an emerging market to a developed economy, it can be automatically included in the corresponding index for developed markets (such as the MSCI World in the MSCI index family).*

  - Other factors also play a role, such as the proportion of freely tradable shares.

## Is the USA Overrepresented?

The aforementioned weighting can be seen as problematic because <span style="color: #d65d48;">a large portion of the global economy operates outside the stock markets—in privately held companies</span>.

In the USA, nearly 150% of USA's economy is market capitalized. This is because many multinational corporations, like Facebook, are headquartered in the U.S., earning revenue globally but being listed on U.S. stock exchanges. This means that **the value of U.S. companies exceeds the value of the U.S. economy itself**.



{{% callout  note %}}
####  Market Capitalization to GDP Ratio

The **Market Capitalization to GDP Ratio** compares the total market value of a country’s publicly traded companies (stock market capitalization) to its **Gross Domestic Product (GP)**

![截屏2025-03-13 22.21.09](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/%E6%88%AA%E5%B1%8F2025-03-13%2022.21.09.png)

It is often used to assess whether a country’s stock market is overvalued or undervalued relative to its economy:

- **Ratio > 100%** → The stock market is **larger** than the country’s economy, indicating that publicly traded companies have a high valuation. 
  - This is common in countries like the **U.S. (around 150%)**, where many global corporations are listed domestically.
- **Ratio < 100%** → The stock market is **smaller** than the economy, meaning a significant portion of economic activity comes from **private or non-listed companies**.
  - For example, in **Germany (~50%)**, many large companies (e.g., Bosch, Aldi) are not publicly traded.
- **Ratio around 75-100%** → The stock market and the economy are roughly in balance.

{{% /callout %}}

This situation contributes to the <span style="color: #d65d48;">**high weighting of the U.S. in market-capitalization-based indices**</span>.

- While the U.S. makes up **55% of the MSCI ACWI**, in EU countries, only a little more than half of GDP is market capitalized, meaning the U.S. overweighting comes at the expense of regions like Europe.

Another factor affecting the balance is **company size selection based on market capitalization**. 

- The MSCI World index only includes large- and mid-cap companies, covering 85% of a country’s market capitalization. 
- However, small-cap stocks, which represent 15% of economic activity, are excluded from the index.

## Weighting by GDP as an Alternative

Those who find the weighting of world indices (such as MSCI ACWI) problematic can counteract this by **orienting towards GDP-based weighting**. 

- Advantage: Minimize the concentration risk that arises from the tendency to overweight the United States, ensuring broader regional diversification

- Allow for a more accurate reflection of the global economy
- Open up new opportunities for returns through a stronger emphasis on emerging markets, which are underrepresented in terms of market capitalization.
- Challenge: the need for rebalancing, as the relative shares of different GDPs change dynamically over time. 

### Using Regional Indices for Balance

Easy and stress-free ways to counteract imblances and align more with GDP-based weighting

-  **Overweight emerging markets by increasing the proportion of emerging markets in a mixed index portfolio made up of the MSCI World and MSCI Emerging Markets**.

-  Add an index like the STOXX Europe 600, which includes large, mid, and small-cap companies from Europe. ( Europe is much more strongly represented in a GDP-based weighting compared to a market capitalization-based one. )

## Strengthening with Small Caps

Including indices that focus on small-cap companies can be a valuable addition, as small (and mid) caps are underweighted in the MSCI World indices.

Example:

- **MSCI Europe Small Cap index** specifically targets small caps from the European region
- **STOXX Europe 200 Small**

## Reference

- [Regionale Gewichtung im Weltportfolio](https://www.finanzfluss.de/etf-handbuch/weltportfolio-gewichtung/)