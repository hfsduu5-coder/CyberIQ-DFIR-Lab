# CyberIQ DFIR Lab

> **Personal cybersecurity project by Muqtada Al-Sadr Jarallah Khalif (Al-Hantooshi)**  
> Developer • Team Leader of CyberIQ

![Version](https://img.shields.io/badge/version-1.2.1-B00020) ![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white) ![Scope](https://img.shields.io/badge/DFIR-local--first-800020)

A Python **Digital Forensics & Incident Response workbench** for authorized investigations, CTF/DFIR practice, education, and defensive security engineering.

> [!IMPORTANT]
> CyberIQ DFIR Lab works on supplied local evidence. It intentionally excludes network scanning, exploitation, credential attacks, persistence, and malware behavior.

## What v1.2 does

**Evidence → SHA-256 manifest → offline analysis → normalized case timeline → analyst notes/status → JSON/Markdown/HTML report → local dashboard**

- Case workspaces with evidence, reports and notes directories
- Evidence copy + SHA-256 integrity record + size/provenance metadata
- Offline log-level summaries with stricter level matching and validated IPv4 inventory
- IPv4/domain/SHA-256 pattern inventory from supplied evidence
- ISO timestamp timeline extraction from supplied logs
- Case event timeline, analyst notes and controlled lifecycle status
- Case schema validation and evidence integrity re-verification
- Chain-of-custody activity records
- Structured analyst findings with severity and evidence references
- JSON, Markdown and standalone HTML exports; Markdown reports include findings, evidence hashes, custody records and timeline
- Read-only local HTML dashboard
- Small safe offline plugin registry
- Synthetic example evidence
- Unit/regression tests and GitHub Actions matrix for Python 3.10–3.13
- Architecture, analyst, security and contribution documentation

## Install

```bash
git clone https://github.com/hfsduu5-coder/CyberIQ-DFIR-Lab.git
cd CyberIQ-DFIR-Lab
python -m venv .venv
pip install -e .
cyberiq-dfir --version
```

## Investigation workflow

```bash
cyberiq-dfir case-new incident-001
cyberiq-dfir case-add cases/incident-001 examples/sample.log
cyberiq-dfir analyze-log examples/sample.log --output analysis.json
cyberiq-dfir timeline examples/sample.log --output timeline.json
cyberiq-dfir case-note cases/incident-001 "Initial evidence review complete"
cyberiq-dfir case-status cases/incident-001 review
cyberiq-dfir case-verify cases/incident-001
cyberiq-dfir case-validate cases/incident-001
cyberiq-dfir custody-add cases/incident-001 review --actor analyst --detail "Integrity checked"
cyberiq-dfir finding-add cases/incident-001 "Synthetic training observation" --severity low --evidence sample.log
cyberiq-dfir case-export cases/incident-001 report.html --format html
cyberiq-dfir dashboard cases/incident-001 --output dashboard.html
```

## Offline plugins

```bash
cyberiq-dfir plugin-list
cyberiq-dfir plugin-run indicators examples/sample.log
cyberiq-dfir plugin-run log-summary examples/sample.log
```

## Architecture

```text
                  CYBERIQ DFIR LAB
                         │
                 Case Workspace
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
      Evidence       Analyst Notes     Status
          │
    SHA-256 + metadata
          │
          ▼
     Offline Parsers
   Logs • IOCs • Timeline
          │
          ▼
      Case Timeline
          │
     ┌────┴────┐
     ▼         ▼
   Reports   Dashboard
 JSON/MD/HTML  HTML
```

## Tests

```bash
python -m unittest discover -s tests -v
```

The repository defines CI across Python 3.10–3.13. The README does not claim a current remote CI result.

## Documentation

- `docs/ARCHITECTURE.md` — evidence pipeline and design boundaries
- `docs/ANALYST-GUIDE.md` — practical investigation workflow
- `docs/CASE-WORKFLOW.md` — case lifecycle and review procedure
- `docs/DATA-MODEL.md` — case, evidence, finding and custody records
- `docs/THREAT-MODEL.md` — trust boundaries and untrusted evidence model
- `docs/ROADMAP.md` — planned hardening
- `SECURITY.md` — project security policy
- `CONTRIBUTING.md` — contribution rules
- `CHANGELOG.md` — version history

## Evidence principles

**Authorization first • Preserve originals • Hash evidence • Record provenance • Offline by default • Separate observations from conclusions**

## Portfolio & attribution

This repository documents my personal development work on CyberIQ DFIR Lab. External standards, libraries, formats, and learning resources remain credited to their respective authors and are not presented as my own.

## License

MIT
