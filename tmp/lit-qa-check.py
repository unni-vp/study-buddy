from pathlib import Path
p=Path('scripts/check_biology_qa.cjs');s=p.read_text();s=s.replace(".count()!==6)",".count()!==Number(process.argv[4]||6))");p.write_text(s)
