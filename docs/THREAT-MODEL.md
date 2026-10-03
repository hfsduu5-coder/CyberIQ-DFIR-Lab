# Threat Model

CyberIQ DFIR Lab assumes evidence may be untrusted. Parsers are designed to treat supplied artifacts as data, not executable content.

## Trust boundaries
- Source evidence is untrusted input.
- Case metadata is local analyst state.
- HTML output escapes case-controlled text.
- The project does not execute evidence, fetch remote indicators, or probe targets.

## Analyst responsibilities
Preserve original evidence outside the working case, validate acquisition procedures, restrict access to sensitive cases, and independently confirm automated observations before drawing conclusions.
