"""Bilgi tabanını resmî kaynaklardan baştan üretir ve tüm doğrulamaları çalıştırır.

Sıra: build_curriculum → build_skills → enrich_learning_outcomes → build_concepts → build_prerequisites → build_formulas → build_question_families → build_osym → build_market → build_pedagogy
      → validate_curriculum → validate_graphs
Herhangi bir adım hata verirse durur ve çıkış kodu 1 döner.
"""
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
STEPS = ["build_curriculum.py", "build_skills.py", "enrich_learning_outcomes.py", "build_concepts.py",
         "build_prerequisites.py", "build_formulas.py", "build_question_families.py", "build_osym.py", "build_market.py", "build_pedagogy.py", "validate_curriculum.py", "validate_graphs.py"]

for step in STEPS:
    print(f"\n=== {step} ===", flush=True)
    r = subprocess.run([sys.executable, str(HERE / step)], cwd=HERE, stderr=subprocess.DEVNULL)
    if r.returncode != 0:
        print(f"\n✗ {step} başarısız (çıkış kodu {r.returncode})")
        sys.exit(1)
print("\n✓ Tüm adımlar başarılı")
