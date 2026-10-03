# Architecture

CyberIQ DFIR Lab follows a local-first evidence pipeline:

1. Preserve supplied source evidence.
2. Record SHA-256, size, path and acquisition-record time.
3. Parse copies or supplied text locally.
4. Normalize observations separately from analyst conclusions.
5. Export reproducible reports.

The v0.1 core performs no network collection.
