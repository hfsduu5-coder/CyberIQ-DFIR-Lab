from __future__ import annotations
import re
from .schemas import CASE_SCHEMA, ALLOWED_STATUS
SHA256=re.compile(r"^[0-9a-fA-F]{64}$")
SEVERITIES={"info","low","medium","high","critical"}
def validate_case(data):
 errors=[]
 if data.get("schema")!=CASE_SCHEMA: errors.append("unsupported case schema")
 if not isinstance(data.get("case"),str) or not data.get("case","").strip(): errors.append("case name is required")
 if data.get("status") not in ALLOWED_STATUS: errors.append("invalid case status")
 for key in ("timeline","evidence","findings","chain_of_custody"):
  if not isinstance(data.get(key),list): errors.append(f"{key} must be a list")
 evidence=data.get("evidence",[]) if isinstance(data.get("evidence"),list) else []
 ids=set()
 for i,item in enumerate(evidence):
  if not isinstance(item,dict): errors.append(f"evidence[{i}] must be an object"); continue
  if not SHA256.fullmatch(str(item.get("sha256",""))): errors.append(f"evidence[{i}] invalid sha256")
  eid=item.get("id")
  if eid:
   if eid in ids: errors.append(f"duplicate evidence id {eid}")
   ids.add(eid)
 findings=data.get("findings",[]) if isinstance(data.get("findings"),list) else []
 for i,item in enumerate(findings):
  if not isinstance(item,dict): errors.append(f"findings[{i}] must be an object"); continue
  if item.get("severity") not in SEVERITIES: errors.append(f"findings[{i}] invalid severity")
 for key in ("timeline","chain_of_custody"):
  items=data.get(key,[]) if isinstance(data.get(key),list) else []
  for i,item in enumerate(items):
   if not isinstance(item,dict): errors.append(f"{key}[{i}] must be an object")
 return {"valid":not errors,"errors":errors}
