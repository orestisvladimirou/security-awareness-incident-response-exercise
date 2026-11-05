# Phase 4 — Integrated portfolio dashboard and final review

**v0.4 · SIMULATION ONLY.**

The [executive dashboard](dashboard.md) joins the initial third-party incident-response exercise, six branch-based tabletop decision gates, eight evidence challenges, role-based learning activities and original unresolved corrective actions.

The [release and consistency review](docs/13-final-quality-review.md) records checks and remaining limitations. **All risk, exercise, learning and incident outcomes are synthetic**; no employee was trained or incident handled, and there is no authenticated evidence of exfiltration.

- [Metrics with provenance](data/portfolio_metrics.csv)
- [Incident decision traceability](data/incident_traceability.csv)
- [Worked tabletop scores](../phase2/data/illustrative_tabletop_answers.csv)
- [Worked training scores](../phase3/data/illustrative_training_scorecards.csv)

The Excel workbook `Security_Awareness_Incident_Response_v0.1.xlsx` is retained as the original snapshot and does not claim to sync to later CSVs. All other authoritative records are in versioned CSV files. Run `python scripts/validate_portfolio.py` and the repository's full test suite before release.
