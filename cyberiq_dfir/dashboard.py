from __future__ import annotations
import html, json
from pathlib import Path
def build(case_dir,output):
 case=Path(case_dir); data=json.loads((case/"case.json").read_text(encoding="utf-8"))
 events=data.get("timeline",[]); evidence=data.get("evidence",[])
 cards=f"<div class='card'><b>{len(evidence)}</b><span>Evidence</span></div><div class='card'><b>{len(events)}</b><span>Events</span></div><div class='card'><b>{html.escape(data.get('status',''))}</b><span>Status</span></div>"
 rows="".join(f"<tr><td>{html.escape(str(x.get('time','')))}</td><td>{html.escape(str(x.get('type','')))}</td><td>{html.escape(str(x.get('detail','')))}</td></tr>" for x in events)
 doc=f"""<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>CyberIQ DFIR</title><style>body{{margin:auto;max-width:1100px;padding:32px;background:#070707;color:#eee;font:15px system-ui}}h1{{color:#ff3131}}.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}}.card{{background:#121212;border:1px solid #302020;padding:22px;border-radius:14px}}.card b,.card span{{display:block}}.card b{{font-size:24px;color:#ff5252}}table{{width:100%;margin-top:25px;border-collapse:collapse}}th,td{{padding:10px;border-bottom:1px solid #292929;text-align:left}}</style></head><body><h1>CyberIQ DFIR Lab</h1><p>Case: {html.escape(data.get('case',''))}</p><div class="grid">{cards}</div><table><tr><th>Time</th><th>Type</th><th>Detail</th></tr>{rows}</table></body></html>"""
 Path(output).write_text(doc,encoding="utf-8"); return Path(output)
