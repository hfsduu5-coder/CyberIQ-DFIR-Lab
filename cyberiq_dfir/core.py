from __future__ import annotations
import hashlib, json, re
from pathlib import Path
from datetime import datetime, timezone

PATTERNS={"ipv4":re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),"domain":re.compile(r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b"),"sha256":re.compile(r"\b[a-fA-F0-9]{64}\b")}

def sha256_file(path):
 h=hashlib.sha256()
 with open(path,"rb") as f:
  for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
 return h.hexdigest()

def evidence_record(path):
 p=Path(path); s=p.stat()
 return {"name":p.name,"path":str(p),"size":s.st_size,"sha256":sha256_file(p),"recorded_utc":datetime.now(timezone.utc).isoformat()}

def extract_indicators(text):
 return {k:sorted(set(v.findall(text))) for k,v in PATTERNS.items()}

def summarize_log(text):
 lines=text.splitlines(); levels={x:0 for x in ("ERROR","WARN","INFO","DEBUG")}
 for line in lines:
  u=line.upper()
  for x in levels:
   if x in u: levels[x]+=1
 return {"lines":len(lines),"levels":levels,"indicators":extract_indicators(text)}

def write_json(data,path): Path(path).write_text(json.dumps(data,indent=2),encoding="utf-8")
