"""Export the policy manifest from RULES.md into policy-manifest.yaml.

RULES.md is the single source of truth. Never edit the exported YAML by hand:
edit the rules file, then run

    python tools/export_manifest.py

The script refuses to export if the tables and the manifest disagree, or if the
manifest uses a class other than allowed / approval / forbidden.

Requires PyYAML (pip install pyyaml).
"""
import pathlib, re, sys
import yaml

BASE = pathlib.Path(__file__).resolve().parent.parent
RULES = BASE / "RULES.md"
OUT = BASE / "policy-manifest.yaml"
VALID_CLASSES = {"allowed", "approval", "forbidden"}


def main():
    text = RULES.read_text(encoding="utf-8")
    blocks = re.findall(r"```yaml\n(.*?)```", text, re.S)
    if len(blocks) != 1:
        sys.exit(f"expected exactly one yaml block in {RULES.name}, found {len(blocks)}")
    block = blocks[0]
    manifest = yaml.safe_load(block)

    table_ids = set(re.findall(r"^\| ((?:SC|GN|GB|GA|HL|WP)-\d\d) \|", text, re.M))
    man_ids = set(manifest["rules"])
    problems = []
    if table_ids - man_ids:
        problems.append(f"in tables but not manifest: {sorted(table_ids - man_ids)}")
    if man_ids - table_ids:
        problems.append(f"in manifest but not tables: {sorted(man_ids - table_ids)}")
    bad = {k: v["class"] for k, v in manifest["rules"].items() if v["class"] not in VALID_CLASSES}
    if bad:
        problems.append(f"invalid classes: {bad}")
    if problems:
        sys.exit("REFUSED — fix RULES.md first:\n  " + "\n  ".join(problems))

    header = (
        "# GENERATED from RULES.md by tools/export_manifest.py — DO NOT EDIT BY HAND.\n"
        "# Edit RULES.md, then re-run the script.\n"
        "# If this file and RULES.md ever disagree, the stricter class wins.\n"
    )
    OUT.write_text(header + block, encoding="utf-8")

    counts = {}
    for v in manifest["rules"].values():
        counts[v["class"]] = counts.get(v["class"], 0) + 1
    print(f"exported {len(man_ids)} rules -> {OUT.relative_to(BASE)}  "
          f"(version {manifest['version']}, review by {manifest['review_by']})")
    print("  " + ", ".join(f"{k}: {counts[k]}" for k in sorted(counts)))


if __name__ == "__main__":
    main()
