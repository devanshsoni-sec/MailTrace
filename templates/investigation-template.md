# Phishing Investigation Report Template

Use this template for individual MailTrace case reports.

Keep the report concise, evidence based, and specific to the case. Remove sections that are not relevant rather than filling them with unnecessary text.

---

## 1. Case Metadata

| Field | Value |
|---|---|
| Case ID | PH-XXX |
| Case Type | Credential Phishing / Malicious Attachment / BEC / QR Phishing / Advanced Credential Phishing / Benign |
| Source | [Source name] |
| Original Filename | `sample.eml` |
| File Type | `message/rfc822` |
| File Size | [Size] |
| SHA-256 | `[hash]` |
| Analysis Date | YYYY-MM-DD |
| Analyst Verdict | Malicious / Benign / Inconclusive |
| Severity | Critical / High / Medium / Low / Informational |

---

## 2. Executive Summary

Provide a concise summary of the investigation.

State:

- What the email attempted to do
- The strongest indicators identified
- Whether the message was malicious or benign
- The overall impact or risk
- The final disposition

Do not include conclusions that are not supported by the available evidence.

---

## 3. Observed Evidence

Record evidence directly present in the original artifact.

### Sender

| Field | Observed Value |
|---|---|
| From | [Value] |
| Return-Path | [Value] |
| Reply-To | [Value] |
| Display Name | [Value] |
| Sender Domain | [Value] |

### Message

| Field | Observed Value |
|---|---|
| To | [Value] |
| Cc | [Value] |
| Subject | [Value] |
| Date | [Value] |
| Message-ID | [Value] |
| MIME Type | [Value] |

### Other Observations

Record relevant observations such as:

- Urgency or pressure
- Credential requests
- Financial requests
- Account changes
- Suspicious links
- Attachments
- QR codes
- Executive impersonation
- Requests for secrecy
- Unusual authentication prompts

---

## 4. Authentication Analysis

Document the available authentication results.

| Control | Result | Interpretation |
|---|---|---|
| SPF | Pass / Fail / SoftFail / Neutral / None / TempError / PermError / Not Available | [Interpretation] |
| DKIM | Pass / Fail / None / Not Available | [Interpretation] |
| DMARC | Pass / Fail / None / Not Available | [Interpretation] |

Explain how the authentication results affect the investigation.

Do not treat an authentication failure as the sole reason for a malicious verdict.

---

## 5. Header Analysis

Review the available message headers for inconsistencies.

### Header Observations

Document relevant findings from:

- From
- Return-Path
- Reply-To
- Received
- Authentication-Results
- Message-ID
- MIME headers

### Header Divergence

Describe any meaningful differences between:

- Display name and sender address
- From and Reply-To
- From domain and Return-Path
- Claimed organization and sender infrastructure
- Expected mail flow and observed mail flow

Record relevant source IP addresses and mail servers when present.

---

## 6. URL Analysis

Complete this section when URLs are present.

### Observed URL

Use a defanged representation:

`hxxps://example[.]com/path`

### URL Findings

Document:

- URL structure
- Domain
- Subdomain
- Path
- Query parameters
- Redirect behavior, if safely observed
- Credential collection behavior, if evidenced
- Reputation results
- Domain or infrastructure observations

### URL Safety

State whether the URL was accessed.

Example:

> The URL was not opened during analysis. Investigation was performed using static inspection and external reputation sources.

---

## 7. QR Code Analysis

Complete this section when a QR code is present.

### QR Artifact

| Field | Value |
|---|---|
| Image | `qr-code.png` |
| SHA-256 | `[hash]` |

### Decoded Destination

Use a defanged URL:

`hxxps://example[.]com/login`

### Analysis

Document:

- Whether the QR code decoded successfully
- Destination domain
- Destination path
- Credential harvesting indicators
- Reputation results
- Redirect information, if safely obtained

State whether the decoded destination was accessed.

---

## 8. Attachment Analysis

Complete this section when an attachment is present.

### Attachment Details

| Field | Value |
|---|---|
| Filename | `[filename]` |
| MIME Type | `[type]` |
| File Size | `[size]` |
| File Type | `[type]` |
| SHA-256 | `[hash]` |

### Static Findings

Document:

- File type and metadata
- Embedded URLs
- Embedded scripts
- Suspicious objects
- Macro presence
- Other relevant static indicators

### Reputation

Document external reputation results and identify the source.

Do not claim execution unless execution was actually observed.

---

## 9. Threat Intelligence Enrichment

Record external enrichment separately from observations in the original artifact.

| Source | Indicator | Result |
|---|---|---|
| VirusTotal | `[IOC]` | [Result] |
| URLScan | `[IOC]` | [Result] |
| ANY.RUN | `[Artifact]` | [Result] |
| Other | `[IOC]` | [Result] |

External enrichment supports the investigation but does not replace analyst reasoning.

---

## 10. User Interaction

State what is known about user interaction.

| Activity | Status |
|---|---|
| Email opened | Confirmed / Not confirmed / Unknown |
| Link clicked | Confirmed / Not confirmed / Unknown |
| Attachment opened | Confirmed / Not confirmed / Unknown |
| Credentials submitted | Confirmed / Not confirmed / Unknown |
| Authentication completed | Confirmed / Not confirmed / Unknown |
| Account compromise | Confirmed / Not confirmed / Unknown |

Do not assume user interaction occurred when the evidence does not establish it.

---

## 11. Scope Assessment

Determine the known or suspected scope of the event.

Consider:

- Intended recipient
- Other recipients
- Distribution pattern
- Similar messages
- Related indicators
- Other affected accounts
- Other affected systems

State clearly when the scope cannot be determined from the available evidence.

---

## 12. Impact Assessment

Assess the potential impact based on the evidence.

Consider:

- Credential exposure
- Account compromise risk
- Malware execution risk
- Financial fraud risk
- Business email compromise
- Data exposure
- Further phishing activity

Distinguish potential impact from confirmed impact.

---

## 13. Analyst Reasoning

Explain how the evidence supports the conclusion.

Structure the reasoning around:

1. Initial suspicion
2. Key investigative pivots
3. Supporting evidence
4. Contradicting or limiting evidence
5. Final assessment

Do not simply repeat threat intelligence verdicts.

---

## 14. Verdict

### Final Verdict

**Malicious / Benign / Inconclusive**

### Classification

[Credential Phishing / Malicious Attachment / BEC / QR Phishing / Advanced Credential Phishing / Benign Communication]

### Rationale

Provide the principal evidence supporting the verdict.

---

## 15. Severity Assessment

**Severity: Critical / High / Medium / Low / Informational**

Explain the severity based on:

- Likelihood of successful attack
- Sensitivity of the targeted action
- Potential business impact
- Evidence of user interaction
- Evidence of compromise
- Availability of containment actions

---

## 16. Containment

Document recommended containment actions appropriate to the evidence.

Examples:

- Quarantine the email
- Remove matching messages
- Block malicious domains or URLs
- Block malicious file hashes
- Disable compromised accounts
- Revoke active sessions
- Reset exposed credentials
- Isolate affected endpoints

Do not claim that containment was performed unless it was actually performed.

---

## 17. Remediation

Document recommended remediation actions.

Examples:

- User awareness follow-up
- Credential reset
- MFA review
- Mail filtering improvement
- Sender validation controls
- Executive impersonation controls
- Attachment filtering
- QR phishing protections
- Detection rule improvements

---

## 18. Detection Opportunities

Document useful detection opportunities derived from the investigation.

Examples:

- Sender and Reply-To mismatch
- Authentication failures
- Suspicious sender infrastructure
- Known phishing domains
- Malicious attachment hashes
- Suspicious URL patterns
- QR encoded phishing URLs
- Executive impersonation indicators
- Credential harvesting patterns

Only include detections that are reasonably supported by the case.

---

## 19. MITRE ATT&CK

Map the case only when the available evidence supports a technique.

| Technique | Name | Evidence |
|---|---|---|
| T1566.001 | Phishing: Spearphishing Attachment | [Evidence] |
| T1566.002 | Phishing: Spearphishing Link | [Evidence] |

Do not assign techniques merely because they are commonly associated with phishing.

---

## 20. Evidence References

List the supporting artifacts used during the investigation.

| Evidence | Location |
|---|---|
| Original Email | `sample.eml` |
| Headers | `evidence/headers.txt` |
| Hashes | `evidence/hashes.txt` |
| URL Analysis | `evidence/url-analysis.txt` |
| Attachment Analysis | `evidence/attachment-analysis.txt` |
| Threat Intelligence | `evidence/virustotal-result.txt` |
| Sandbox Analysis | `evidence/anyrun-analysis.txt` |
| Screenshots | `evidence/[filename].png` |

Remove entries that do not exist for the case.

---

## 21. Evidence Limitations

Document important limitations.

Examples:

- Original headers were incomplete
- Authentication results were unavailable
- User interaction could not be confirmed
- The original attachment was unavailable
- Sandbox analysis was available only through an external report
- Credential submission could not be independently verified
- Account compromise could not be confirmed
- Redirect behavior was not tested

The purpose of this section is to prevent unsupported conclusions.

---

## 22. Evidence Classification

Classify important findings using the MailTrace evidence model.

### OBSERVED

Directly present in the original artifact or produced through controlled local analysis.

Examples:

- Sender address
- Reply-To address
- Subject
- Authentication result
- Received header
- Attachment filename
- Attachment hash
- QR decoded URL

### ENRICHED

Obtained from external analysis or threat intelligence.

Examples:

- VirusTotal results
- Sandbox findings
- DNS information
- URL reputation
- Public malware analysis

### INFERRED

Analyst conclusions derived from the available evidence.

Examples:

- Credential phishing
- Executive impersonation
- BEC attempt
- Malicious attachment
- Benign communication

Never present an inferred conclusion as directly observed evidence.

---

## 23. Final Disposition

| Field | Value |
|---|---|
| Verdict | [Malicious / Benign / Inconclusive] |
| Severity | [Severity] |
| User Interaction | [Confirmed / Not confirmed / Unknown] |
| Compromise | [Confirmed / Not confirmed / Unknown] |
| Containment Required | [Yes / No] |
| Remediation Required | [Yes / No] |
| Escalation Required | [Yes / No] |

### Disposition Summary

Provide a short final statement describing the analyst's decision and the reason for that decision.

---

## Analyst Notes

Use this area only for important investigation notes that do not fit elsewhere.

Avoid adding unnecessary raw tool output or repetitive observations.