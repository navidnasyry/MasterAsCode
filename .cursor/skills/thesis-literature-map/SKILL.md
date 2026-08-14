---
name: thesis-literature-map
description: Builds and queries a structured literature map for this thesis. Use when the user asks for related work, citations, topic combinations (CMAPSS, Digital Twin, LLM, LSTM, MAS), or wants recent 2025-2026 papers and prioritized references.
disable-model-invocation: true
---

# Thesis Literature Map

## Scope

Use this skill as the primary retrieval workflow for thesis writing in this repository, with source priority:

1. `Writing/Theses/IUT_Theses` (thesis text and citations)
2. `Writing/Theses/IUT_Theses/my_ref.bib` (master bibliography)
3. `articles` (local papers and notes)
4. `gpt-scholar.md` + `catalog.gpt-scholar.json` (curated 2026 GPT Scholar harvest)
5. curated 2026 additions in `new-2026-candidates.md`

## Available Files

- `catalog.local.json`: machine-readable index generated from `my_ref.bib` with inferred tags and priority score.
- `catalog.articles-toread.json`: extracted index of all PDFs under `articles/DT/ToRead` (including `MADT+LLM+LSTM`, `DT+Ontology`, `DT+SI`).
- `gpt-scholar.md`: raw curated notes of 26 recent (mostly 2026) papers from GPT Scholar.
- `catalog.gpt-scholar.json`: structured tagged index of `gpt-scholar.md`.
- `new-2026-candidates.md`: merged 2026 candidates (web search + GPT Scholar), with priority reading list.
- `query-guide.md`: quick search and ranking rules for retrieval.
- `local-articles.md`: human-readable coverage of local `articles/DT/ToRead` PDFs by folder/topic.
- `scripts/query_catalog.py`: fast CLI query utility for tags/combinations.

## Important indexing rule

Do **not** rely only on Cursor `Glob`/workspace search for `articles/**/*.pdf`. Many PDFs are on disk but not returned by indexed search. Always list via filesystem (`Get-ChildItem` / `Path.rglob`) when refreshing local article coverage.

## Topic Tags

Use these normalized tags:

- `CMAPSS`
- `DigitalTwin`
- `LLM`
- `LSTM`
- `MAS`
- `Ontology`
- `SwarmIntelligence`
- `General`

For each paper, infer one or more `combo` labels:

- `CMAPSS+LSTM`
- `CMAPSS+DigitalTwin`
- `CMAPSS+LLM`
- `DigitalTwin+LLM`
- `DigitalTwin+MAS`
- `DigitalTwin+Ontology`
- `CMAPSS+LLM+DigitalTwin`
- `CMAPSS+LSTM+DigitalTwin`
- `MAS+LLM+DigitalTwin`

## Retrieval Workflow

When user asks for writing support:

1. Parse request into:
   - thesis section goal
   - required topic tags
   - year window (default: newest first)
2. Select candidates from `catalog.local.json` by tag intersection.
3. Also select from `catalog.articles-toread.json` (local PDFs), especially for MADT / Ontology / LSTM / LLM folders.
4. Also select from `catalog.gpt-scholar.json` for 2026-focused combos and research-gap claims.
5. Expand with `new-2026-candidates.md` if year >= 2025 requested.
6. Rank using this order:
   - tag-combo exact match
   - recency (2026 > 2025 > older)
   - source quality (journal/conference > arXiv > web/article page)
   - priority score
7. Return 5-12 best papers in this format:
   - Title
   - Authors
   - Year
   - DOI/URL
   - Why relevant (1-2 lines)
   - Thesis-ready claim(s) that can be cited

## Output Template

Use this fixed Persian-friendly template for user-facing outputs:

- **موضوع/ترکیب:** `<combo>`
- **مقاله:** `<title>`
- **نویسندگان:** `<authors>`
- **سال:** `<year>`
- **DOI/Link:** `<doi-or-url>`
- **ارتباط با پایان‌نامه:** `<1-2 short lines>`
- **نکته کلیدی قابل استناد:** `<1 short claim>`
- **اولویت استفاده:** `High | Medium | Low`

## Quality Rules

- Prefer papers with DOI.
- If a source looks weak or unverifiable, mark as `Needs verification`.
- Do not invent missing bibliographic fields.
- If a citation key is duplicated in bib (same key, different papers), warn and suggest key normalization.

## Maintenance

When bibliography changes:

1. Regenerate `catalog.local.json` from `my_ref.bib`.
2. Re-check duplicate keys and missing DOI.
3. If `gpt-scholar.md` changes, regenerate `catalog.gpt-scholar.json`.
4. Append only non-duplicate papers to `new-2026-candidates.md`.

## Utility Commands

From repository root:

- `python ".cursor/skills/thesis-literature-map/scripts/query_catalog.py" --tags CMAPSS,LSTM --top 8`
- `python ".cursor/skills/thesis-literature-map/scripts/query_catalog.py" --combo "DigitalTwin+LLM" --min-year 2024 --top 10`
