from __future__ import annotations
from pathlib import Path
from .core import sha256_file
from .cases import load

def verify_case(case_dir):
 case=Path(case_dir); data=load(case); results=[]
 for item in data.get("evidence",[]):
  p=Path(item["path"])
  exists=p.exists(); actual=sha256_file(p) if exists else None
  results.append({"name":item.get("name"),"exists":exists,"expected_sha256":item.get("sha256"),"actual_sha256":actual,"match":exists and actual==item.get("sha256")})
 return {"case":data.get("case"),"verified":all(x["match"] for x in results),"items":results}
