# SME Cybersecurity Mitigation Strategy Framework

## Purpose

This framework defines how recommended cybersecurity controls will be selected for the risks identified in the SME risk assessment.

## Mitigation Process

Risk
→ Identify Vulnerability
→ Select Security Control
→ Map Control to NIST CSF
→ Define Expected Effect
→ Reassess Residual Risk

## Control Selection Principles

Security controls should:

1. Address the identified vulnerability.
2. Be appropriate for the size and resources of an SME.
3. Reduce the likelihood and/or potential impact of the risk.
4. Be practical to implement.
5. Support the relevant NIST CSF functions.
6. Allow the risk to be reassessed after implementation.

## Risk Treatment Approach

The primary treatment approach in this project is risk reduction through appropriate cybersecurity controls.

Residual risk will be reassessed after the recommended controls are applied.

## R-001 — Phishing

### Identified Vulnerability

Lack of employee awareness and inconsistent multi-factor authentication.

### Recommended Controls

- Security awareness training
- Multi-factor authentication (MFA)
- Email filtering

### NIST CSF Mapping

Protect / Detect / Respond

### Expected Effect

These controls are intended to reduce the likelihood of successful phishing-based account compromise by improving employee awareness, strengthening authentication, and filtering suspicious messages.

### Residual Risk

The expected residual likelihood is reduced from 5 (Very High) to 2 (Low), while the potential impact remains 4 (High).

Residual Risk Score:

**2 × 4 = 8 — Moderate**

## R-002 — Ransomware

### Identified Vulnerability

Backup restoration is not regularly tested.

### Recommended Controls

- Regular backup restoration testing
- Offline or isolated backups
- Endpoint protection
- Patch management

### NIST CSF Mapping

Protect / Respond / Recover

### Expected Effect

These controls are intended to reduce the likelihood and potential operational impact of ransomware by strengthening endpoint protection, reducing exposure to exploitable vulnerabilities, and improving the organization's ability to restore affected data.

### Residual Risk

The expected residual likelihood is reduced from 4 (High) to 2 (Low), while the potential impact remains 5 (Very High).

### Residual Risk Score

**2 × 5 = 10 — High**

---

## R-003 — Insider Threat

### Identified Vulnerability

Excessive access privileges and limited monitoring of user activity.

### Recommended Controls

- Role-Based Access Control (RBAC)
- Least-privilege access
- Access logging and monitoring
- Periodic access reviews

### NIST CSF Mapping

Govern / Protect / Detect

### Expected Effect

These controls are intended to reduce the opportunity for misuse of legitimate access by limiting unnecessary privileges, reviewing access regularly, and improving visibility into suspicious user activity.

### Residual Risk

The expected residual likelihood is reduced from 3 (Moderate) to 2 (Low), while the potential impact is reduced from 4 (High) to 3 (Moderate) through improved access control and monitoring.

### Residual Risk Score

**2 × 3 = 6 — Moderate**

---

## R-004 — Weak Authentication

### Identified Vulnerability

Inconsistent multi-factor authentication and potential password reuse.

### Recommended Controls

- Multi-Factor Authentication (MFA)
- Strong password policy
- Password manager
- Account monitoring

### NIST CSF Mapping

Govern / Protect / Detect

### Expected Effect

These controls are intended to strengthen account security, reduce the likelihood of credential-based compromise, and improve detection of suspicious account activity.

### Residual Risk

The expected residual likelihood is reduced from 4 (High) to 2 (Low), while the potential impact remains 4 (High).

### Residual Risk Score

**2 × 4 = 8 — Moderate**

---

## R-005 — Unpatched Software

### Identified Vulnerability

There is no formal vulnerability-management process for identifying, prioritizing, and tracking software vulnerabilities.

### Recommended Controls

- Centralized patch management
- Vulnerability scanning
- Software inventory
- Patch prioritization

### NIST CSF Mapping

Identify / Protect / Detect

### Expected Effect

These controls are intended to improve visibility of vulnerable systems, prioritize security updates, reduce exposure to known vulnerabilities, and detect weaknesses before they are exploited.

### Residual Risk

The expected residual likelihood is reduced from 4 (High) to 2 (Low), while the potential impact remains 4 (High).

### Residual Risk Score

**2 × 4 = 8 — Moderate**

---

## R-006 — Data Breach

### Identified Vulnerability

Multiple potential attack paths, including compromised accounts and vulnerable systems.

### Recommended Controls

- Data access controls
- Multi-Factor Authentication (MFA)
- Encryption
- Security monitoring
- Incident response procedures

### NIST CSF Mapping

Identify / Protect / Detect / Respond

### Expected Effect

These controls are intended to reduce unauthorized access to sensitive information, improve visibility into suspicious activity, and strengthen the organization's ability to respond to a potential data breach.

### Residual Risk

The expected residual likelihood is reduced from 3 (Moderate) to 2 (Low), while the potential impact remains 5 (Very High).

### Residual Risk Score

**2 × 5 = 10 — High**
