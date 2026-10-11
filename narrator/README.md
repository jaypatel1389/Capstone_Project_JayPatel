# Mamaearth E-Commerce Analytics & GenAI Narrative Pipeline

This repository implements an end-to-end analytics and executive reporting pipeline for Mamaearth order transaction data. It covers raw SQL schema ingestion, data hygiene and reconciliation, exploratory data analysis (EDA), automated findings serialization, and Gemini-powered business narrative generation using the Situation–Complication–Resolution (SCR) framework.

---

## Free-Path & API Key Policy

Per the course guidelines, this project uses the free tier of the official Google GenAI SDK (`google-genai`). Google AI Studio issues a free Gemini API key that incurs zero charges. 

To ensure the pipeline is reproducible and gradable without external dependencies, rate limits, or network connectivity, **Task 4 includes a fully keyless deterministic offline fallback (`generate_scr_narrative_offline`)**. The entire repository can be evaluated with zero API spend or network access.

---

## End-to-End Pipeline Execution

Follow these steps sequentially to reproduce every figure and output reported across Parts 1–3.

### 1. Database Setup & SQL Reporting (Part 1)

Load the relational schema, ingest the raw seed dataset, and execute the analytical audit reports:

```bash
# SQLite execution:
sqlite3 mamaearth.db < sql/schema.sql
sqlite3 mamaearth.db < sql/seed_data.sql
sqlite3 mamaearth.db < sql/reports.sql

# Alternatively, for PostgreSQL:
psql -U postgres -d mamaearth -f sql/schema.sql
psql -U postgres -d mamaearth -f sql/seed_data.sql
psql -U postgres -d mamaearth -f sql/reports.sql
