# 10 — Evidence challenge register and uncertainty gates

Every exercise decision should cite a relevant piece of [fictional evidence](../../data/evidence_register.csv), identify its provenance and distinguish observations from inferred harm.

| Test | Known in scenario | Unproven / needs evidence |
| --- | --- | --- |
| Identity anomaly | Invented unfamiliar sign-in alert | Legitimate context, session integrity, actual compromise |
| Employee message | Invented vendor-branded unexpected email | Whether the recipient clicked or entered any credential |
| Support app | Invented 41 ticket reads in nine minutes | Export, exfiltration, affected data categories, purpose |
| Containment | Draft suspension request | Authorization, provider action, revocation, business fallback |
| Privacy | Incomplete assessment material | Scope, individuals, risk assessment and reporting decision |
| Recovery | Draft improvement notes only | Clean access and business approval, measured control effectiveness |

Eight actionable evidence questions are linked by control owner in [the evidence challenge register](../data/evidence_challenges.csv). Data exported by a provider must not be assumed trustworthy or complete before source authentication and collection metadata are recorded.

**No hashes, timestamps or chain-of-custody assertions here represent real forensics.** This exercise may use invented data to model decision quality, but must never claim evidence of confirmed exfiltration, real suspension, signed approval or training success.
