# Query Guide

## Fast Lookup

Use these indexes together:

- `catalog.local.json` — thesis bibliography
- `catalog.articles-toread.json` — local ToRead PDFs
- `catalog.gpt-scholar.json` — GPT Scholar 2026 harvest
- `new-2026-candidates.md` — merged priority list

Recommended filters:

- by one tag: `CMAPSS` or `LLM`
- by combo: `CMAPSS+LSTM`, `DigitalTwin+LLM`, `CMAPSS+LLM+DigitalTwin`
- by year range: e.g. `>=2024`
- by source: `gpt-scholar` for newest external candidates

## Ranking Heuristic

Sort by:

1. exact combo match
2. `priority_score` descending
3. year descending
4. source trust:
   - Journal/Conference with DOI
   - arXiv with DOI
   - Other URLs

## Suggested Output Sizes

- Literature paragraph support: 3-5 papers
- Related work subsection: 8-12 papers
- Gap analysis: 6-10 papers with at least two combos

## Combination Coverage Checklist

Always try to include at least one paper for each relevant combo:

- `CMAPSS+LSTM`
- `CMAPSS+DigitalTwin`
- `CMAPSS+LLM`
- `DigitalTwin+LLM`
- `CMAPSS+LLM+DigitalTwin`
- `DigitalTwin+MAS` (if architecture/agents are discussed)

## Known Data Issues In Current Bibliography

- Some entries look synthetic or hard to verify; mark `Needs verification` before citation in final thesis text.
- Some citation keys are duplicated (example: `chen2025llmdt`).
- DOI/url fields are missing for some high-priority entries; fill before final submission.
