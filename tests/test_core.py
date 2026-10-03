import tempfile, unittest, json
from pathlib import Path
from cyberiq_dfir.core import sha256_file, extract_indicators, summarize_log
from cyberiq_dfir.timeline import parse_lines
from cyberiq_dfir.cases import new_case, add_evidence, note, set_status, load
from cyberiq_dfir.reporting import markdown_report, html_report
from cyberiq_dfir.plugins import names, run
from cyberiq_dfir.integrity import verify_case

class CoreTests(unittest.TestCase):
 def test_hash(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/"x"; p.write_bytes(b"abc")
   self.assertEqual(sha256_file(p),"ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad")
 def test_indicators(self): self.assertIn("10.0.0.1",extract_indicators("src=10.0.0.1")["ipv4"])
 def test_log(self): self.assertEqual(summarize_log("INFO ok\nERROR bad")["levels"]["ERROR"],1)
 def test_timeline(self): self.assertEqual(len(parse_lines("2026-10-03T10:00:00Z INFO start")),1)
 def test_case_lifecycle(self):
  with tempfile.TemporaryDirectory() as d:
   new_case("demo",d); case=Path(d)/"demo"; src=Path(d)/"e.log"; src.write_text("INFO demo")
   rec=add_evidence(case,src); self.assertEqual(len(rec["sha256"]),64)
   note(case,"reviewed"); set_status(case,"review")
   data=load(case); self.assertEqual(data["status"],"review"); self.assertEqual(len(data["evidence"]),1); self.assertTrue(verify_case(case)["verified"])
   self.assertIn("# demo",markdown_report("demo",data)); self.assertIn("<!doctype html>",html_report("demo",data))
 def test_plugins(self):
  self.assertIn("indicators",names()); self.assertIn("1.2.3.4",run("indicators","1.2.3.4")["ipv4"])
if __name__=="__main__": unittest.main()
