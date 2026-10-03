from __future__ import annotations
from .core import summarize_log, extract_indicators
REGISTRY={"log-summary":summarize_log,"indicators":extract_indicators}
def names(): return sorted(REGISTRY)
def run(name,text):
 if name not in REGISTRY: raise KeyError(name)
 return REGISTRY[name](text)
