from __future__ import annotations
from .cases import load, save, now
SEVERITIES={"info","low","medium","high","critical"}

def add(case_dir,title,severity="info",evidence="",observation=""):
 if severity not in SEVERITIES: raise ValueError("invalid severity")
 data=load(case_dir); finding={"id":f"F-{len(data.get('findings',[]))+1:03d}","title":title,"severity":severity,"evidence":evidence,"observation":observation,"created_utc":now()}
 data.setdefault("findings",[]).append(finding)
 data.setdefault("timeline",[]).append({"time":finding["created_utc"],"type":"finding","detail":f"{finding['id']} {title} [{severity}]"})
 save(case_dir,data); return finding

def list_findings(case_dir): return load(case_dir).get("findings",[])
