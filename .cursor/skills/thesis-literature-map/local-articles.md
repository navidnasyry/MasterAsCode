# Local Articles Coverage (`articles/DT`)

## Why earlier scan missed most PDFs

The first pass used Cursor workspace search (`Glob`), which only surfaced a few **indexed** files under `articles`. On disk, `articles/DT` has many more PDFs (especially under `ToRead`). Those files were **not ignored by intent** — they were simply not returned by the indexed search. Full coverage now uses direct filesystem listing + PDF text extraction.

## Coverage summary (ToRead only)

Source: `articles/DT/ToRead`  
Catalog file: `catalog.articles-toread.json`  
Total PDFs extracted: **34** (0 read errors)

| Folder | Count | Primary themes |
|--------|------:|----------------|
| `ToRead/` (root) | 11 | DigitalTwin + MAS / architecture |
| `ToRead/MADT+LLM+LSTM/` | 10 | CMAPSS+LSTM, DigitalTwin+LLM, MADT |
| `ToRead/DT+Ontology/` | 10 | DigitalTwin + Ontology |
| `ToRead/DT+SI/` | 3 | DigitalTwin + Swarm Intelligence |

Also present but not citation sources: `deepseek.txt`, `perplexity.txt`, notebooks, screenshots, xlsx/zip.

---

## A) `ToRead/MADT+LLM+LSTM` (core thesis combo)

### CMAPSS + LSTM / RUL

1. **An aircraft engine remaining useful life prediction method based on predictive vector angle minimization and feature fusion gate improved transformer model**  
   DOI: `10.1016/j.jmsy.2024.08.025`  
   Tags: `CMAPSS`, `LSTM` | Combo: `CMAPSS+LSTM`  
   Use: strong RUL method paper for turbofan / CMAPSS baselines.

2. **Asymmetric Loss Functions for Deep Learning: Early Predictions of Remaining Useful Life in Aerospace Gas Turbine Engines**  
   Tags: `CMAPSS`, `LSTM` | Combo: `CMAPSS+LSTM`  
   Use: asymmetric loss / early-RUL — useful for underestimation discussion.

3. **Automated Machine Learning for Remaining Useful Life Predictions**  
   Tags: `CMAPSS`, `LSTM` | Combo: `CMAPSS+LSTM`  
   Use: AutoML comparison baseline for RUL.

4. **Remaining Useful Life Prediction Using Attention-LSTM Neural Network of Aircraft Engines**  
   Year: 2021 | DOI: `10.36001/ijphm.2025.v16i2.4274`  
   Tags: `CMAPSS`, `LSTM` | Combo: `CMAPSS+LSTM`  
   Use: Attention-LSTM baseline for chapter method comparison.

### DigitalTwin + LLM (+ MAS)

5. **Integrating Large Language Model and Digital Twins in the Context of Industry 5.0**  
   Year: 2025 | DOI: `10.1016/j.rcim.2025.102982`  
   Tags: `DigitalTwin`, `LLM` | Combo: `DigitalTwin+LLM`  
   Use: already aligned with thesis bib key `CHEN2025102982LLMDT`.

6. **Leveraging Large Language Models for Enhanced Digital Twin Modeling: Trends, Methods, and Challenges**  
   Tags: `DigitalTwin`, `LLM` | Combo: `DigitalTwin+LLM`  
   Use: survey-style support for LLM-enhanced DT modeling.

7. **LLM experiments with simulation: Large Language Model Multi-Agent System for Simulation Model Parametrization in Digital Twin**  
   Tags: `DigitalTwin`, `LLM`/`MAS` (by title)  
   Use: LLM-MAS for DT simulation parametrization — very close to thesis architecture.

8. **Multi-Agent Systems for Manufacturing Digital Twins: A Perspective on Agency and Large Language Models**  
   Year: 2025 | DOI: `10.1016/j.ifacol.2025.09.271`  
   Tags: `DigitalTwin`, `LLM` | Combo: `DigitalTwin+LLM` (+ MAS by title)  
   Use: **High priority** for MADT + LLM related work.

9. **Predictive Analytics Based on Digital Twins, Generative AI, and ChatGPT**  
   Author: Mihail Mateev | DOI: `10.54808/WMSCI2023.01.168`  
   Tags: `DigitalTwin`, `LLM` | Combo: `DigitalTwin+LLM`  
   Use: early DT + generative AI predictive analytics evidence.

10. `grok_report_1.pdf` — generated report artifact, not a peer-reviewed paper.

---

## B) `ToRead/` root (DigitalTwin + MAS / architecture)

1. A Quality-Oriented Digital Twin Modelling Method for Manufacturing — DOI `10.1016/j.promfg.2020.10.044` — `DigitalTwin+MAS`
2. An Agent-Based Architecture of the Digital Twin for an Emergency Department — DOI `10.3390/su15043412` — `DigitalTwin`
3. Developing a Digital Twin for Testing Multi-Agent Systems (2023) — `DigitalTwin+MAS`
4. Digital twin-enabled automated anomaly detection and bottleneck identification... multi-agent approach — DOI `10.1016/j.jmsy.2023.02.008` — `DigitalTwin+MAS`
5. Digital-Twin Integration in Multi-Agent Cyber-Physical Manufacturing Systems — DOI `10.1016/j.ifacol.2021.08.096` — `DigitalTwin+MAS`
6. Large-scale field demonstration of an interoperable and ontology-based... building digital twins — `DigitalTwin`
7. Reference architecture and ontology framework for digital twin construction — DOI `10.1016/j.autcon.2025.106111` — `DigitalTwin+Ontology`
8. Short Survey: The Role of Multi-Agents in Digital Twin Implementation — DOI `10.1145/3697350` — `DigitalTwin+MAS`
9. Generic Multi-Layered Digital-Twin-Framework-Enabled Asset Lifecycle Management... — DOI `10.3390/su15043470` — `DigitalTwin`
10. Towards Agrirobot Digital Twins: Agri-RO5 Multi-Agent Architecture — DOI `10.3390/electronics13010080` — `DigitalTwin+MAS`
11. Towards developing Digital Twin enabled... — `DigitalTwin+MAS`

---

## C) `ToRead/DT+Ontology`

High-value for semantic/layer design of DT:

- Ontologies in digital twins: A systematic literature review (2024)
- Reference architecture and ontology framework for digital twin construction (DOI `10.1016/j.autcon.2025.106111`)
- Cognitive twin construction for system-of-systems... (DOI `10.3233/ICA-220677`)
- Digital Twin Sensors in Cultural Heritage Ontology Applications (DOI `10.3390/s24123978`)
- Plus domain cases (land-use, IoT zero-touch, occupant feedback, carbon emissions, heritage DT)
- Kitchenham 2007: methodology for systematic reviews (not DT-core)

---

## D) `ToRead/DT+SI` (Digital Twin + Swarm Intelligence)

1. Adaptive Swarm Intelligent Offloading Based on Digital Twin-assisted Prediction in VEC — DOI `10.1109/TMC.2023.3344645`
2. An Intelligent Monitoring and Warning Framework in Drone Swarm Digital Twin Systems — DOI `10.1109/ICC51166.2024.10622736`
3. Exploring 6G Potential for Industrial Digital Twinning and Swarm Intelligence...

Use when discussing distributed agent coordination / swarm-inspired multi-agent DT.

---

## Note on `articles/DT/Done`

There are **~20 additional PDFs** under `articles/DT/Done` (surveys, MADTwin, MAS surveys, LLM-agent DT interaction, etc.). They were not fully extracted in this pass because the immediate gap was `ToRead`. They should be indexed next with the same pipeline.

## Retrieval rule for this skill

When answering thesis literature questions:

1. Query `catalog.local.json` (thesis bib)
2. Query `catalog.articles-toread.json` (local ToRead PDFs)
3. Check `new-2026-candidates.md` for external 2026 papers
4. Prefer DOI-backed peer-reviewed sources over generated reports / notes
