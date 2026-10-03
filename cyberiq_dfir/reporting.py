from __future__ import annotations
import html, json
from pathlib import Path

def markdown_report(title,data):
 body=[f"# {title}","","> Generated locally by CyberIQ DFIR Lab.",""]
 body += ["## Summary","",f"- Schema: {data.get('schema','n/a')}",f"- Status: {data.get('status','n/a')}",f"- Evidence items: {len(data.get('evidence',[]))}",f"- Findings: {len(data.get('findings',[]))}",f"- Custody records: {len(data.get('chain_of_custody',[]))}","", "## Findings",""]\n for f in data.get("findings",[]): body.append(f"- **{f.get('id','')} [{f.get('severity','')}] {f.get('title','')}** — Evidence: {f.get('evidence','n/a')} — {f.get('observation','')}")\n body += ["","## Evidence",""]\n for x in data.get("evidence",[]): body.append(f"- `{x.get('name','')}` — SHA-256 `{x.get('sha256','')}` — {x.get('size',0)} bytes")\n body += ["","## Chain of Custody",""]\n for x in data.get("chain_of_custody",[]): body.append(f"- **{x.get('time','')}** — {x.get('actor','')}: {x.get('action','')} — {x.get('detail','')}")\n body += ["","## Timeline",""]
 for e in data.get("timeline",[]): body.append(f"- **{e.get('time','')}** — {e.get('type','event')}: {e.get('detail','')}")
 return "\n".join(body)+"\n"
def html_report(title,data):
 rows="".join(f"<tr><td>{html.escape(str(e.get('time','')))}</td><td>{html.escape(str(e.get('type','')))}</td><td>{html.escape(str(e.get('detail','')))}</td></tr>" for e in data.get("timeline",[]))
 return f"""<!doctype html><meta charset="utf-8"><title>{html.escape(title)}</title><style>body{{font-family:system-ui;background:#090909;color:#eee;max-width:1000px;margin:40px auto;padding:20px}}h1{{color:#e53935}}table{{width:100%;border-collapse:collapse}}td,th{{padding:10px;border-bottom:1px solid #333;text-align:left}}code{{color:#ff6b6b}}</style><h1>{html.escape(title)}</h1><p>Local CyberIQ DFIR report. Evidence items: <b>{len(data.get('evidence',[]))}</b>. Status: <b>{html.escape(str(data.get('status','n/a')))}</b>.</p><table><tr><th>Time</th><th>Type</th><th>Detail</th></tr>{rows}</table>"""
def export_case(data,path,fmt):
 p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
 if fmt=="json": p.write_text(json.dumps(data,indent=2),encoding="utf-8")
 elif fmt=="md": p.write_text(markdown_report(data.get("case","DFIR Case"),data),encoding="utf-8")
 elif fmt=="html": p.write_text(html_report(data.get("case","DFIR Case"),data),encoding="utf-8")
 else: raise ValueError("format must be json, md, or html")
 return p
