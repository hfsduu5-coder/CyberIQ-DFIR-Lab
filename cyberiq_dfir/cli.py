import argparse, json
from pathlib import Path
from .core import evidence_record, summarize_log, write_json

def main():
 p=argparse.ArgumentParser(prog="cyberiq-dfir",description="CyberIQ local-first DFIR workbench")
 p.add_argument("--version",action="version",version="0.1.0"); sub=p.add_subparsers(dest="cmd",required=True)
 a=sub.add_parser("evidence"); a.add_argument("file"); a.add_argument("--output")
 a=sub.add_parser("analyze-log"); a.add_argument("file"); a.add_argument("--output")
 a=sub.add_parser("case-new"); a.add_argument("name")
 args=p.parse_args()
 if args.cmd=="evidence": data=evidence_record(args.file)
 elif args.cmd=="analyze-log": data=summarize_log(Path(args.file).read_text(encoding="utf-8",errors="replace"))
 else:
  root=Path("cases")/args.name; (root/"evidence").mkdir(parents=True,exist_ok=True); (root/"reports").mkdir(exist_ok=True)
  data={"case":args.name,"path":str(root),"status":"open"}
 if getattr(args,"output",None): write_json(data,args.output)
 print(json.dumps(data,indent=2))
if __name__=="__main__": main()
