from __future__ import annotations
import json, shutil
from datetime import datetime, timezone
from pathlib import Path
from .core import evidence_record

def now(): return datetime.now(timezone.utc).isoformat()
def new_case(name, root="cases"):
 p=Path(root)/name
 for d in ("evidence","reports","notes"): (p/d).mkdir(parents=True,exist_ok=True)
 manifest={"schema":"cyberiq.case.v1","case":name,"status":"open","created_utc":now(),"timeline":[],"evidence":[]}
 save(p,manifest); return manifest
def load(case_dir): return json.loads((Path(case_dir)/"case.json").read_text(encoding="utf-8"))
def save(case_dir,data): (Path(case_dir)/"case.json").write_text(json.dumps(data,indent=2),encoding="utf-8")
def add_evidence(case_dir,source):
 case=Path(case_dir); src=Path(source); dst=case/"evidence"/src.name
 shutil.copy2(src,dst); rec=evidence_record(dst); rec["source_name"]=src.name
 data=load(case); data["evidence"].append(rec); data["timeline"].append({"time":now(),"type":"evidence_added","detail":src.name}); save(case,data); return rec
def note(case_dir,text):
 data=load(case_dir); event={"time":now(),"type":"analyst_note","detail":text}; data["timeline"].append(event); save(case_dir,data); return event
def set_status(case_dir,status):
 data=load(case_dir); data["status"]=status; data["timeline"].append({"time":now(),"type":"status","detail":status}); save(case_dir,data); return data
