from __future__ import annotations
from pathlib import Path
from .core import sha256_file
from .cases import load

def verify_case(case_dir):
 case=Path(case_dir).resolve(); data=load(case); results=[]
 for item in data.get("evidence",[]):
  raw=Path(item.get("path",""))
  candidate=(case/raw).resolve() if not raw.is_absolute() else raw.resolve()
  try:
   candidate.relative_to(case); safe=True
  except ValueError:
   safe=False
  exists=safe and candidate.is_file()
  actual=sha256_file(candidate) if exists else None
  results.append({"id":item.get("id"),"name":item.get("name"),"exists":exists,"safe_path":safe,"expected_sha256":item.get("sha256"),"actual_sha256":actual,"match":exists and actual==item.get("sha256")})
 return {"case":data.get("case"),"verified":all(x["match"] for x in results),"item_count":len(results),"items":results}
