# Data Model

## Case
Schema: `cyberiq.case.v1`

Core fields: case name, status, creation time, evidence records, timeline events, findings, and chain-of-custody entries.

## Evidence record
Records local working-copy path, file name, byte size, SHA-256, and record time.

## Finding
A finding has an ID, title, severity, evidence reference, observation text, and creation time. Findings are analyst records, not automatic proof of compromise.

## Chain of custody
Each entry records UTC time, actor label, action, and detail. This is an educational/local workflow record and does not by itself satisfy any jurisdiction's evidentiary rules.
