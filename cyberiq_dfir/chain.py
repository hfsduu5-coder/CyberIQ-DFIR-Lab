from __future__ import annotations
from .cases import load, save, now

def record(case_dir,action,actor="analyst",detail=""):
 data=load(case_dir)
 entry={"time":now(),"actor":actor,"action":action,"detail":detail}
 data.setdefault("chain_of_custody",[]).append(entry)
 data.setdefault("timeline",[]).append({"time":entry["time"],"type":"custody","detail":f"{actor}: {action} - {detail}".strip(" -")})
 save(case_dir,data); return entry

def history(case_dir): return load(case_dir).get("chain_of_custody",[])
