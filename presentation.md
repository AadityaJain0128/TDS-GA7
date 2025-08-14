---
marp: true
theme: serif
size: 16:9
paginate: true
header: 'Q3 2025 Earnings Report'
footer: 'Confidential & Proprietary'
---

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
## Technical Appendix: Growth Formula

We use the Compound Annual Growth Rate (CAGR) to model long-term performance. The formula is:

$$
\text{CAGR} = \left( \frac{\text{Ending Value}}{\text{Beginning Value}} \right)^{\frac{1}{\text{n}}} - 1
$$

Where:
- $n$ = Number of Years

<!--
Speaker Notes: The CAGR formula is central to how we project future earnings. Marp uses KaTeX to render math formulas beautifully using the $$ syntax.
-->

---

<!-- Slide 7: Q&A -->
## Q&A
### Thank You

Open for questions.

<br>

**Contact:** <a href="mailto:23f2003550@ds.study.iitm.ac.in">23f2003550@ds.study.iitm.ac.in</a>
