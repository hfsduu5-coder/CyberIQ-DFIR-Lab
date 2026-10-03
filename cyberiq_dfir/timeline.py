from __future__ import annotations
import re
from datetime import datetime
ISO=re.compile(r"^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z?)\s+(.*)$")
def parse_lines(text,source="input"):
 out=[]
 for n,line in enumerate(text.splitlines(),1):
  m=ISO.match(line.strip())
  if not m: continue
  raw,msg=m.groups()
  try: dt=datetime.fromisoformat(raw.replace("Z","+00:00"))
  except ValueError: continue
  out.append({"timestamp":dt.isoformat(),"source":source,"line":n,"message":msg})
 return sorted(out,key=lambda x:x["timestamp"])
