---
# Title, summary, and position in the list
# linktitle: ""
summary: ""
weight: 130

# Basic metadata
title: "Evaluation"
date: 2020-08-17
draft: false
 
authors: ["admin"]
tags: ["Machine Learning", "ML Basics"]
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

## TL;DR

{{< figure src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/Confusion_Matrix_and_ROC.png" caption="Confusion matrix, ROC, and AUC" numbered="true" >}}




## Confuse matrix

A confusion matrix tells you what your ML algorithm did right and what it did wrong.

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg .tg-cly1{text-align:left;vertical-align:middle}
.tg .tg-tab6{color:#77b300;text-align:left;vertical-align:top}
.tg .tg-viqs{color:#fe0000;text-align:left;vertical-align:top}
.tg .tg-0lax{text-align:left;vertical-align:top}
.tg .tg-hjor{font-weight:bold;color:#9698ed;text-align:center;vertical-align:middle}
.tg .tg-dsu0{color:#9698ed;text-align:left;vertical-align:top}
.tg .tg-0sd6{font-weight:bold;color:#3399ff;text-align:center;vertical-align:top}
.tg .tg-12v1{color:#3399ff;text-align:left;vertical-align:top}
</style>
<table class="tg">
  <tr>
    <th class="tg-0lax" colspan="2" rowspan="2"></th>
    <th class="tg-hjor" colspan="2">Known Truth</th>
    <th class="tg-cly1" rowspan="2"></th>
  </tr>
  <tr>
    <td class="tg-dsu0">Positive</td>
    <td class="tg-dsu0">Negative</td>
  </tr>
  <tr>
    <td class="tg-0sd6" rowspan="2"><br>Prediction</td>
    <td class="tg-12v1">Positive</td>
    <td class="tg-tab6">True Positive (TP)</td>
    <td class="tg-viqs">False Positive (FP)</td>
    <td class="tg-0lax">Precision = TP / (TP+FP)</td>
  </tr>
  <tr>
    <td class="tg-12v1">Negative</td>
    <td class="tg-viqs">False Negative (FN)</td>
    <td class="tg-tab6">True Negative (TN)</td>
    <td class="tg-0lax" rowspan="2"></td>
  </tr>
  <tr>
    <td class="tg-0lax" colspan="2"></td>
    <td class="tg-0lax">TPR = Sensitivity = Recall <br> = TP / (TP + FN)</td>
    <td class="tg-0lax">Specificity = TN / (FP+TN) <br> FPR = FP / (FP + TN) = 1 - Specificity </td>
  </tr>
</table>



- Row: Prediction
- Column: Known truth 

Each cell:

- Positive/negative: refers to the prediction

- True/False: Whether this prediction matches to the truth

- The numbers along the diagonal (green) tell us how many times the samples were correctly classified
- The numbers not on the diagonal (red) are samples the algorithm messed up.



## Definition

### **Precision** 

How many selected items are relevant?
$$
\text{ Precision } = \frac{TP}{TP + FP}
=\frac{\\# \text{ relevant item retrieved }}{\\# \text{ of items retrieved }}
$$


### **Recall / True Positive Rate (TPR) / Sensitivity**

How many relevant items are selected?
$$
\text { Recall }  = \frac{TP}{TP + FN}
=\frac{\\# \text { relevant item retrieved }}{\\# \text { of relevant items in collection }}
$$

![img](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/350px-Precisionrecall.svg.png)


<details>
<summary>Example</summary>
<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2020-09-15%2011.51.38.png" alt="截屏2020-09-15 11.51.38" style="zoom: 33%;" />
<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2020-09-15%2011.51.43.png" alt="截屏2020-09-15 11.51.43" style="zoom:33%;" />

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2020-09-15%2011.51.46.png" alt="截屏2020-09-15 11.51.46" style="zoom:33%;" />

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2020-09-15%2011.51.49.png" alt="截屏2020-09-15 11.51.49" style="zoom:33%;" />

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2020-09-15%2011.51.52.png" alt="截屏2020-09-15 11.51.52" style="zoom:33%;" />
</details>

### **F-score / F-measure**

#### $F\_1$ score

The traditional F-measure or balanced F-score (**$F\_1$ score**) is the [harmonic mean](https://en.wikipedia.org/wiki/Harmonic_mean#Harmonic_mean_of_two_numbers) of precision and recall:
$$
F\_1=\frac{2 \cdot \text {precison} \cdot \text {recall}}{\text {precision}+\text {recall}} = \frac{2TP}{2TP + FP + FN}
$$

#### $F\_\beta$ score

$F\_\beta$ uses a positive real factor $\beta$, where $\beta$ is chosen such that **recall is considered $\beta$ times as important as precision**
$$
F\_{\beta}=\left(1+\beta^{2}\right) \cdot \frac{\text { precision } \cdot \text { recall }}{\left(\beta^{2} \cdot \text { precision }\right)+\text { recall }}
$$
Two commonly used values for $\beta$:

- $2$: weighs recall **higher** than precision
- $0.5$: weighs recall **lower** than precision

### Specificity

$$
\text{Specifity} = \frac{TN}{FP + TN}
$$

### False Positive Rate (FPR)

$$
\text{FPR} = \frac{FP}{FP + TN} \left(= 1- \frac{TN}{FP + TN} = 1- \text{Specifity}\right)
$$






## Relation between Sensitivity, Specificity, FPR and Threshold

Assuming that the distributions of the actual postive and negative classes looks like this:

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/evaluation-metrics-Page-1.png" alt="evaluation-metrics-Page-1" style="zoom:67%;" />

And we have already defined our threshold. What greater than the threshold will be predicted as positive, and smaller than the threshold will be predicted as negative. 

If we set a lower threshold, we'll get the following diagram:

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/evaluation-metrics-2.png" alt="evaluation-metrics-2" style="zoom:67%;" />

We can notice that FP ⬆️ , and FN ⬇️ .

Therefore, we have the relationship:

- Threshold ⬇️
  - FP ⬆️ , FN ⬇️ 
  - $\text{Sensitivity} (= TPR) = \frac{TP}{TP + FN}$ ⬆️ , $\text{Specificity} = \frac{TN}{TN + FP}$ ⬇️ 
  - $FPR (= 1 - \text{Specificity})$⬆️
- And vice versa



## AUC-ROC curve

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/evaluation-metrics-ROC-AUC.png" alt="evaluation-metrics-ROC-AUC" style="zoom:80%;" />

AUC (**Area Under The Curve**)-ROC (**Receiver Operating Characteristics**) curve

- Performance measurement for the classification problems at various threshold settings. 
  - ROC is a probability curve 
  - AUC represents the degree or measure of separability

- Tells how much the model is capable of distinguishing between classes.
- The higher the AUC, the better the model is at predicting 0s as 0s and 1s as 1s

### How is ROC plotted?

```python
for threshold in thresholds: # iterate over all thresholds
    TPR, FPR = classify(threshold) # calculate TPR and FPR based on threshold
    plot_point(FPR, TPR) # plot coordinate (FPR, TPR) in the diagram
    
connect_points() # connect all plotted points to get ROC curve
```

Example:

Suppose that the probability of a series of samples being classified into positive classes has been derived and we sort them descendingly:

<img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-02-24%2022.05.59.png" alt="截屏2021-02-24 22.05.59" style="zoom: 50%;" />

- Class: actual label of test sample 
- Score: probability of classifying test sample as positive

Next, we use the "Score" value as the threshold (from high to low). 

- When the probability that the test sample is a positive sample is greater than or equal to this threshold, we consider it a positive sample, otherwise it is a negative sample. 
  - For example, for the 4-th sample, its "Score" has value 0.6. So Sample 1, 2, 3, 4 will be considered as positive, because their "Score" values are $\geq$ 0.6. Other samples are classified as negative.

- By picking a different threshold each time, we can get a set of FPR and TPR, i.e., a point on the ROC curve. In this way, we get a total of 20 sets of FPR and TPR values. We plot them in the diagram:

  <img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/081955100088586.jpg" alt="img" style="zoom:80%;" />

### How to speculate about the performance of the model?

- An **excellent** model has **AUC near to the 1** which means it has a good measure of separability. 

  {{< figure src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-02-24%2021.02.34.png"  caption="Ideal situation: two curves don’t overlap at all means model has an ideal measure of separability. It is perfectly able to distinguish between positive class and negative class." numbered="true" >}}

- When $0.5 < \text{AUC} < 1$, there is a high chance that the classifier will be able to distinguish the positive class values from the negative class values. This is because the classifier is able to detect more numbers of True positives and True negatives than False negatives and False positives.

  {{< figure src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-02-24%2021.09.30.png"  caption="When AUC is 0.7, it means there is a 70% chance that the model will be able to distinguish between positive class and negative class." numbered="true" >}}

- When AUC is 0.5, it means the model has no class separation capacity whatsoever.![截屏2021-02-24 21.05.28](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-02-24%2021.05.28.png)

  

- A **poor** model has **AUC near to the 0** which means it has the worst measure of separability.

  {{< figure src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/截屏2021-02-24%2021.05.54.png"  caption="When AUC is approximately 0, the model is actually reciprocating the classes. It means the model is predicting a negative class as a positive class and vice versa." numbered="true" >}}

## 🎥 Video tutorials

### The confusion matrix

{{< youtube Kdsp6soqA7o >}}

### Sensitivity and specificity

{{< youtube vP06aMoz4v8 >}}

### ROC and AUC

{{< youtube 4jRBRDbJemM >}}



## Reference

- [Understanding AUC - ROC Curve](https://towardsdatascience.com/understanding-auc-roc-curve-68b2303cc9c5)
- [What is the F-score?](https://deepai.org/machine-learning-glossary-and-terms/f-score): very nice explanation with examples
- [机器学习之分类器性能指标之ROC曲线、AUC值](http://www.cnblogs.com/dlml/p/4403482.html)

