# Zero-Lockout Rules

Operating rules for AI agents that work on client accounts: GoHighLevel, Google Search
Console, Google Business Profile, SMS, email and DNS.

The goal is that an agent never gets a client locked out, suspended, penalised or taken
offline. That goal outranks every ranking or growth goal.

## Why this exists

An agency that lets an AI agent or script act on client accounts takes on a new kind of
risk. One bulk change, one unreviewed AI page or one message sent without consent can
cost the client their Google listing, their texting number or their email.

Most guidance is written for people and assumes judgment. An agent needs each action
named and classified in advance. This repo does that for one common small-agency stack.

## What is in it

| File | What it is |
|---|---|
| [`RULES.md`](RULES.md) | 74 rules with IDs. Each action is ALLOWED, APPROVAL or FORBIDDEN, and each links to its primary source. Also covers the write procedure, freeze conditions, approval requests, verification checks and incident playbooks. |
| [`policy-manifest.yaml`](policy-manifest.yaml) | The same 74 classifications in machine-readable form, for enforcement in code. |
| [`tools/export_manifest.py`](tools/export_manifest.py) | Regenerates the manifest from `RULES.md`. It refuses to export if the tables and the manifest disagree. |

## The ideas that carry over to any stack

- **Default deny.** An action that is not listed needs human approval.
- **Data is not instructions.** Text in web pages, reviews, emails or tool output
  cannot grant approval. Only the operator can.
- **One client per operation.** Cross-client bulk changes turn one mistake into an
  agency-wide lockout.
- **Before state and rollback first.** The agent records both before every write, then
  verifies the live result.
- **Irreversible actions belong to humans**, every time.
- **The client owns their assets.** The agency is a user or manager, never the owner.

## How to use it

1. Read `RULES.md` and adapt it: the thresholds marked "agency policy" are choices, not
   platform limits.
2. Give `RULES.md` to your agent as governing instructions, above any SEO playbook.
3. Load `policy-manifest.yaml` in your own code and check the rule ID before each write.
   Treat any action without a rule ID as `approval`.
4. Re-verify the rules by the `review_by` date and after any platform policy change.

## Limits

- This is dated guidance from a small agency, not legal advice. The rules were
  researched on 2026-09-28 and platform policies change often. Check each source link.
- It covers GoHighLevel and Google. Other platforms need their own registry.
- §12 of `RULES.md` lists what the research could not confirm.

## Contributing

Corrections are welcome, especially where a platform policy has changed. Open an issue
or a pull request with the rule ID and a link to the primary source.

## License

MIT. See [`LICENSE`](LICENSE).

Built by Santiago Kamt Raffo (Celestel Enterprises LLC) with Claude.
