# Incident Response & Awareness — Executive Simulation Dashboard

> **FULLY FICTIONAL TRAINING EXERCISE — NO INCIDENT, LIVE ATTACK, EXFILTRATION, REAL TABLETOP, EMPLOYEE TRAINING OR MANAGEMENT APPROVAL OCCURRED.** All involved entities and artifacts are invented; case events are modeled as **18–20 November 2026**, after the repository's 5 November 2026 preparation date. Outcomes below are design metrics, not proof of operating controls.

## Case assessment

| Topic | Current assessment | Evidence boundary |
| --- | --- | --- |
| Third-party support sign-in | Suspicious / require investigation | Unfamiliar sign-in alone is not confirmed compromise |
| Employee vendor-message report | Reported in synthetic narrative | No established credential input or link click |
| Customer-support ticket reads | **41 reads in nine minutes**, in a made-up audit record | **Export, exfiltration, content and affected users remain unverified** |
| Proposed severity | SEV-2 provisional | Must be authorized and adjusted as facts change |
| Identity/vendor containment | Proposed and unsigned | No actual revocation or service interruption |
| Privacy/regulatory decision | Specialist review gate | Not evaluated or reported in this project |
| Recovery and corrective actions | **10 still open** | Independent effectiveness evidence absent |

## Exercise design and evidence coverage

| Record class | Count | Meaning |
| --- | ---: | --- |
| Fictional incident events | **11** | Ordered scenario events, not real SIEM export |
| Evidence records | **10** | **4 missing** and 6 simulated placeholders |
| Incident response proposals | **8** | Every decision remains unsigned |
| Response and treatment actions | **10** | None verified or approved as completed |
| Original tabletop injects | **6** | Design only, never administered |
| Illustrative branch choices | **12** | Two per inject; safe versus unsafe decisions |
| Evidence validation challenges | **8** | Questions for future authorized collection |
| Open lessons | **6** | No operational fixes demonstrated |

## Worked response scoring — not participants

The [tabletop decision guide](../phase2/docs/09-tabletop-decision-guide.md) defines a 0/1/2 rubric. Two deliberately constructed model answers illustrate scoring: **MODEL-EVIDENCE-LED 12/12**; **MODEL-RUSHED 2/12**. These numbers represent **answer-key demonstrations, not people, measured incident response speed, or real organizational readiness.** The proposed safe actions require evidence, authorization and independent verification.

## Awareness learning — not employees

Four modules and eight original questions were designed. Three constructed example answer sheets score **8/8, 6/8 and 3/8**, illustrating how topic-level coaching would work. They are **not employee test results** and cannot be used to compute a real pass rate. Six planned learning KPIs still have **zero measured baselines**. See [learning evaluation](../phase3/docs/11-learning-evaluation.md) and [model scorecards](../phase3/data/illustrative_training_scorecards.csv).

## Priority management decisions for a future authorized exercise

1. Assign an incident commander and vendor liaison with a safe customer-support fallback.
2. Obtain source-authenticated identity session/export audit logs before claiming data theft or absence of impact.
3. Require formal approvals for temporary vendor access restrictions, preservation and restoration.
4. Refer personal-data impact and possible notifications to a qualified privacy/legal decision-maker.
5. Run a consent-based tabletop and accessible role-specific learning pilot before collecting performance indicators.
6. Independently test remediation and evidence of changed behavior before declaring an action closed.

## Dashboard integrity

[Data provenance](data/portfolio_metrics.csv) · [Incident-decision crosswalk](data/incident_traceability.csv) · [Final quality review](docs/13-final-quality-review.md) · [Original case summary](../docs/07-executive-report.md)

All counts are source-validated by standard-library Python checks. The 8-sheet [original Excel workbook](../Security_Awareness_Incident_Response_v0.1.xlsx) remains a **v0.1 snapshot**, not an automatically refreshed live dashboard or evidence of incident-handling outcomes.
