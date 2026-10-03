from __future__ import annotations
import html, json
from pathlib import Path

def markdown_report(title,data):
 body=[f"# {title}","","> Generated locally by CyberIQ DFIR Lab.",""]
 body += ["## Summary","",f"- Schema: {data.get('schema','n/a')}",f"- Status: {data.get('status','n/a')}",f"- Evidence items: {len(data.get('evidence',[]))}",f"- Findings: {len(data.get('findings',[]))}",f"- Custody records: {len(data.get('chain_of_custody',[]))}","", "## Findings",""]\n for f in data.get("findings",[]): body.append(f"- **{f.get('id','')} [{f.get('severity','')}] {f.get('title','')}** — Evidence: {f.get('evidence','n/a')} — {f.get('observation','')}")\n body += ["","## Evidence",""]\n for x in data.get("evidence",[]): body.append(f"- `{x.get('name','')}` — SHA-256 `{x.get('sha256','')}` — {x.get('size',0)} bytes")\n body += ["","## Chain of Custody",""]\n for x in data.get("chain_of_custody",[]): body.append(f"- **{x.get('time','')}** — {x.get('actor','')}: {x.get('action','')} — {x.get('detail','')}")\n body += ["","## Timeline",""]
 for e in data.get("timeline",[]): body.append(f"- **{e.get('time','')}** — {e.get('type','event')}: {e.get('detail','')}")
 return "\n".join(body)+"\n"
def html_report(title,data):
 def esc(v): return html.escape(str(v))
 def rows(items,fields):
  return ''.join('<tr>'+''.join('<td>'+esc(item.get(field,''))+'</td>' for field in fields)+'</tr>' for item in items)
 findings=rows(data.get('findings',[]),('id','severity','title','evidence','observation'))
 evidence=rows(data.get('evidence',[]),('id','name','sha256','size'))
 custody=rows(data.get('chain_of_custody',[]),('time','actor','action','detail'))
 timeline=rows(data.get('timeline',[]),('time','type','detail'))
 return "<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>"+esc(title)+"</title></head><body><h1>"+esc(title)+"</h1><p>Local CyberIQ DFIR report. Status: <b>"+esc(data.get('status','n/a'))+"</b></p><h2>Findings</h2><table>"+findings+"</table><h2>Evidence</h2><table>"+evidence+"</table><h2>Chain of Custody</h2><table>"+custody+"</table><h2>Timeline</h2><table>"+timeline+"</table></body></html>"
def export_case(data,path,fmt):
 p=Path(path)
 if p.exists() and p.is_dir(): raise ValueError('output must be a file path')
 p.parent.mkdir(parents=True,exist_ok=True)
 if fmt=="json": p.write_text(json.dumps(data,indent=2),encoding="utf-8")
 elif fmt=="md": p.write_text(markdown_report(data.get("case","DFIR Case"),data),encoding="utf-8")
 elif fmt=="html": p.write_text(html_report(data.get("case","DFIR Case"),data),encoding="utf-8")
 else: raise ValueError("format must be json, md, or html")
 return p
