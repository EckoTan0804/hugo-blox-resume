---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 310
# ============================================================

# ========== Basic metadata ==========
title: Statische und Dynamische Systeme
date: 2022-06-16
draft: false
# page type
authors:
  - admin
tags:
  - SI
  - Lecture Notes
  - wertkontinuierliche lineare Systeme
  - statische Systeme
categories:
  - Lecture
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

## Linearität

Gegeben ein System $S$



![wertekontinuierliche_lineare_systeme.drawio](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/wertekontinuierliche_lineare_systeme.drawio.png)

{{< math >}}
$$
\underline{x}_k \rightarrow \underline{y}_k \qquad k \in \mathbb{N}_0
$$
{{< /math >}} 

Zwei Bedingungen der Linearität

- Skalierung

  {{< math >}}
  $$
  \underline{x}_k \rightarrow \underline{y}_k \Rightarrow A \cdot \underline{x}_k \rightarrow A \cdot \underline{y}_k
  $$
  {{< /math >}} 

- Superposition

  {{< math >}}
  $$
  \begin{aligned}
  \underline{x}_k^1 \rightarrow \underline{y}_k^1, \quad  \underline{x}_k^2 \rightarrow \underline{y}_k^2 \\
  \Rightarrow \underline{x}_k^1 + \underline{x}_k^2 \rightarrow \underline{y}_k^1 + \underline{y}_k^2
  \end{aligned}
  $$
  

  {{< /math >}} 



## Statische Systeme

- Ein-/Ausgänge: Zufallsvektoren $\underline{u}_k$ und $\underline{y}_k$ ($k \in \mathbb{N}_0$ ist der Zeitschritt)

  <img src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/wertekontinuierliche_lineare_systeme-statische_systeme.drawio.png" alt="wertekontinuierliche_lineare_systeme-statische_systeme.drawio" style="zoom:80%;" />

  - $\underline{u}_k \in \mathbb{R}^P$ und $\underline{y}_k \in \mathbb{R}^M$ sind wertekontinuierlich

- Abbildung von $\underline{u}_k$ und $\underline{y}_k$ durch lineare Abbildung

  {{< math >}}
  $$
  \underline{y}_k = \mathbf{A}_k \cdot \underline{u}_k
  $$
  

  {{< /math >}} 

  wobei $\mathbf{A}_k \in \mathbb{R}^{M \times P}$

- Beschreibung der Unsicherheiten in $\underline{u}_k$ und $\underline{y}_k$ durch die ersten beiden Momente
  - Erwartungswert
    - {{< math >}}$\underline{\hat{u}}_k := E\{\underline{u}_k\}${{< /math >}} 
    - {{< math >}}$\underline{\hat{y}}_k := E\{\underline{y}_k\}${{< /math >}} 
  - Kovarianz Matrix
    - {{< math >}}$C_k^u := \operatorname{Cov}\{\underline{u}_k\}${{< /math >}} 
    - {{< math >}}$C_k^y := \operatorname{Cov}\{\underline{y}_k\}${{< /math >}} 

- Beschreibung der Kenngröße $\underline{\hat{y}}_k, C_k^y$  für gegebene $\underline{\hat{u}}_k, C_k^u$

  {{< math >}}
  $$
  \begin{aligned}
  \hat{y}_{k} &=E\left\{\underline{y}_{k}\right\} \\
  &=E\left\{A_{k} \cdot x_{k}\right\} \\
  &=A_{k} \cdot E\left\{x_{k}\right\} \\
  &=A_{k} \cdot \hat{\underline{u}}_{k} \\\\
  C_{k}^{y} &=\operatorname{Cov}\left\{\underline{y}_{k}\right\} \\
  &=E\left\{\left(y_{k}-\hat{y}_{k}\right)\left(\underline{y}_{k}-\underline{y}_{k}\right)^{\top}\right\} \\
  &=E\left\{A_{k}\left(\underline{u}_{k}-\underline{\hat{u}}_{k}\right)\left(\underline{u}_{k}-\underline{\hat{u}}_{k}\right)^{\top} A_{k}^{\top}\right\} \\
  &=A_{k} E\left\{\left(\underline{u}_{k}-\hat{u}_{k}\right)\left(\underline{u}_{k}-\underline{\hat{u}}_{k}\right)^{\top}\right\} A_{k}^{\top} \\
  &=A_{k} \cdot C_{k}^{u} \cdot A_{k}^{\top}
  \end{aligned}
  $$
  {{< /math >}} 



## Dynamische Systeme

- Anregung hängt nicht nur vom aktuellen Eingang $\underline{u}_k$ ab (analog wie wertdiskrete Systeme), sondern auch vom aktuellen Zustand
- Zustände werden in internen Speichern gespeichert
- Gesamtsystem ("**Gauß-Markov-Modell**") besteht aus
  - Systemabbildung
  - Messabbildung

{{< figure src="https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/wertekontinuierliche_lineare_systeme-Gauß-Markov-Modell.drawio.png" caption="Graphische Darstellung von dynamischer Systeme" numbered="true" >}}

### Systemabbildung

{{% callout note %}}
**Definition**

Ein lineares Zustandraummodell wird als <mark>**zeitinvariant** (Engl. Linear Time Invariant (LTI))</mark> bezeichnet, falls die Systemmatrizen nicht von Zeitindex $k$ abhängen, also 

{{< math >}}
$$
\mathbf{A}\_{k} = \mathbf{A}, \quad \mathbf{B}\_{k} = \mathbf{B}
$$
{{< /math >}} 
{{% /callout %}}

Zeitliche Entwicklung (linear)

{{< math >}}
$$
\underline{x}_{k+1}=\mathbf{A}_{k} \cdot \underline{x}_{k}+\mathbf{B}_{k} \cdot \underbrace{(\underline{\tilde{u}}_{k}+\underline{w}_{k})}_{=\underline{u}_{k}}
$$
{{< /math >}} 

- Zustand: Zufallsvektor $\underline{x}_k \in \mathbb{R}^N, k\in \mathbb{N}_0$

- Markov-Modell (erster Ordnung): {{< math >}}$\underline{x}_{k+1}${{< /math >}} hängt NUR von {{< math >}}$\underline{x}_{k}${{< /math >}} und $\underline{u}_{k}$ ab



- Häufig wird $\underline{u}_{k}$ mit mittelwertfreien Rauschen argestellt 

  {{< math >}}
  $$
  \underline{u}_{k}=\underline{\tilde{u}}_{k}+\underline{w}_{k}
  $$
  {{< /math >}} 

  - $\underline{\tilde{u}}_{k}$ bekannt
  - Zufallsvektor $\underline{w}_{k}$ mit {{< math >}}$E\{\underline{w}_k\} = \underline{0}, \operatorname{Cov}\{\underline{w}_k\} = c_k^w${{< /math >}} 

### Messabbildung

- Zustand $\underline{x}_k$ typischerweise NICHT verfügbar
- Ausgang $\underline{y}_{k}$ hängt von $\underline{x}_k$ und evtl. von $\underline{u}_k$

- Lineare Messabbildung

  {{< math >}}
  $$
  \underline{y}_{k}=\mathbf{H}_{k} \cdot \underline{x}_{k}+\underline{v}_{k}
  $$
  {{< /math >}}

  - $\underline{v}_{k}$: additives mittelwertfreien Messrauschen ({{< math >}}$E\{\underline{w}_k\} = \underline{0}, \operatorname{Cov}\{\underline{w}_k\} = c_k^w${{< /math >}} )
  - Messabbildung ist zeitinvaraint, falls $\mathbf{H}_{k} = \mathbf{H}$

## Einschub: Systemeigenschaften zeitdiskreter Systeme

Für Definitionen von Systemeigenschaften zeitdiskreter Systeme siehe **Signale und Systeme**[^1] Seite 312 - 314.

### Linearität

Ein zeitdiskretes System {{< math >}}$\mathcal{S}${{< /math >}} heißt **linear**, wenn für zwei beliebige Eingangssignale {{< math >}}$y_{\mathrm{e} 1, n}${{< /math >}} und {{< math >}}$y_{\mathrm{e} 2, n}${{< /math >}} und zwei beliebige Konstanten {{< math >}}$c_1, c_2 \in \mathbb{R}${{< /math >}} oder {{< math >}}$\mathbb{C}${{< /math >}} 

{{< math >}}
$$
\mathcal{S}\left\{c_{1} y_{\mathrm{e} 1, n}+c_{2} y_{\mathrm{e} 2, n}\right\}=c_{1} \mathcal{S}\left\{y_{\mathrm{e} 1, n}\right\}+c_{2} \mathcal{S}\left\{y_{\mathrm{e} 2, n}\right\}
$$
{{< /math >}} 

gilt.

- Erweiterung auf auf $N$ Eingangssignale

  {{< math >}}
  $$
  \mathcal{S}\left\{\sum_{i=1}^{N} c_{i} y_{\mathrm{e} i, n}\right\}=\sum_{i=1}^{N} c_{i} \mathcal{S}\left\{y_{\mathrm{e} i, n}\right\}
  $$
  {{< /math >}} 

- Erweiterung auf unendlich viele Eingangssignale

  {{< math >}}
  $$
  \mathcal{S}\left\{\sum_{i=-\infty}^{\infty} c_{i} y_{\mathrm{e} i, n}\right\}=\sum_{i=-\infty}^{\infty} c_{i} \mathcal{S}\left\{y_{\mathrm{e} i, n}\right\}
  $$
  {{< /math >}} 

### Zeitinvarianz

Ein zeitdiskretes System {{< math >}}$\mathcal{S}${{< /math >}} heißt **zeitinvariant**, wenn es auf ein zeitlich verschobenes Eingangssignal {{< math >}}$y_{\mathrm{e}, n-n_{0}}${{< /math >}} mit dem entsprechend zeitlichverschobenen Ausgangssignal {{< math >}}$y_{\mathrm{a}, n-n_{0}}${{< /math >}} antwortet

{{< math >}}
$$
y_{\mathrm{a}, n}=\mathcal{S}\left\{y_{\mathrm{e}, n}\right\} \quad \Longrightarrow \quad y_{\mathrm{a}, n-n_{0}}=\mathcal{S}\left\{y_{\mathrm{e}, n-n_{0}}\right\}.
$$
{{< /math >}} 

Sonst heißen die Systeme **zeitvariant**.

### Kausalität

Ein zeitdiskretes System S heißt **kausal**, wenn die Antwort NUR von *gegenwärtigen* oder *vergangenen*, nicht jedoch von zukünftigen Werten des Eingangssignals abhängt.

Dies bedeutet, dass für ein System {{< math >}}$\mathcal{S}${{< /math >}} aus

{{< math >}}
$$
y_{\mathrm{e} 1, n}=y_{\mathrm{e} 2, n} \quad \text { für } n \leq n_{1}
$$
{{< /math >}} 

und 

{{< math >}}
$$
y_{\mathrm{a} 1, n}=\mathcal{S}\left\{y_{\mathrm{e} 1, n}\right\}, \quad y_{\mathrm{a} 2, n}=\mathcal{S}\left\{y_{\mathrm{e} 2, n}\right\}
$$
{{< /math >}} 

stets

{{< math >}}
$$
y_{\mathrm{a} 1, n}=y_{\mathrm{a} 2, n} \quad \text { für } n \leq n_{1}
$$
{{< /math >}} 

folgt.

## Beispiel

(Übungsblatt 5, Aufgabe 1)

Ein zeidiskretes wertekontinuierliches System $S$ wird durch die Differenzengleichung

{{< math >}}
$$
y_{k}-2^{k} \cdot y_{k+1}+3 \cdot y_{k+2}^{2}=4 \cdot u_{k}-2 \cdot u_{k+1}
$$
{{< /math >}} 

beschrieben.

1. Ist das System $S$ linear?

   Das System $S$ ist aufgrund des Terms {{< math >}}$y_{k+2}^{2}${{< /math >}} NICHT linear.

2. Ist das System $S$ zeitinvariant?

   Das System $S$ ist wegen des zeitabhängigen Koeffizienten $2^k$ von $y_{k+1}$ zeitvariant.

3. Ist das System $S$ kausal?

   Das System $S$ ist kausal, da $y_{k+2}$ nur von vergangenen Eingangswerten abhängt.







[^1]: F. P. León and H. Jäkel. Signale und Systeme. De Gruyter Oldenbourg, Berlin, Boston, 02 Sep. 2019. ISBN 978-3-11-062632-2. doi: https://doi.org/10.1515/9783110626322. URL https://www.degruyter.com/view/title/543041.

