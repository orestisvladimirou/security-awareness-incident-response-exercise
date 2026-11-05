# 03 — Response playbook for vendor-linked account misuse

**A proposed procedure, not a performed containment or incident response.** NIST SP 800-61 Revision 3 frames incident response within CSF 2.0, with broad Govern/Identify/Protect preparation and Detect/Respond/Recover supported by continual improvement. This project uses those concepts rather than mislabeling the older Revision 2 lifecycle as the latest. See [sources](08-sources-and-limitations.md).

## Preparation and prerequisites

Maintain a tested 24/7 contact directory, identity/session inventory, service owner, legal/privacy contact, verified vendor security contact, emergency change authority, log retention requirements, and safe continuity fallback for the ticketing service.

## Detect / Analyze

Review sign-in provenance, approved access context, application logs and employee report. Keep all evidence UTC-aligned. Record what was observed, inferred and unavailable. Avoid unsupervised employee account searches and do not expose secrets in incident notes. Provisional risk level depends on customer content and actual access.

## Respond / Contain

Request authorized containment under the incident commander: suspend the affected identity, invalidate active sessions and refresh tokens, restrict vendor privileges, review any API keys/integrations separately, and preserve safe support-service fallback. Provider revocation semantics must be independently confirmed; **clicking an admin toggle does not prove all active access ended**. Record change authority and adverse service impact.

## Preserve, investigate and coordinate

Capture relevant time-bounded IdP and application activity through authorized channels. Record collector/time/asset/retrieval path, cryptographic digest if original evidence were collected, and access history. Ask the vendor about access paths, event completeness, ticket export, delegated permissions and provider-side evidence retention. Never invent evidence hashes for synthetic logs.

## Recover

Only restore access after the service owner and incident commander approve identity re-issuance, scoped permissions and witnessed failed unauthorized access tests. Validate monitoring, vendor use case and rollback plan. If an evidence gap persists, explicitly document conditional restrictions and senior risk decisions rather than guessing closure.

## Improve

Hold an actual after-action review **if an exercise is later run**, assign root causes to individuals/systems/processes, define correction vs systemic corrective action, and require independent effectiveness checks before signing closure. Training should be measured by reporting behavior and decisions, not solely attendance.

## Decision ownership

See [RACI](../data/roles_raci.csv), [decision log](../data/incident_decisions.csv) and [response action tracker](../data/response_actions.csv). Every simulated action remains **OPEN - SIMULATED**. No operational token invalidation, credential rotation, customer notification or actual employee training is claimed.
