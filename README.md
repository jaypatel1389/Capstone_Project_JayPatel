Mamaearth Order Analytics Pipeline

A three-layer analytics project that turns raw e-commerce order data into verified business insights and a structured Situation–Complication–Resolution narrative.







Layer



Technology



Output





Part 1



SQLite



Relational reports (revenue, returns, rankings)





Part 2



Python / Pandas



Cleaned data, EDA, charts, findings.json





Part 3



Gemini API (with offline fallback)



SCR business narrative

All figures in this repository were produced by running the pipeline against the supplied seed data. They are exact, not estimated.



Repository layout

.
├── README.md
├── requirements.txt
├── sql/
│   ├── schema.sql              # Table definitions
│   ├── seed_data.sql           # Data load (45 + 16 + 180 rows)
│   └── reports.sql             # Business report queries (a–i)
├── data/
│   ├── customers.csv           # 45 customers (source of truth)
│   ├── products.csv            # 16 products (source of truth)
│   └── orders.csv              # 180 orders (source of truth)
├── analysis/
│   ├── clean_and_eda.py        # Cleaning, EDA, findings export
│   └── visualize.py            # Chart generation
├── visualizations/
│   ├── return_rate_by_payment.png
│   └── monthly_revenue_trend.png
└── narrator/
    ├── findings.json           # Machine-written verified figures
    ├── generate_narrative.py   # SCR narrator (online + offline)
    └── sample_output.txt       # Last generated narrative



Prerequisites





Python 3.10+



SQLite 3 (or SQLite Online)



Optional: a free Gemini API key from Google AI Studio

python -m pip install -r requirements.txt



Part 1 — SQL Relational Layer

Goal: Load the raw CSVs into a relational store and answer the business report questions.

sqlite3 mamaearth.db < sql/schema.sql
sqlite3 mamaearth.db < sql/seed_data.sql
sqlite3 mamaearth.db < sql/reports.sql

Alternatively, paste each file into SQLite Online and run in order. Execute the ALTER TABLE statement in reports.sql only once on a freshly created schema.

Verification counts







Table



Rows





customers



45





products



16





orders



180

Selected Part 1 results







Metric



Value





Total orders



180





Raw total revenue



₹99,860.20





Average order value



₹554.78





Orders without a rating



15





Customer with zero orders



C045 (Vihaan)





Highest-return cities



Jaipur 42.1 %, Lucknow 30.6 %, Bangalore 24.2 %

Part 1 is independent of Part 2. Part 2 reads the CSVs directly and does not require the database.



Part 2 — Python / Pandas Cleaning & EDA

Goal: Clean the raw CSVs, run exploratory analysis, produce charts, and export verified figures for Part 3.

python analysis/clean_and_eda.py
python analysis/visualize.py

Pipeline steps (executed by clean_and_eda.py)





Load CSVs — orders.shape must be (180, 9) before cleaning



Standardise payment_method casing → CARD / UPI / COD



Remove five exact duplicate orders (O0176–O0180) → 175 rows



Impute missing discount_pct (→ 0) and rating (→ median 3.0)



Merge with products & customers; compute order_value



Detect quantity outliers via IQR (flag only, do not drop)



Test hypothesis: COD has a higher return rate



Segment risk by payment method × city tier



Correlation analysis across rating, returned, discount, quantity



Outlier-corrected monthly revenue time series



Write narrator/findings.json (never hand-edit this file)

Selected Part 2 results







Metric



Value





Cleaned total revenue



₹97,358.30





Duplicate reconciliation delta



₹2,501.90





COD return rate



44.4 %





CARD return rate



14.7 %





UPI return rate



18.9 %





Highest-risk segment



COD + Tier-2 cities — 54.5 %





True peak month



March 2026 — ₹20,318.90

Charts (visualizations/)







File



Content





return_rate_by_payment.png



Bar chart of return rate by payment method (descending), percentages labelled





monthly_revenue_trend.png



Line chart of outlier-corrected monthly revenue; peak annotated as March 2026

Both scripts are fully re-runnable from the raw CSVs. No intermediate files need to be edited by hand.



Part 3 — GenAI-Powered Insight Narrator

Goal: Turn the verified figures into a concise Situation–Complication–Resolution narrative for Mamaearth’s regional ops and finance heads.

python narrator/generate_narrative.py

The script:





Loads narrator/findings.json



Attempts the online Gemini path (temperature=0.0, explicit token limit, timeout ≥ 10 s)



On missing key, network failure, or any error → switches to a deterministic offline template



Writes the narrative to narrator/sample_output.txt



Runs a numeric-accuracy checklist and prints PASS/FAIL for each required figure

Online path (optional free tier)

# macOS / Linux
export GEMINI_API_KEY="YOUR_GOOGLE_AI_STUDIO_KEY"
python narrator/generate_narrative.py

# Windows PowerShell
$env:GEMINI_API_KEY="YOUR_GOOGLE_AI_STUDIO_KEY"
python narrator/generate_narrative.py

Use a free-tier key from Google AI Studio. Never commit a real API key to the repository.

Offline path (default, zero configuration)

If GEMINI_API_KEY is unset, the script never makes a network call. The offline template still contains every required number and passes the same checker. This is the keyless grading path.

Required numbers in the narrative







Figure



Meaning





97,358.30



Cleaned total revenue





44.4



COD return rate (%)





54.5



COD + Tier-2 highest-risk segment (%)





2,501.90



Duplicate-driven reconciliation delta





March + 20,318.90



True peak month and its revenue



Full reproduction sequence

# Dependencies
python -m pip install -r requirements.txt

# Part 1 (SQL)
sqlite3 mamaearth.db < sql/schema.sql
sqlite3 mamaearth.db < sql/seed_data.sql
sqlite3 mamaearth.db < sql/reports.sql

# Part 2 (Pandas)
python analysis/clean_and_eda.py
python analysis/visualize.py

# Part 3 (Narrator — works with or without an API key)
python narrator/generate_narrative.py

A reader who follows the steps above from a clean checkout will reproduce every number cited in the assignment brief.
