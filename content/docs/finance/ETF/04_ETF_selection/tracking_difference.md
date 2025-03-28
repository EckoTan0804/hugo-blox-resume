---
# ===== Title, summary, and position in the left sidebar =====
linktitle: Tracking Difference  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 406 # Position in the left sidebar
# ============================================================

# ========== Basic metadata ==========
title: Tracking Difference & Tracking Difference
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
- The Tracking Difference refers to the difference in performance between an ETF and its benchmark index *over a given period*. It is influenced by factors such as transaction costs from rebalancing, taxes, or cash holdings. 
- You can use the Tracking Difference to assess the quality of an ETF's index replication.

- The Tracking Difference usually needs to be calculated by yourself. The necessary performance data can be found in the factsheet.

- The Tracking Error refers to the annual deviation of the daily returns of the ETF and the benchmark index. It indicates how much the Tracking Difference fluctuates.


{{% /callout %}}


An important quality feature for ETFs is the so-called **Tracking Difference**, the performance difference between the ETF and its benchmark index. In combination with the **Total Expense Ratio (TER)**, you can determine if poor index replication is causing you to miss out on potential returns.

## Tracking Difference in ETFs

### What is tracking difference?

ETFs aim to replicate an index as accurately as possible. However, this is never perfectly achievable for several reasons. Therefore, the value progression of the ETF will always differ slightly from that of the index. 🤪

The Tracking Difference shows the **difference between the performance of the ETF and that of the benchmark index**. The causes for this can include 

- fees
- the handling of foreign withholding taxes
- income from securities lending

Sometimes, ETFs even outperform the benchmark index.

### Where does the Tracking Difference come from?

ETF providers generally try to keep the tracking difference as low as possible, as investors compare it with other ETFs and choose the one with the better value. The following factors can influence the tracking difference:

{{< spoiler text="TER (Total Expense Ratio)" >}}
The total expense ratio reduces the returns of an ETF. The lower it is, the smaller the impact on the fund's performance.
{{< /spoiler >}}

{{< spoiler text="(Source) Taxes" >}}
Differences between the calculated and actual taxes can lead to discrepancies in the ETF.
{{< /spoiler >}}

{{< spoiler text="Replication" >}}
Depending on how an ETF replicates an index, different costs may arise. With physical replication, many securities may need to be bought, leading to high transaction costs.
{{< /spoiler >}}

{{< spoiler text="Cash Drag" >}}
Cash holdings from dividend payouts cause delays, leading to deviations.
{{< /spoiler >}}

{{< spoiler text="Timing" >}}
Rebalancing the ETF due to changes in the benchmark index can contribute to the difference.
{{< /spoiler >}}

{{< spoiler text="Securities Lending" >}}
By lending securities, ETF providers can generate additional income, allowing them to (temporarily) outperform the benchmark index.
{{< /spoiler >}}

### Tracking Difference and TER

To illustrate the costs of an ETF, 

the **Total Expense Ratio (TER)** is usually the first metric considered. 

- It indicates how much an ETF costs per year.

- However, the TER alone is only partially meaningful when assessing opportunity costs—missed profit opportunities.

The **tracking difference**, which is also a useful metric for evaluating an ETF's quality, reflects this "missed return" by comparing the ETF’s performance to that of the index

- If the tracking difference in the past was *significantly higher* than the TER, opportunity costs were incurred, meaning potential gains were lost.
- However, these figures are based on past performance and cannot be directly projected into the future. 

When determining actual costs, the TER still remains the most reliable metric. You can compare the tracking difference with the TER to get a clearer picture.

### Finding the Tracking Difference

- Find in the factsheet

- Browse through ETF platforms

  *⚠️ These figures should be taken with caution, as they are based on independent calculations rather than official data from the fund provider. As a result, the calculations may be inaccurate.*

### Calculating the Tracking Difference

Here, we take the **iShares Core MSCI World ETF** with ISIN **IE00B4L5Y983** as an example. The **TER** (Total Expense Ratio) for this ETF is **0.2%**.

Formula for calculating the tracking difference:
$$
\text{Tracking Difference (TD)} = \text{Fund return} - \text{Index return}
$$

- $\text{TD} > 0$: The ETF has outperformed the index.

- $\text{TD} < 0$: The ETF has underformed the index.

![ETF Tracking Difference Beispiel](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/Bildschirmfoto-2020-11-03-um-15.56.04.jpeg)

We compute the tracking difference for the past year:
$$
\text{TD} = 10.42\% - 10.41\% = 0.01\%
$$
$\text{TD} = 0.1\% > 0$ indicates that the ETF has **outperformed** its benchmark index. In this case, the ETF has performed better than expected, making it more cost-effective for investors.

## Tracking Error

The **Tracking Error**, also known as the **replication error**, is a related metric. It is often mistakenly used interchangeably with the **Tracking Difference**.

- The **Tracking Error measures how much the Tracking Difference fluctuates over time**.
- A **lower Tracking Error** means the ETF replicates its benchmark index more accurately.
- A **higher Tracking Error** indicates that the ETF tracks the index less reliably, sometimes performing better and sometimes worse than the benchmark index.

### Tracking difference vs. tracking error

- The **Tracking Difference** refers to the *actual* performance difference between an ETF and its benchmark index over a given period.

- The **Tracking Error**, on the other hand, measures the variability of these performance differences over time, indicating how the Tracking Difference has fluctuated.

## Reference

- [Tracking Error & Tracking Differenz erklärt](https://www.finanzfluss.de/etf-handbuch/tracking-error-tracking-difference/)