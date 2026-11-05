# Security Awareness & Incident Response Exercise

**Independent cybersecurity portfolio project · v0.4 · 5 November 2026**

> **ENTIRELY FICTIONAL.** Aster Vale Services Ltd, its vendors, accounts, people, logs, messages, decisions, tabletop exercise, and outcomes are synthetic educational examples. No employee was trained, no live incident occurred, no system was accessed, and no organizational decisions were actually authorized. **The scenario is deliberately dated 18–20 November 2026 (future to project creation), not an event that has already happened.**

## What this project demonstrates

A fictional 45-person EU business uses an external customer-support provider. A suspicious sign-in to the provider's federated support identity is followed by unusual access to customer-support tickets. The security team must **detect, validate, contain, preserve evidence, coordinate with the vendor, recover with authorization, and learn** without assuming that an anomaly proves exfiltration. A complementary security-awareness programme prepares employees to recognize vendor impersonation and report suspicious activity quickly.

This is a **simulation of operational response and employee learning**, not a DORA/GDPR legal assessment, an ISO certification project, a SOC production exercise, or evidence of real incident-response employment. Privacy/regulatory assessment is deliberately a distinct unresolved decision gate referred to the appropriate specialists.

## Start here

1. [Organization, scenario, and guardrails](docs/01-scenario-and-scope.md)
2. [Detection and evidence-based triage](docs/02-detection-and-triage.md)
3. [Practical incident-response playbook](docs/03-response-playbook.md)
4. [Six-inject tabletop facilitator guide](docs/04-tabletop-facilitator-guide.md)
5. [Role-specific awareness programme and knowledge checks](docs/05-employee-awareness-program.md)
6. [Fictional after-action report and improvement backlog](docs/06-after-action-report.md)
7. [Executive summary](docs/07-executive-report.md)
8. [Official references and limitations](docs/08-sources-and-limitations.md)

## Core deliverables

| Area | v0.1 coverage | Critical limitation |
| --- | --- | --- |
| Incident chronology | 11 synthetic event/response rows | Not real telemetry; some inferences remain unconfirmed |
| Evidence register | 10 items including explicitly missing records | Integrity hashes are not authentic forensic chain-of-custody |
| Triage and decisions | 8 documented reasoning decisions | All proposed, none actually authorized |
| Operational response | 10 sequenced actions, with owners and proof tests | No action performed in a production system |
| Tabletop | 6 facilitator injects with expected decision points | Scenario scripted, not an exercise actually delivered |
| Awareness | 4 microlearning modules and 8 question checks | No employee attendance, testing or behavioral outcomes |
| Learning measurement | 6 planned metrics with unknown baseline | Targets are hypothetical, not achieved values |
| Excel companion | 8-sheet dashboard and working registers | CSV is authoritative; workbook is a versioned snapshot |
| Automation | Python standard-library integrity checks and tests | Validates dataset quality, not operational security |

## Key scenario facts

- **Case:** `IR-2026-001` — possible compromise of a third-party support account.
- **Proposed severity:** `SEV-2 provisional`, pending impact/exfiltration confirmation.
- **Evidence:** simulated sign-in anomaly and ticket reads; alleged customer-data export **not established**.
- **Containment:** token invalidation and provider-side access suspension are **proposed exercise decisions**, not actions actually taken.
- **Open gates:** vendor audit completeness, session scope, customer-data impact, authorization to restore, privacy/legal notification advice, and independent closure of corrective actions.

## Reproduce local quality checks

Requires Python 3.10+; the validator uses only the Python standard library.

```bash
python scripts/validate_project.py
python -m unittest discover -s tests -v
```

The spreadsheet and other deliverables are fictional training materials. Use [the local sources and limitations](docs/08-sources-and-limitations.md) and the published NIST guidance to adapt to a real organization. **Do not make public claims of genuine training delivery, forensic examination or incident handling.**

## Completed versioned phases

- **v0.1 — Original case baseline:** 11 events, 10 evidence references (4 absent), 8 unsigned decisions, 10 open actions, 6 tabletop injects, 4 training modules, 8 questions, 6 unmeasured learning KPIs and 8-sheet Excel workbook.
- **[v0.2 — Decision branches and evidence challenges](phase2/README.md):** 12 safe/unsafe branches, 8 evidence challenges, 6 scoring gates and 2 worked **model** tabletop answers. **No real tabletop took place.**
- **[v0.3 — Training and effectiveness design](phase3/README.md):** 24 fictional question responses across three constructed profiles, 4 unapproved module plans, 10 unclosed actions and 6 open lessons. **No employees participated.**
- **[v0.4 — Executive dashboard and quality review](phase4/README.md):** reconciled source metrics, incident/decision/action crosswalk, publication checks, reproducibility and current manifest.

### Final integrated summary

[Open the source-linked fictional executive dashboard](phase4/dashboard.md) and [the final portfolio quality report](phase4/docs/13-final-quality-review.md). The original workbook remains a **v0.1 snapshot**; the dashboard reflects the latest versioned CSVs.

### Repeat all validations

```sh
python scripts/validate_project.py
python scripts/validate_phase2.py
python scripts/validate_phase3.py
python scripts/validate_portfolio.py
python scripts/validate_workbook.py
python scripts/validate_manifest.py
python -m unittest discover -s tests -v
```

The generated model scores are **not employee assessments or incident-response outcomes**. There was **no real incident, exercise, training or approved remediation**, and ticket reads do not prove exfiltration. Keep this repository **private until its owner chooses to publish it**.
