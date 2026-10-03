from __future__ import annotations
import json, re, shutil
from datetime import datetime, timezone
from pathlib import Path
from .core import evidence_record, sha256_file

CASE_NAME=re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$")
def now(): return datetime.now(timezone.utc).isoformat()
def _case_name(name):
 if not isinstance(name,str) or name in (".","..") or not CASE_NAME.fullmatch(name): raise ValueError("case name must use letters, numbers, dot, underscore or hyphen")
 return name
def new_case(name, root="cases"):
 name=_case_name(name); p=Path(root)/name
 if (p/"case.json").exists(): raise FileExistsError("case already exists")
 for d in ("evidence","reports","notes"): (p/d).mkdir(parents=True,exist_ok=True)
 manifest={"schema":"cyberiq.case.v1","case":name,"status":"open","created_utc":now(),"timeline":[],"evidence":[],"findings":[],"chain_of_custody":[]}
 save(p,manifest); return manifest
def load(case_dir): return json.loads((Path(case_dir)/"case.json").read_text(encoding="utf-8"))
def save(case_dir,data):
 p=Path(case_dir)/"case.json"; tmp=p.with_suffix(".json.tmp"); tmp.write_text(json.dumps(data,indent=2),encoding="utf-8"); tmp.replace(p)
def add_evidence(case_dir,source):
 case=Path(case_dir); src=Path(source)
 if not src.is_file(): raise FileNotFoundError("evidence source must be a file")
 data=load(case); digest=sha256_file(src)
 for old in data.get("evidence",[]):
  if old.get("sha256")==digest: raise ValueError("duplicate evidence content")
 dst=case/"evidence"/src.name
 if dst.exists(): dst=dst.with_name(f"{dst.stem}-{digest[:8]}{dst.suffix}")
 shutil.copy2(src,dst); rec=evidence_record(dst); rec["source_name"]=src.name; rec["path"]=str(Path("evidence")/dst.name); rec["id"]=f"E-{len(data.get('evidence',[]))+1:03d}"
 data["evidence"].append(rec); data["timeline"].append({"time":now(),"type":"evidence_added","detail":f"{rec['id']} {src.name}"}); save(case,data); return rec
def note(case_dir,text):
 data=load(case_dir); event={"time":now(),"type":"analyst_note","detail":text}; data["timeline"].append(event); save(case_dir,data); return event
def set_status(case_dir,status):
 from .schemas import ALLOWED_STATUS
 if status not in ALLOWED_STATUS: raise ValueError("invalid case status")
 data=load(case_dir); data["status"]=status; data["timeline"].append({"time":now(),"type":"status","detail":status}); save(case_dir,data); return data
