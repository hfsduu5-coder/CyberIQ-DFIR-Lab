from __future__ import annotations
from .schemas import CASE_SCHEMA, ALLOWED_STATUS

def validate_case(data):
 errors=[]
 if data.get("schema")!=CASE_SCHEMA: errors.append("unsupported case schema")
 if not isinstance(data.get("case"),str) or not data.get("case","").strip(): errors.append("case name is required")
 if data.get("status") not in ALLOWED_STATUS: errors.append("invalid case status")
 if not isinstance(data.get("timeline"),list): errors.append("timeline must be a list")
 if not isinstance(data.get("evidence"),list): errors.append("evidence must be a list")
 for i,item in enumerate(data.get("evidence",[]) if isinstance(data.get("evidence"),list) else []):
  if not isinstance(item,dict): errors.append(f"evidence[{i}] must be an object"); continue
  if not item.get("sha256") or len(str(item.get("sha256")) )!=64: errors.append(f"evidence[{i}] invalid sha256")
 return {"valid":not errors,"errors":errors}
