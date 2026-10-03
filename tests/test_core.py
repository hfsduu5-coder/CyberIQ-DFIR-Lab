import tempfile, unittest
from pathlib import Path
from cyberiq_dfir.core import sha256_file, extract_indicators, summarize_log
class CoreTests(unittest.TestCase):
 def test_hash(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/"x"; p.write_bytes(b"abc")
   self.assertEqual(sha256_file(p),"ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad")
 def test_indicators(self): self.assertIn("10.0.0.1",extract_indicators("src=10.0.0.1")["ipv4"])
 def test_log(self): self.assertEqual(summarize_log("INFO ok\nERROR bad")["levels"]["ERROR"],1)
if __name__=="__main__": unittest.main()
