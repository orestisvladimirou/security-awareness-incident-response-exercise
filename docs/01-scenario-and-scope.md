# 01 — Scenario, scope, and safety boundaries

**COMPLETELY FICTIONAL CASE STUDY.** The scenario date (18 November 2026) and tabletop date (20 November 2026) are future hypothetical dates as of authorship (5 November 2026). No live vendor, customer, compromised identity or security event exists.

## Organization and service

Aster Vale Services Ltd is an imaginary 45-person EU software-services business. It relies on **Cedarline Support Services**, a fictional external provider, for limited customer support ticket triage. A service account is not involved in the main alert; the suspicious identity is a **vendor-linked human support identity** federated through a cloud identity provider. Customer ticket metadata can include contact details, so unauthorized reads may raise privacy concerns, but the available mock data do **not** show content export.

The identity can view a restricted customer-support workspace. The exercise assumes no local administrative shell access, payment processing privileges or access to other tenants. Any new discovery may require an updated blast-radius assessment.

## Initial detection question

A synthetic sign-in from an unfamiliar network occurs at 08:40Z. At 08:46Z, an employee reports a suspicious vendor-branded verification message. At 08:53Z, the support application shows unusual ticket reads. These facts are **correlated indicators, not proof that the employee visited the link, credential theft occurred, an attacker used the account, or data was exfiltrated**.

## Mission and scope

The exercise covers identity security triage, third-party support coordination, evidence handling, incident-command approvals, business continuity tradeoffs, end-user reporting, follow-up learning metrics and root-cause questions. It deliberately **does not carry out** phishing, credential harvesting, account access, penetration testing, vendor contact, security-product changes, messages to real employees, or regulator notifications.

Data includes no real passwords, production endpoints, personal identifiers, or operational secrets. All characters and vendor names are invented.

## Desired outputs

- A fact-versus-hypothesis incident chronology and eight provisional decisions.
- A safe response playbook with containment/recovery gates.
- A six-inject tabletop *script*, not a falsely claimed delivered exercise.
- An awareness learning plan with eight objective questions and measurable targets.
- An after-action improvement backlog with **open/unverified** actions.

Privacy and regulatory matters are referred to a separate qualified review; no reporting conclusion is fabricated. The project complements the other GRC case studies by focusing on actual response operations and **human factors** rather than certifying the fictional company.
