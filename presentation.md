---
marp: true
theme: custom-theme
size: 16:9
paginate: true
header: 'Q3 2025 Earnings Report'
footer: 'Confidential & Proprietary'
---

<style>
/* @theme custom-theme */

section {
  background-color: #f0f4f8;
  color: #1a202c;
  font-family: 'Georgia', serif;
  padding: 60px;
}

h1, h2, h3 {
  font-family: 'Helvetica Neue', sans-serif;
  color: #2a4365;
}

a {
  color: #3182ce;
}

header, footer {
  color: #a0aec0;
  font-size: 0.8em;
}
</style>

<!-- 
backgroundImage: "url('https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?auto=format&fit=crop&q=80')"
color: white
-->

<!-- Slide 1: Title Slide -->
# Quarterly Earnings Report
## Q3 2025
<br>

Presented by: Technical Consultant

**Contact:** <a href="mailto:23f2003550@ds.study.iitm.ac.in">23f2003550@ds.study.iitm.ac.in</a>

<!-- 
Speaker Notes: Welcome everyone. Today, we'll review the strong performance from the third quarter of 2025 and discuss our outlook.
-->

---

<!-- Slide 2: Agenda -->
## Agenda & Key Takeaways

- Financial Highlights & Performance
- Segment-wise Revenue Analysis
- Growth Drivers & Strategic Initiatives
- Technical Appendix: Formulas & Code
- Outlook for Q4 2025

<!--
Speaker Notes: This slide provides a quick overview. We'll cover our financial performance, strategic wins, and the technical models behind our analysis.
-->

---

<!-- Slide 3: Key Takeaways -->
### Key Takeaways

1. Record revenue growth this quarter.
2. Successful launch of new digital banking platform.
3. Stronger profit margins due to operational efficiencies.

<!--
Speaker Notes: The key message is that we had a very successful quarter driven by revenue, innovation, and efficiency.
-->

---

<!-- Slide 4: Animated Fragments -->
## Q3 Financial Highlights

- * **Total Revenue:** $1.2B (Up 15% YoY)
- * **Net Profit:** $250M (Up 22% YoY)
- * **Earnings Per Share (EPS):** $1.45 (Up 25% YoY)
- * **New Customer Acquisition:** 500,000+

<!--
Speaker Notes: Let's break down the numbers. Each of these key metrics shows significant year-over-year growth. The '*' causes these to appear one by one. I want to draw special attention to the EPS, which indicates strong shareholder value.
-->

---

<!-- Slide 5: Code Sample -->
## Technical Appendix: Data Processing

Python script used for portfolio risk analysis.

```python
import pandas as pd
import numpy as np

# Load transaction data from Q3
portfolio_data = pd.read_csv('q3_portfolio.csv')

# Calculate Value at Risk (VaR) using Monte Carlo simulation
returns = portfolio_data['returns'].pct_change()
var_95 = np.percentile(returns.dropna(), 5)

print(f"95% Value at Risk (VaR): {var_95:.2%}")
```

<!--
Speaker Notes: For the technical stakeholders, here's a glimpse of our process. We use Python with libraries like Pandas. This ensures our risk assessments are data-driven. Marp provides syntax highlighting automatically.
-->

---

<!-- Slide 6: Mathematical Equation -->
## Technical Appendix: Algorithmic Complexity

We analyze algorithm performance using Big O notation to ensure scalability.

- **Constant Time:** $$ O(1) $$
- **Linear Time:** $$ O(n) $$
- **Quadratic Time:** $$ O(n^2) $$

<!--
Speaker Notes: We prioritize algorithms with lower complexity, ideally linear or constant time, to ensure our systems remain efficient as data volume grows.
-->

---

<!-- Slide 7: Q&A -->
## Q&A
### Thank You

Open for questions.

<br>

**Contact:** <a href="mailto:23f2003550@ds.study.iitm.ac.in">23f2003550@ds.study.iitm.ac.in</a>
