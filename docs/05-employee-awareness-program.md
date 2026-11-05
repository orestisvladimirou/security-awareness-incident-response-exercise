# 05 — Security-awareness and role-based learning plan

**Fictional learning programme design.** No employees have enrolled, received phishing simulations, taken a quiz or passed training. NIST SP 800-50 Revision 1 (September 2024) supports a life-cycle learning programme oriented toward behavior change and evaluation, not merely attendance.

## Learners and modules

| ID | Audience | Format | Behavior objective | Learning demonstration |
| --- | --- | --- | --- | --- |
| M-01 | All staff | 8-minute microlearning | Spot vendor impersonation and verify unexpected login prompts through known channels | Choose safe action in two examples |
| M-02 | Customer support and vendor management | 12-minute scenario | Respect least privilege and demand owner approval for access scope | Reject undocumented privilege escalation and record missing logs |
| M-03 | All staff | 8-minute microlearning | Report accidental clicks or credential disclosure rapidly and without fear | Provide concise fact-only report via trusted channel |
| M-04 | Managers and incident stakeholders | 12-minute scenario | Communicate uncertainty and approve recovery only after independent tests | Separate access observations from evidence of exfiltration and identify approval gate |

## Suggested materials

A staff message, [employee reporting template](../templates/employee-reporting-message.md), three safe simulated incident screenshots or plain-language cues from the fictional evidence, a short role-specific quiz, and an after-action review. **No real phishing messages should be sent or credentials collected** for this project.

### Core staff guidance

Unexpected vendor-branded messages may still be malicious. Do not use a link in an unexpected account-verification email. Look up the vendor through an already approved contact route and notify your internal security channel. If you clicked, entered a password or approved a login prompt, report it immediately; fast, accurate reporting is valued over blame.

### Knowledge assessment

Eight three-option questions and rationale are in [awareness_questions.csv](../data/awareness_questions.csv). For a future controlled course, target **7/8 correct** (at least 87.5%, satisfying the planned 80% mastery threshold), with feedback on missed objectives. Questions are example assessment items; no real learner results or pass rates exist.

### Measuring behavior, not attendance

Track time-to-report in a **consent-based future drill**, first-response accuracy, vendor access approvals, containment verification, clarity of incident updates, and independently re-tested corrective actions. Baselines in [learning_metrics.csv](../data/learning_metrics.csv) are **NOT MEASURED** and have no achieved values. Segment results carefully by role and sample size, avoid individual blame and limit handling of personal training data.

## 30/60/90-day proposed rollout

- **Days 0–30:** management approval, staff communications, baseline questionnaire, reporting-channel usability test.
- **Days 31–60:** deliver four modules and a voluntary, consent-based practice scenario; collect actual measurements before claiming outcomes.
- **Days 61–90:** audit selected vendor-access approvals, run a facilitated tabletop, measure reporting behavior and prioritize weak decisions for retraining.

This is an educational plan only. Any future real rollout needs organizational authorization, privacy consideration and accessible training materials.
