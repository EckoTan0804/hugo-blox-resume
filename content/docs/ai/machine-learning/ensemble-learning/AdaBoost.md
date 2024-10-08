---
# Title, summary, and position in the list
# linktitle: ""
summary: ""
weight: 670

# Basic metadata
title: "AdaBoost"
date: 2020-11-07
draft: false
 
authors: ["admin"]
tags: ["Machine Learning", "Ensemble Learning"]
categories: ["Machine Learning"]
toc: true # Show table of contents?

# Advanced metadata
profile: false  # Show author profile?

reading_time: true # Show estimated reading time?
share: false  # Show social sharing links?
featured: true

comments: true  # Show comments?
disable_comment: false
commentable: true  # Allow visitors to comment?  

editable: false  # Allow visitors to edit the page?  

# Optional header image (relative to `assets/media/` folder).
header:
  caption: ""
  image: ""
---

**Ada**ptive **Boost**ing:

Correct its predecessor by paying a bit more attention to the training instance that the predecessor underfitted. This results in new predictors focusing more and more on the hard cases.

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/AdaBoost.png" alt="AdaBoost" style="zoom:80%;" />



## Pseudocode

1. Assign observation $i$ the weight for $d\_{1,i}=\frac{1}{n}$ (equal weights)

2. For $t=1:T$

    1. Train weak learning alg orithm using data weighted by $d\_{ti}$. This produces weak classifier $h\_t$

    2. Choose coefficient $\alpha\_t$ (tells us how good is the classifier is at that round)

    $$
    \begin{aligned}
      \operatorname{Error}\_{t} &= \displaystyle\sum\_{i;  h\_{t}\left(x\_{i}\right) \neq y\_{i}} d\_{t} \quad \text{(sum of weights of misclassified points)} \\\\
      \alpha\_t &= \frac{1}{2} (\frac{1 - \operatorname{Error}\_{t}}{\operatorname{Error}\_{t}})
    \end{aligned}
    $$

    

    3. Update weights
       $$
       d\_{t+1, i}=\frac{d\_{t, i} \cdot \exp (-\alpha\_{t} y\_{i} h\_{t}\left(x\_{i}\right))}{Z\_{t}}
       $$

       - $Z\_t = \displaystyle \sum\_{i=1}^{n} d\_{t,i} $:  **normalization factor**

         > - If prediction $i$ is correct $\rightarrow y\_i h\_t(x\_i) = 1 \rightarrow $ Weight of observation $i$ will be decreased by $\exp(-\alpha\_t)$
         > - If prediction $i$ is incorrect $ \rightarrow y\_i h\_t(x\_i) = -1 \rightarrow $ Weight of observation $i$ will be increased by $\exp(\alpha\_t)$

3. Output the final classifier 

    $
        H(x)=\operatorname{sign}\left(\sum\_{t=1}^{T} \alpha\_{t} h\_{t}\left(x\_{i}\right)\right)
    $
    
    

## Example

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/AdaBoost_Eg-00.png" alt="AdaBoost_Eg-00" style="zoom:50%;" />

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/AdaBoost_Eg-01.png" alt="AdaBoost_Eg-01" style="zoom:50%;" />

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/AdaBoost_Eg-02.png" alt="AdaBoost_Eg-02" style="zoom:50%;" />

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/AdaBoost_Eg-03.png" alt="AdaBoost_Eg-03" style="zoom:50%;" />

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/AdaBoost_Eg-04.png" alt="AdaBoost_Eg-04" style="zoom:50%;" />

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/AdaBoost_Eg-05.png" alt="AdaBoost_Eg-05" style="zoom:50%;" />

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/AdaBoost_Eg-06.png" alt="AdaBoost_Eg-06" style="zoom:50%;" />

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/AdaBoost_Eg-07.png" alt="AdaBoost_Eg-07" style="zoom:50%;" />

## Tutorial

{{< youtube -DUxtdeCiB4 >}}

