import tempfile, unittest, json
from pathlib import Path
from cyberiq_dfir.core import sha256_file, extract_indicators, summarize_log
from cyberiq_dfir.timeline import parse_lines
from cyberiq_dfir.cases import new_case, add_evidence, note, set_status, load
from cyberiq_dfir.reporting import markdown_report, html_report, export_case
from cyberiq_dfir.plugins import names, run
from cyberiq_dfir.integrity import verify_case
from cyberiq_dfir.validation import validate_case
from cyberiq_dfir.chain import record as custody_record
from cyberiq_dfir.findings import add as finding_add

class CoreTests(unittest.TestCase):
 def test_hash(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/"x"; p.write_bytes(b"abc")
   self.assertEqual(sha256_file(p),"ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad")
 def test_indicators(self):\n  out=extract_indicators("src=10.0.0.1 invalid=999.999.999.999"); self.assertIn("10.0.0.1",out["ipv4"]); self.assertNotIn("999.999.999.999",out["ipv4"])
 def test_log(self): self.assertEqual(summarize_log("INFO ok\nERROR bad")["levels"]["ERROR"],1)
 def test_timeline(self): self.assertEqual(len(parse_lines("2026-10-03T10:00:00Z INFO start")),1)
 def test_case_lifecycle(self):
  with tempfile.TemporaryDirectory() as d:
   new_case("demo",d); case=Path(d)/"demo"; src=Path(d)/"e.log"; src.write_text("INFO demo")
   rec=add_evidence(case,src); self.assertEqual(len(rec["sha256"]),64)
   note(case,"reviewed"); set_status(case,"review")
   data=load(case); self.assertEqual(data["status"],"review"); self.assertEqual(len(data["evidence"]),1); self.assertTrue(verify_case(case)["verified"])
   self.assertTrue(validate_case(data)["valid"])
   custody_record(case,"review","tester","synthetic evidence"); finding_add(case,"Synthetic finding","low","e.log","training observation")
   data=load(case); self.assertEqual(len(data["chain_of_custody"]),1); self.assertEqual(data["findings"][0]["severity"],"low")
   self.assertIn("# demo",markdown_report("demo",data)); rendered=html_report("demo",data); self.assertIn("<!doctype html>",rendered); self.assertIn("Findings",rendered); self.assertIn("Evidence",rendered)
   out=export_case(data,case/"reports"/"case.html","html"); self.assertTrue(out.is_file())
 def test_case_name_safety(self):
  with tempfile.TemporaryDirectory() as d:
   with self.assertRaises(ValueError): new_case("../escape",d)
 def test_tamper_detection(self):
  with tempfile.TemporaryDirectory() as d:
   new_case("demo",d); case=Path(d)/"demo"; src=Path(d)/"e.log"; src.write_text("original")
   rec=add_evidence(case,src); (case/rec["path"]).write_text("changed")
   self.assertFalse(verify_case(case)["verified"])
 def test_duplicate_evidence(self):
  with tempfile.TemporaryDirectory() as d:
   new_case("demo",d); case=Path(d)/"demo"; src=Path(d)/"e.log"; src.write_text("same")
   add_evidence(case,src)
   with self.assertRaises(ValueError): add_evidence(case,src)
 def test_plugins(self):
  self.assertIn("indicators",names()); self.assertIn("1.2.3.4",run("indicators","1.2.3.4")["ipv4"])
if __name__=="__main__": unittest.main()
