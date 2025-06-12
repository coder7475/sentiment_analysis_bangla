## 📊 Final Sentiment Label Imbalance Analysis

### 🧾 Label Definitions

| Label ID | Sentiment |
|----------|-----------|
| 0        | Negative  |
| 1        | Positive  |
| 2        | Neutral   |

---

### 🔢 Overall Distribution

#### 📌 Counts:

| Sentiment | Count |
|-----------|-------|
| Negative (0) | **3,667** |
| Neutral  (2) | 2,251 |
| Positive (1) | **1,825** |
| **Total**    | **7,743** |

#### 📌 Percentages:

| Sentiment | Percentage |
|-----------|------------|
| Negative  | **47.36%** |
| Neutral   | 29.07%     |
| Positive  | **23.57%** |

---

### ⚖️ Imbalance Ratio

```csv
Metric,Value
Imbalance Ratio,2.0093150684931507
```

- The **imbalance ratio** is defined as:

  \[
  \text{Imbalance Ratio} = \frac{\text{Majority Class Count}}{\text{Minority Class Count}} = \frac{3667}{1825} \approx 2.01
  \]

- The **majority class** is **Negative (0)**.
- The **minority class** is **Positive (1)**.

---

### 📈 Interpretation

- A ratio of **2.01** indicates a **moderate imbalance** — the Negative class appears **twice as often** as the Positive class.
- While this isn't considered extreme, it can:
  - Bias models toward predicting the **majority class** (Negative).
  - Result in **lower recall and precision** for the Positive class if not handled properly.
- The Neutral class (29.07%) is closer to balance but still significantly less than Negative.

---

### 🧠 Why This Matters

- Machine learning models tend to **optimize for the majority class** in imbalanced datasets, which:
  - Skews accuracy,
  - Masks poor performance on underrepresented classes,
  - Leads to unfair or incomplete sentiment predictions.

---

### ✅ Recommendations

| Strategy | Action |
|----------|--------|
| **Model Evaluation** | Use metrics like **macro F1-score**, **recall**, and **precision per class** |
| **Data Handling**    | Apply **stratified sampling**, or use **resampling** techniques (e.g., SMOTE, undersampling) |
| **Training**         | Use **class weights** (e.g., `class_weight='balanced'` in scikit-learn) |
| **Monitoring**       | Continuously track performance separately for each label, not just overall accuracy |

---

### 📌 Conclusion

> Your dataset is **moderately imbalanced**, with Negative sentiments being twice as frequent as Positive ones. This could lead to **predictive bias** if unaddressed, especially in real-world applications like feedback analysis, reviews, or social sentiment tracking.
