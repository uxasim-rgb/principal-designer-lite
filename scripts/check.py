"""Checks that this repository holds exactly one installable skill with a valid header.

Run: python scripts/check.py
"""
import pathlib, re, sys
import yaml

root = pathlib.Path(__file__).resolve().parent.parent
errors = []
skills = [p for p in root.rglob("SKILL.md") if "evals" not in p.parts and ".git" not in p.parts]
if len(skills) != 1:
    errors.append(f"expected exactly one SKILL.md, found {len(skills)}")
for p in skills:
    text = p.read_text(encoding="utf-8").replace("\r\n", "\n")
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append(f"{p.name}: no frontmatter")
        continue
    try:
        fm = yaml.safe_load(m.group(1))
    except yaml.YAMLError as e:
        errors.append(f"{p.name}: invalid YAML: {str(e).splitlines()[0]}")
        continue
    if fm.get("name") != "principal-designer-lite":
        errors.append(f"{p.name}: name is {fm.get('name')!r}")
    d = fm.get("description") or ""
    if not d or len(d) > 1024:
        errors.append(f"{p.name}: description must be 1 to 1024 characters, is {len(d)}")
    for link in re.findall(r"`((?:references|catalogs|examples)/[\w.-]+\.md)`", text):
        if not (root / link).exists():
            errors.append(f"{p.name}: points to {link}, which does not exist")
for e in errors:
    print("FAIL", e)
if errors:
    sys.exit(1)
print("ok: one skill, valid header, all referenced files exist")
