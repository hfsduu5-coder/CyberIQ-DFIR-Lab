import argparse, json
from pathlib import Path
from .core import evidence_record, summarize_log, write_json
from .cases import new_case, add_evidence, note, set_status, load
from .timeline import parse_lines
from .reporting import export_case
from .dashboard import build as build_dashboard
from .plugins import names as plugin_names, run as plugin_run
from .integrity import verify_case
from .validation import validate_case
from .chain import record as custody_record, history as custody_history
from .findings import add as finding_add, list_findings

def emit(data): print(json.dumps(data,indent=2))
def main():
 p=argparse.ArgumentParser(prog="cyberiq-dfir",description="CyberIQ local-first DFIR workbench")
 p.add_argument("--version",action="version",version="1.0.0"); s=p.add_subparsers(dest="cmd",required=True)
 q=s.add_parser("evidence"); q.add_argument("file"); q.add_argument("--output")
 q=s.add_parser("analyze-log"); q.add_argument("file"); q.add_argument("--output")
 q=s.add_parser("timeline"); q.add_argument("file"); q.add_argument("--output")
 q=s.add_parser("case-new"); q.add_argument("name")
 q=s.add_parser("case-add"); q.add_argument("case"); q.add_argument("file")
 q=s.add_parser("case-note"); q.add_argument("case"); q.add_argument("text")
 q=s.add_parser("case-status"); q.add_argument("case"); q.add_argument("status",nargs="?")
 q=s.add_parser("case-export"); q.add_argument("case"); q.add_argument("output"); q.add_argument("--format",choices=["json","md","html"],default="html")
 q=s.add_parser("dashboard"); q.add_argument("case"); q.add_argument("--output",default="dfir-dashboard.html")
 q=s.add_parser("case-verify"); q.add_argument("case")
 q=s.add_parser("case-validate"); q.add_argument("case")
 q=s.add_parser("custody-add"); q.add_argument("case"); q.add_argument("action"); q.add_argument("--actor",default="analyst"); q.add_argument("--detail",default="")
 q=s.add_parser("custody-list"); q.add_argument("case")
 q=s.add_parser("finding-add"); q.add_argument("case"); q.add_argument("title"); q.add_argument("--severity",default="info"); q.add_argument("--evidence",default=""); q.add_argument("--observation",default="")
 q=s.add_parser("finding-list"); q.add_argument("case")
 q=s.add_parser("plugin-list")
 q=s.add_parser("plugin-run"); q.add_argument("name"); q.add_argument("file")
 a=p.parse_args()
 if a.cmd=="evidence": data=evidence_record(a.file)
 elif a.cmd=="analyze-log": data=summarize_log(Path(a.file).read_text(encoding="utf-8",errors="replace"))
 elif a.cmd=="timeline": data=parse_lines(Path(a.file).read_text(encoding="utf-8",errors="replace"),Path(a.file).name)
 elif a.cmd=="case-new": data=new_case(a.name)
 elif a.cmd=="case-add": data=add_evidence(a.case,a.file)
 elif a.cmd=="case-note": data=note(a.case,a.text)
 elif a.cmd=="case-status": data=set_status(a.case,a.status) if a.status else load(a.case)
 elif a.cmd=="case-export": export_case(load(a.case),a.output,a.format); data={"output":a.output,"format":a.format}
 elif a.cmd=="dashboard": build_dashboard(a.case,a.output); data={"output":a.output}
 elif a.cmd=="case-verify": data=verify_case(a.case)
 elif a.cmd=="case-validate": data=validate_case(load(a.case))
 elif a.cmd=="custody-add": data=custody_record(a.case,a.action,a.actor,a.detail)
 elif a.cmd=="custody-list": data={"chain_of_custody":custody_history(a.case)}
 elif a.cmd=="finding-add": data=finding_add(a.case,a.title,a.severity,a.evidence,a.observation)
 elif a.cmd=="finding-list": data={"findings":list_findings(a.case)}
 elif a.cmd=="plugin-list": data={"plugins":plugin_names()}
 else: data=plugin_run(a.name,Path(a.file).read_text(encoding="utf-8",errors="replace"))
 if getattr(a,"output",None) and a.cmd in ("evidence","analyze-log","timeline"): write_json(data,a.output)
 emit(data)
if __name__=="__main__": main()
