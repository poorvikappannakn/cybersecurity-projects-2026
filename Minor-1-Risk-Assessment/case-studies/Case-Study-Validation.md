# Case Study Validation

## Purpose

The risk assessment framework is validated by applying it to different fictional SME environments.

The purpose of the validation is to determine whether the framework can identify and prioritize cybersecurity risks across businesses with different assets, operations, and security requirements.

## Validation Approach

Each case study follows the same assessment process:

1. Define the business environment.
2. Identify critical assets.
3. Identify relevant threats.
4. Identify vulnerabilities.
5. Assess likelihood.
6. Assess impact.
7. Calculate risk score.
8. Classify risk.
9. Map risks to relevant NIST CSF Functions.
10. Recommend mitigation controls.
11. Reassess residual risk.

The scoring methodology remains unchanged across all case studies.

---

# Case Study 1 — Retail & E-commerce SME

## Business Profile

**Business Type:** Small Retail & E-commerce Business  
**Employees:** 15  
**Operations:** Physical retail store and online e-commerce platform

## Critical Assets

1. Customer information
2. E-commerce platform
3. Payment/POS systems
4. Employee accounts
5. Business laptops
6. Business documents
7. Internal network

## Baseline Security Posture

- Basic endpoint protection is deployed.
- Password-based authentication is used for business accounts.
- Multi-factor authentication (MFA) is not consistently enabled.
- Basic access controls are in place.
- Security awareness training is informal.
- Business backups are maintained.
- There is no dedicated cybersecurity team.
- Centralized security monitoring is limited.

## Assessment Objective

The framework is applied to determine whether it can identify and prioritize risks associated with customer information, online services, authentication, payment-related systems, and employee access.

## Source Basis

The business scenario is fictional and the business characteristics are project assumptions.

NIST guidance was used to inform the types of cybersecurity considerations relevant to small businesses and e-commerce environments, particularly authentication, MFA, and logging.

NIST's e-commerce guidance demonstrates the relevance of stronger authentication and authentication-related logging in online retail environments.

---

# Case Study 2 — Small IT Services Company

## Business Profile

**Business Type:** Small IT Services Company  
**Employees:** 20  
**Operations:** Provides technical support, software services, cloud administration, and IT consulting to business clients.

## Critical Assets

1. Client information
2. Employee accounts
3. Administrative accounts
4. Cloud services
5. Source code and technical documentation
6. Company laptops
7. Client credentials and configuration information
8. Internal network

## Baseline Security Posture

- Endpoint protection is deployed on company laptops.
- Password-based authentication is widely used.
- MFA is enabled for some critical services but is not consistently enforced.
- Employees have access to multiple cloud-based services.
- Administrative privileges are limited but not regularly reviewed.
- Security monitoring is limited.
- Software and system updates are performed but are not centrally tracked.
- There is no dedicated internal security team.

## Assessment Objective

The framework is applied to determine whether it can identify and prioritize risks associated with privileged accounts, cloud services, client information, administrative access, software vulnerabilities, and employee devices.

## Expected Risk Characteristics

Because the company provides IT services and may hold client credentials and administrative access, compromise of an employee or administrative account could potentially affect both the company and its clients.

The case study therefore provides an opportunity to evaluate whether the framework appropriately prioritizes risks involving:

- Privileged access
- Weak authentication
- Cloud account compromise
- Unpatched systems
- Insider misuse
- Client information exposure

## Source Basis

The business scenario is fictional and the business characteristics are project assumptions.

NIST's small-business guidance emphasizes that cybersecurity risk management should be adapted to an organization's size, resources, environment, and requirements. This case study applies that principle to an IT-services environment.

---

# Case Study 3 — Small Healthcare / Clinic Business

## Business Profile

**Business Type:** Small Healthcare Clinic  
**Employees:** 18  
**Operations:** Provides outpatient healthcare services and maintains electronic patient records.

## Critical Assets

1. Patient information
2. Electronic health records
3. Employee accounts
4. Clinical workstations
5. Medical and administrative systems
6. Backup systems
7. Internal network
8. Telehealth or online communication systems

## Baseline Security Posture

- Endpoint protection is deployed.
- Password-based authentication is used.
- MFA is not consistently enabled across all accounts.
- Access to patient information is role-based but access reviews are irregular.
- Backups are maintained.
- Security awareness training is provided informally.
- Software updates are performed but are not centrally managed.
- There is no dedicated cybersecurity team.

## Assessment Objective

The framework is applied to determine whether it can identify and prioritize risks associated with patient information, electronic health records, employee accounts, clinical workstations, and healthcare-related systems.

## Expected Risk Characteristics

Healthcare environments can have significant confidentiality, integrity, and availability requirements because cybersecurity incidents can affect sensitive patient information and clinical operations.

The case study therefore provides an opportunity to evaluate whether the framework appropriately prioritizes risks involving:

- Patient information exposure
- Ransomware
- Unauthorized access
- Weak authentication
- Unpatched clinical systems
- Backup and recovery

## Source Basis

The business scenario is fictional and the business characteristics are project assumptions.

NIST provides healthcare-specific cybersecurity resources addressing electronic health information and cybersecurity practices for small healthcare organizations. These resources were used to inform the types of assets and cybersecurity considerations included in this scenario.

---

# Cross-Case Validation

The same risk assessment methodology is applied to all three businesses.

The framework does not change its scoring rules based on the business type.

Instead, the business environment changes:

**Business Type**
→ **Assets**
→ **Threats**
→ **Vulnerabilities**
→ **Risk Priorities**

This allows the framework to be evaluated for adaptability across different SME environments.

## Validation Criteria

The framework will be considered useful if it:

1. Identifies risks relevant to each business.
2. Produces different risk priorities when business assets and vulnerabilities differ.
3. Provides a consistent and repeatable scoring process.
4. Maps identified risks to relevant NIST CSF Functions.
5. Produces practical mitigation recommendations.
6. Allows residual risk to be reassessed after mitigation.
7. Remains understandable and practical for an SME environment.

## Important Assumption

All three businesses described in this document are fictional scenarios created for project validation.

Business characteristics, risk scores, likelihood values, impact values, and residual-risk values used later in the assessment are project assumptions unless explicitly supported by an external source.

---

# Validation Results

## Comparative Risk Assessment

The same 1–5 likelihood and 1–5 impact methodology is applied to each case study.

| Case Study | Primary Risk | Likelihood | Impact | Initial Risk | Risk Level | Residual Risk | Residual Level |
|---|---|---:|---:|---:|---|---:|---|
| Retail & E-commerce | Unauthorized account access | 4 | 5 | 20 | Critical | 10 | High |
| IT Services | Privileged account compromise | 4 | 5 | 20 | Critical | 10 | High |
| Healthcare / Clinic | Ransomware | 4 | 5 | 20 | Critical | 10 | High |

## Validation Observation

The framework is expected to produce different risk priorities across the three businesses because their assets, operations, vulnerabilities, and security requirements differ.

The scoring methodology itself remains unchanged.

Detailed risk assessments for each case study will be documented below.

## Case Study Risk Assessments

### Retail & E-commerce

#### Primary Risk Assessment

**Asset:** Customer information and e-commerce customer accounts

**Threat:** Unauthorized account access

**Vulnerability:** Inconsistent multi-factor authentication and weak authentication practices

**Existing Controls:**

- Password authentication
- Basic access controls
- Basic endpoint protection
- MFA is not consistently enabled

**Likelihood:** 4 — High

**Impact:** 5 — Very High

**Initial Risk Score:**

**4 × 5 = 20 — Critical**

#### NIST CSF Mapping

Protect / Detect / Respond

#### Recommended Controls

- Multi-factor authentication (MFA)
- Strong authentication and password controls
- Account monitoring
- Access controls
- Security logging

#### Expected Effect

The recommended controls are intended to reduce the likelihood of unauthorized account access by strengthening authentication, improving access control, and increasing visibility into suspicious account activity.

#### Residual Risk

The expected residual likelihood is reduced from 4 (High) to 2 (Low), while the potential impact remains 5 (Very High).

#### Residual Risk Score

**2 × 5 = 10 — High**

#### Validation Result

The framework identified unauthorized account access as a high-priority risk in this e-commerce environment. The result demonstrates that the framework can prioritize risks based on the specific assets and exposure of the business rather than applying identical priorities to every SME.


### IT Services

#### Primary Risk Assessment

**Asset:** Administrative accounts and client systems

**Threat:** Privileged account compromise

**Vulnerability:** MFA is not consistently enforced and administrative access is not regularly reviewed

**Existing Controls:**

- Endpoint protection
- Password-based authentication
- Limited administrative access controls
- MFA enabled for some critical services
- Limited security monitoring

**Likelihood:** 4 — High

**Impact:** 5 — Very High

**Initial Risk Score:**

**4 × 5 = 20 — Critical**

#### NIST CSF Mapping

Govern / Protect / Detect / Respond

#### Recommended Controls

- Mandatory MFA for administrative accounts
- Role-Based Access Control (RBAC)
- Least-privilege access
- Privileged account monitoring
- Periodic access reviews
- Security logging

#### Expected Effect

The recommended controls are intended to reduce the likelihood of privileged account compromise by strengthening authentication, limiting unnecessary administrative privileges, and improving monitoring of high-risk accounts.

#### Residual Risk

The expected residual likelihood is reduced from 4 (High) to 2 (Low), while the potential impact remains 5 (Very High).

#### Residual Risk Score

**2 × 5 = 10 — High**

#### Validation Result

The framework identified privileged account compromise as a critical risk in the IT services environment. The higher potential impact reflects the possibility that compromised administrative access could affect company systems as well as client-related systems or information.


### Healthcare / Clinic

#### Primary Risk Assessment

**Asset:** Electronic health records and patient information

**Threat:** Ransomware

**Vulnerability:** Software updates are not centrally managed and backup restoration is not regularly tested

**Existing Controls:**

- Endpoint protection
- Password-based authentication
- Backups are maintained
- Software updates are performed but not centrally managed
- Informal security awareness training

**Likelihood:** 4 — High

**Impact:** 5 — Very High

**Initial Risk Score:**

**4 × 5 = 20 — Critical**

#### NIST CSF Mapping

Identify / Protect / Respond / Recover

#### Recommended Controls

- Centralized patch management
- Regular backup restoration testing
- Offline or isolated backups
- Multi-factor authentication (MFA)
- Endpoint protection
- Incident response procedures

#### Expected Effect

The recommended controls are intended to reduce the likelihood of ransomware affecting healthcare systems by improving patch management and authentication while strengthening endpoint protection and recovery capabilities.

#### Residual Risk

The expected residual likelihood is reduced from 4 (High) to 2 (Low), while the potential impact remains 5 (Very High).

#### Residual Risk Score

**2 × 5 = 10 — High**

#### Validation Result

The framework identified ransomware affecting electronic health records and patient information as a critical risk in the healthcare environment. The result demonstrates that the framework can account for the high importance of sensitive information and operational continuity when prioritizing risks.
