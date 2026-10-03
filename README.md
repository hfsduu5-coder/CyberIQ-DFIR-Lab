# CyberIQ DFIR Lab

> **Personal cybersecurity project by Muqtada Al-Sadr Jarallah Khalif (Al-Hantooshi)**  
> Developer • Team Leader of CyberIQ

![Version](https://img.shields.io/badge/version-0.1.0-B00020) ![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white) ![Scope](https://img.shields.io/badge/scope-local--first%20DFIR-800020)

A local-first **Digital Forensics & Incident Response workbench** for authorized investigations, CTF/DFIR practice, education, and defensive security engineering.

> [!IMPORTANT]
> The v0.1 core analyzes supplied local evidence. It performs no network scanning, exploitation, credential attacks, persistence, or malware behavior.

## Investigation pipeline

```text
Supplied evidence
      │
      ├── SHA-256 + size + provenance record
      ▼
Offline parsing
      │
      ├── log-level summary
      ├── IPv4 / domain / SHA-256 pattern inventory
      ▼
Structured JSON
      │
      └── case workspace / reports
```

## v0.1 implemented

- Python package and `cyberiq-dfir` CLI
- SHA-256 evidence hashing
- Evidence metadata records
- Offline log summarization
- Local indicator-pattern extraction
- Case workspace creation
- JSON output
- Synthetic example evidence
- Unit tests
- GitHub Actions test matrix for Python 3.10–3.13
- Architecture and security documentation

## Quick start

```bash
git clone https://github.com/hfsduu5-coder/CyberIQ-DFIR-Lab.git
cd CyberIQ-DFIR-Lab
pip install -e .
cyberiq-dfir --version
cyberiq-dfir evidence examples/sample.log
cyberiq-dfir analyze-log examples/sample.log
cyberiq-dfir case-new demo-case
```

Run tests:

```bash
python -m unittest discover -s tests -v
```

## Structure

```text
cyberiq_dfir/
  core.py          evidence + offline analysis core
  cli.py           command-line interface
tests/             regression tests
examples/          synthetic safe evidence
docs/              architecture documentation
.github/workflows/ CI definition
```

## Evidence principles

**Authorization first • Preserve originals • Hash evidence • Record provenance • Offline by default • Separate observations from conclusions**

## Roadmap

Next milestones: normalized event schema, timeline engine, case manifest lifecycle, Markdown/HTML reports, read-only dashboard, safe parser plugins, richer synthetic datasets, and expanded tests.

## Portfolio & attribution

This repository documents my personal development work on CyberIQ DFIR Lab. External standards, libraries, formats, and learning resources remain credited to their respective authors and are not presented as my own.

## License

MIT
