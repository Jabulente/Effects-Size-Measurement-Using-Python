

## 1. Standardized Mean Differences

| Metric        | Test(s)                                   | Formula (simplified)                                            | Interpretation (rough benchmarks)      | Typical Scenario                                    |
| ------------- | ----------------------------------------- | --------------------------------------------------------------- | -------------------------------------- | --------------------------------------------------- |
| **Cohen’s d** | Two‐sample t-test (independent or paired) | $\displaystyle d = \frac{\bar X_1 - \bar X_2}{s_\text{pooled}}$ | Small ≈ 0.2, Medium ≈ 0.5, Large ≈ 0.8 | Comparing treatment vs. control in a clinical trial |
| **Hedges’ g** | Two‐sample t-test                         | Like d, with small‐sample correction                            | Same benchmarks, less bias with n<20   | Educational intervention with small class sizes     |

**When to use:**

* You have two groups (or two time-points) and want a scale-free estimate of their mean difference.
* Particularly helpful when sample variances differ or when you need a bias correction (Hedges’ g).

---

## 2. Correlation & Proportion Explained

| Metric                                   | Test(s)                | Formula                                                                     | Interpretation                         | Typical Scenario                               |
| ---------------------------------------- | ---------------------- | --------------------------------------------------------------------------- | -------------------------------------- | ---------------------------------------------- |
| **Pearson’s r**                          | Correlation/regression | $r = \frac{\mathrm{Cov}(X,Y)}{s_Xs_Y}$                                      | Small ≈ 0.1, Med ≈ 0.3, Large ≈ 0.5    | Relationship between study time and exam score |
| **$r^2$** (coefficient of determination) | Regression ANOVA       | $r^2 = \frac{\text{SS}_\text{reg}}{\text{SS}_\text{tot}}$                   | Proportion of variance explained       | Forecasting sales based on ad spend            |
| **Eta squared (η²)**                     | One-way ANOVA          | $\displaystyle η^2=\frac{\text{SS}_\text{between}}{\text{SS}_\text{total}}$ | Small < 0.06, Med < 0.14, Large ≥ 0.14 | Comparing test scores across teaching methods  |
| **Omega squared (ω²)**                   | One-way ANOVA          | Slightly adjusts for df                                                     | More conservative than η²              | Policy impact evaluation across regions        |

**When to use:**

* **r / r²** when you’re assessing linear associations or building predictive models.
* **η²/ω²** when comparing more than two groups and wanting proportion-of-variance metrics.

---

## 3. Binary & Categorical Outcomes

| Metric                   | Test(s)                         | Formula sketch                             | Interpretation                 | Typical Scenario                      |
| ------------------------ | ------------------------------- | ------------------------------------------ | ------------------------------ | ------------------------------------- |
| **Odds ratio (OR)**      | Chi-square, logistic regression | $\displaystyle OR=\frac{p/(1-p)}{q/(1-q)}$ | OR > 1 risk higher in group 1  | Drug vs. placebo for side-effect risk |
| **Risk ratio (RR)**      | Cohort studies                  | $\displaystyle RR = \frac{p}{q}$           | RR > 1 risk higher             | Vaccine efficacy (infection rates)    |
| **Phi (ϕ) / Cramér’s V** | Chi-square (2×2 / larger)       | $\displaystyle ϕ=\sqrt{\frac{χ^2}{N}}$     | 0 to 1; small < 0.1, med < 0.3 | Gender vs. purchase preference        |

**When to use:**

* **OR/RR** when the outcome is binary. ORs come from case–control or logistic models; RRs are more intuitive in cohort data.
* **ϕ/Cramér’s V** when both variables are categorical and you want a symmetric association measure.

---

## 4. Nonparametric & Rank-Based Equivalents

| Metric            | Test(s)                  | Relation                                                | Typical Scenario                      |
| ----------------- | ------------------------ | ------------------------------------------------------- | ------------------------------------- |
| **r (from z)**    | Mann–Whitney U, Wilcoxon | $r = \frac{Z}{\sqrt{N}}$                                | Comparing customer satisfaction ranks |
| **Cliff’s Delta** | Mann–Whitney U           | Probability that one random observation exceeds another | Effect in ordinal survey responses    |

**When to use:**

* Your data violate parametric assumptions (non-normal, ordinal).
* You still need a standardized effect rather than just a p-value.

---

### Putting It All Together

* **Clinical Trials:** Cohen’s d for continuous endpoints; OR/RR for adverse-event rates.
* **Education Research:** η²/ω² for multi-group ANOVAs; Pearson’s r for skill–performance correlations.
* **Market Research:** Phi/V for brand preference surveys; r/U-based metrics for rank-order data.
* **Psychology & Social Sciences:** Emphasis on Cohen’s d and Pearson’s r, with clear benchmarks and confidence intervals to convey real-world impact.
