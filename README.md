```markdown
# Mamaearth E-Commerce Analytics & GenAI Narrative Pipeline

This document guides you through reproducing all reported figures end-to-end across Parts 1, 2, and 3. Follow the steps sequentially from top to bottom.

---

## 1. Database Setup & SQL Reporting (Part 1)

Execute the database schema setup, load the seed transactional data, and run the analytical validation reports:

### Using SQLite Online / Local CLI
1. Open [SQLite Online](https://sqliteonline.com/) (or launch your local terminal).
2. Open and run `sql/schema.sql` to build the required table structures.
3. Open and run `sql/seed_data.sql` to ingest the initial raw order and customer records.
4. Open and execute `sql/reports.sql` in order to generate the baseline reconciliation queries and identify duplicate discrepancies.

```bash
# Alternative: Local SQLite CLI execution
sqlite3 mamaearth.db < sql/schema.sql
sqlite3 mamaearth.db < sql/seed_data.sql
sqlite3 mamaearth.db < sql/reports.sql

```

> **Note:** The SQL database is self-contained for Part 1. Part 2 reads directly from raw CSV files in `data/`.

---

## 2. Python Data Wrangling, EDA, & Findings Export (Part 2)

Run the analytical scripts in this exact order from the project root directory:

```bash
python analysis/clean_and_eda.py
python analysis/visualize.py

```

* **`analysis/clean_and_eda.py`**: Ingests raw data files (`orders.csv`, `customers.csv`, `products.csv`), resolves duplicate order entries, handles anomalies, and executes the core EDA. **Task 5 of Part 2 programmatically writes the computed values to `narrator/findings.json**`.
*(Do not hand-edit `narrator/findings.json` — this automated step prevents analytical figures from silently drifting from downstream reports).*
* **`analysis/visualize.py`**: Rebuilds the cleaned analytical dataset and outputs distribution and revenue charts into `visualizations/`:
* `visualizations/return_rate_by_payment.png`
* `visualizations/monthly_revenue_trend.png`



---

## 3. GenAI Insight Narrative Generation (Part 3)

Once `narrator/findings.json` has been generated, run `narrator/generate_narrative.py` to produce the Situation–Complication–Resolution (SCR) business report.

### Path A: Online Mode (Using Free Gemini API Key)

Set your Google AI Studio free-tier API key as an environment variable and execute the script:

**macOS / Linux:**

```bash
export GEMINI_API_KEY="your_actual_api_key_here"
python narrator/generate_narrative.py

```

**Windows (PowerShell):**

```powershell
$env:GEMINI_API_KEY="your_actual_api_key_here"
python narrator/generate_narrative.py

```

**Windows (Command Prompt):**

```cmd
set GEMINI_API_KEY="your_actual_api_key_here"
python narrator/generate_narrative.py

```

* The online path queries the Gemini model with strictly locked parameters (`temperature=0.0`, explicit token limits, and a $\ge 10\text{s}$ request timeout) to guarantee deterministic, hallucination-free output.

### Path B: Keyless Offline Fallback Path (Zero-Spend / Air-Gapped)

If no API key is configured in your environment, the script automatically routes execution through `generate_scr_narrative_offline(findings)`:

```bash
# Ensure GEMINI_API_KEY is unset
unset GEMINI_API_KEY  # On Windows CMD: set GEMINI_API_KEY= | PowerShell: Remove-Item Env:\GEMINI_API_KEY

python narrator/generate_narrative.py

```

* **No network access, paid quota, or setup required.** The offline path renders the narrative using a deterministic f-string template directly from `narrator/findings.json`.

---

## Verification & Output Artifacts

Both execution paths automatically write the resulting text to `narrator/sample_output.txt` and run an automated numeric accuracy checklist confirming the presence of all five core metrics:

1. **Cleaned Total Revenue:** `INR 97,358.30` (or `97358.3`)
2. **COD Return Rate:** `44.4%`
3. **Highest-Risk Segment (COD, Tier-2):** `54.5%`
4. **Duplicate Reconciliation Delta:** `INR 2,501.90` (or `2501.9`)
5. **True Peak Month & Revenue:** `March` together with `INR 20,318.90` (or `20318.9`)

```

<FollowUp label="Would you like an automated grading bash script to verify all three steps in sequence?" query="Can you provide a shell script that runs the entire pipeline from Step 1 to Step 3 and confirms zero errors?"/>

```
