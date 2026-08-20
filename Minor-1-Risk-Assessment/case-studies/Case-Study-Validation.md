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

---

# Validation Findings

## Overall Findings

The framework was applied to three fictional SME environments: a retail and e-commerce business, an IT services company, and a healthcare clinic.

The same likelihood and impact scoring methodology was maintained across all three case studies. The business context, assets, threats, vulnerabilities, and recommended controls were adapted according to each organization's environment.

## Finding 1 — The Framework Identifies Business-Specific Risks

The primary risks differed according to the nature of each business:

- **Retail & E-commerce:** Unauthorized account access was prioritized because of the organization's customer-facing online services and customer information.
- **IT Services:** Privileged account compromise was prioritized because administrative access and client-related systems represent important assets.
- **Healthcare / Clinic:** Ransomware was prioritized because disruption to electronic health records and healthcare operations could have significant consequences.

This demonstrates that the framework can be applied to different SME environments rather than relying on a fixed list of identical priorities.

## Finding 2 — The Scoring Methodology Remains Consistent

The same 1–5 likelihood and 1–5 impact scales were used for every case study.

The risk score was calculated using:

**Risk Score = Likelihood × Impact**

This provides a consistent method for comparing risks while allowing the underlying business context to influence the selected risks and ratings.

## Finding 3 — Mitigation Reduces but Does Not Eliminate Risk

The case studies demonstrated that applying recommended controls can reduce the expected likelihood of a successful incident.

For all three primary risks, the initial risk score was:

**4 × 5 = 20 — Critical**

After applying the proposed controls, the expected residual risk became:

**2 × 5 = 10 — High**

This demonstrates the concept of residual risk: security controls can reduce risk, but they do not necessarily eliminate the potential consequences of a successful attack.

## Finding 4 — Different Businesses Require Different Controls

Although the same assessment methodology was used, the recommended controls differed according to the business environment.

Examples include:

- Retail & E-commerce → MFA, account monitoring, access controls, and security logging.
- IT Services → privileged account controls, RBAC, least privilege, and administrative monitoring.
- Healthcare / Clinic → patch management, backup restoration testing, isolated backups, and incident response.

This demonstrates that mitigation strategies should be selected according to the organization's assets, vulnerabilities, and operational requirements.

## Finding 5 — The Framework Supports Repeatable Assessment

The case studies followed the same sequence:

**Business Environment → Assets → Threats → Vulnerabilities → Likelihood → Impact → Risk Score → NIST CSF Mapping → Mitigation → Residual Risk**

Using the same sequence across different businesses provides a repeatable assessment process that can be reused for other SME environments.

## Validation Conclusion

The case-study results indicate that the proposed framework can be used to identify, prioritize, and mitigate cybersecurity risks in different SME environments while maintaining a consistent risk evaluation methodology.

The validation also demonstrates that risk priorities and mitigation strategies should be adapted to the specific business context rather than applying identical cybersecurity controls to every organization.

---

# SME Cybersecurity Best Practices

The following best practices were identified from the risk assessment, mitigation analysis, case-study validation, and relevant NIST cybersecurity guidance.

## 1. Maintain an Asset Inventory

SMEs should maintain an up-to-date record of important hardware, software, accounts, data, systems, and services.

Knowing what assets exist helps organizations identify which systems require protection and prioritize cybersecurity resources.

## 2. Use Multi-Factor Authentication

Multi-factor authentication (MFA) should be enabled wherever available, particularly for administrator accounts, remote access, email, cloud services, and systems containing sensitive information.

Phishing-resistant authentication should be considered for high-value applications and privileged users where practical.

## 3. Apply Least Privilege

Employees should receive only the access required to perform their responsibilities.

Administrative privileges should be restricted, reviewed periodically, and monitored for unusual activity.

## 4. Maintain Secure and Tested Backups

Important business data should be backed up regularly.

SMEs should also periodically test restoration procedures rather than assuming that a backup will work when needed.

Where appropriate, isolated or offline backup copies should be maintained to reduce the risk of ransomware affecting both production systems and backups.

## 5. Keep Systems and Software Updated

SMEs should maintain an inventory of software and systems and establish a process for applying security updates.

Critical vulnerabilities should be prioritized according to their potential impact and exposure.

## 6. Train Employees to Recognize Cybersecurity Threats

Employees should receive regular cybersecurity awareness training covering threats such as:

- Phishing
- Malicious attachments
- Suspicious links
- Password security
- Social engineering
- Reporting suspected incidents

Employee awareness is particularly important because many attacks attempt to exploit human behavior.

## 7. Implement Basic Security Monitoring

SMEs should maintain appropriate logs and monitoring for important systems, accounts, and security events.

Monitoring can help identify suspicious activity and provide useful information during incident investigation.

## 8. Prepare an Incident Response Plan

An SME should have a basic incident response plan that identifies:

- Who is responsible for coordinating the response
- Who should be contacted during an incident
- How incidents should be reported
- How affected systems should be contained
- How business operations should be restored

The plan should be reviewed and practiced periodically.

NIST's SME guidance recommends establishing responsibilities, contacts, reporting procedures, and response actions before an incident occurs. :contentReference[oaicite:1]{index=1}

## 9. Protect Sensitive Information

Sensitive business and customer information should be protected using appropriate access controls, authentication, encryption, and monitoring.

Additional safeguards should be considered for information such as financial information, personal information, healthcare information, and business credentials.

## 10. Review Cybersecurity Risks Regularly

Cybersecurity risk assessment should not be treated as a one-time activity.

SMEs should periodically review:

- New assets
- New threats
- Vulnerabilities
- Security incidents
- Changes in business operations
- Effectiveness of existing controls
- Residual risks

The risk assessment should be updated when significant changes occur.

## 11. Prioritize Controls According to Risk

SMEs often have limited budgets and personnel.

Therefore, cybersecurity controls should be prioritized according to the organization's most significant risks rather than attempting to implement every possible security measure simultaneously.

## 12. Assign Cybersecurity Responsibilities

Even when an SME does not have a dedicated cybersecurity team, responsibility for cybersecurity should be clearly assigned.

Someone should be responsible for coordinating risk assessment, security controls, incident response, and periodic reviews.

## Best-Practice Summary

The most important principle for SMEs is to establish a practical, risk-based cybersecurity program rather than attempting to implement every security control at once.

A practical progression is:

**Identify Assets**
→ **Identify Risks**
→ **Prioritize Risks**
→ **Implement Appropriate Controls**
→ **Monitor**
→ **Respond**
→ **Recover**
→ **Review and Improve**

These practices should be adapted to the organization's size, resources, business environment, and applicable legal or regulatory requirements. NIST's CSF 2.0 Small Business Quick-Start Guide is intended to help SMBs begin this type of risk-management process. :contentReference[oaicite:2]{index=2}

## Final Conclusion

The project demonstrates that a structured cybersecurity risk assessment can help SMEs identify important threats, prioritize risks, select appropriate controls, and evaluate residual risk.

The case-study validation showed that the same assessment methodology can be applied across different business environments while allowing risks and mitigation strategies to be adapted to each organization's specific circumstances.

A risk-based approach allows SMEs to focus limited resources on the cybersecurity risks that could have the greatest effect on their business operations, information, and customers.
