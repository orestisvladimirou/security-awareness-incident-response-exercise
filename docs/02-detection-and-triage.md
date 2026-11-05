# 02 — Evidence-led detection and triage

## Facts, hypotheses and limitations

| Fact in fictional telemetry | Reasonable hypothesis | What is **not** proven |
| --- | --- | --- |
| Unusual vendor-linked identity login (EV-001) | Suspicious session or travel anomaly | Malicious actor or account takeover |
| Employee reports vendor-themed account request (EV-002) | Impersonation or social engineering | Click, credential entry, or causal relationship to login |
| 41 support ticket records read in nine minutes (EV-003) | Unauthorized bulk browsing | Export, exfiltration or data-breach notification requirement |
| Vendor export audit not supplied (EV-007) | Possible evidence retention/visibility weakness | That export occurred or did not occur |

The scenario must not equate **sign-in anomaly with compromise** or **ticket reads with extraction**. The mock service-desk email is an observation, not a phishing campaign actually delivered to anyone.

## First-hour triage procedure

1. Open a suspected incident, record analyst and normalized UTC timestamps and preserve original alert context.
2. Correlate identity session characteristics with the application's audit events, permissions, time zone, service use and authorized vendor activity.
3. Contact the employee through the **established** service-desk channel; do not ask them to forward secrets or browse the suspect site.
4. Obtain the vendor's approved security contact and request activity confirmation and full authorized session scope.
5. Document provisional severity and impacts separately from causes or conclusions.
6. Initiate containment *only with appropriate change/incident authority*, accounting for availability tradeoffs.
7. Preserve logs with collection metadata, tamper-evident storage, timestamps, legal hold/retention as applicable; **no such collection occurred here**.
8. Ask privacy/legal to evaluate notification duties only once sufficient personal-data facts are available; document any necessary time-sensitive escalation separately.

## Severity decision

The case is **SEV-2 provisional** due to possible customer-related access and a supplier identity. Severity is a local fictional rubric, not an industry certification or official regulatory threshold. Escalate if affected ticket content, export history, malicious account use, service disruption or wider privileged access is verified. Downgrade if authoritative records confirm an authorized benign session.

See [scenario events](../data/scenario_events.csv), [evidence register](../data/evidence_register.csv) and [decision log](../data/incident_decisions.csv).
