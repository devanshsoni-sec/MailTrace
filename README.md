\# MailTrace



\## Phishing Email Triage \& Forensics Lab



MailTrace is a practical SOC-focused phishing investigation lab built around realistic email triage, evidence preservation, threat intelligence enrichment, analyst reasoning, and incident response recommendations.



The project demonstrates how a SOC analyst can take a suspicious or user-reported email from initial triage through final disposition while maintaining evidence integrity and clearly separating observed evidence from external enrichment and analyst conclusions.



\## Objective



The objective of MailTrace is to demonstrate a repeatable phishing investigation workflow aligned with practical SOC L1 responsibilities.



The investigation process covers:



```text

Suspicious Email

&#x20;       ↓

Evidence Preservation

&#x20;       ↓

Header Analysis

&#x20;       ↓

Sender and Authentication Analysis

&#x20;       ↓

URL / Attachment / QR Analysis

&#x20;       ↓

Threat Intelligence Enrichment

&#x20;       ↓

IOC Extraction

&#x20;       ↓

User Interaction Assessment

&#x20;       ↓

Scope Assessment

&#x20;       ↓

Impact Assessment

&#x20;       ↓

Analyst Reasoning

&#x20;       ↓

Verdict and Severity

&#x20;       ↓

Containment

&#x20;       ↓

Remediation

&#x20;       ↓

Detection Opportunities

&#x20;       ↓

Documentation

```



\## Cases



MailTrace contains six investigation cases representing common and higher-risk phishing scenarios.



| Case | Scenario | Final Disposition |

|---|---|---|

| PH-001 | Credential Phishing | Malicious |

| PH-002 | Malicious Attachment | Malicious |

| PH-003 | BEC / Executive Impersonation | Malicious |

| PH-004 | QR Phishing | Malicious |

| PH-005 | Advanced Credential / Access Phishing | Malicious |

| PH-006 | Benign Email / False Positive | Benign |



The cases intentionally cover different investigation patterns rather than repeating the same phishing workflow.



\## Investigation Coverage



\### PH-001: Credential Phishing



Traditional credential phishing investigation focused on sender analysis, authentication, suspicious destination analysis, and credential theft indicators.



\### PH-002: Malicious Attachment



Attachment-focused investigation covering file identification, MIME characteristics, hashing, endpoint security detection, file reputation, and safe enrichment.



\### PH-003: BEC / Executive Impersonation



Business Email Compromise investigation focused on executive impersonation, sender identity divergence, Reply-To analysis, failed authentication, urgent financial requests, and payment fraud risk.



\### PH-004: QR Phishing



QR-based phishing investigation covering embedded image extraction, local QR decoding, safe URL handling, and authentication-themed phishing analysis.



\### PH-005: Advanced Credential / Access Phishing



Advanced Microsoft 365 credential and access phishing investigation using public sandbox enrichment associated with a Sneaky 2FA Adversary-in-the-Middle phishing campaign.



\### PH-006: Benign Email / False Positive



Legitimate internal business communication used to demonstrate false-positive handling and the analyst's ability to avoid unnecessary escalation.



\## Evidence Model



MailTrace uses three evidence categories.



\### OBSERVED



Evidence directly present in the original artifact or produced through controlled local analysis.



Examples:



\- Sender address

\- Reply-To address

\- Subject

\- Authentication results

\- Received headers

\- Attachment metadata

\- File hashes

\- QR-decoded URLs



\### ENRICHED



Evidence obtained from an external source.



Examples:



\- VirusTotal results

\- Sandbox analysis

\- Public malware analysis

\- Domain reputation

\- DNS information



\### INFERRED



The analyst's conclusion based on the observed and enriched evidence.



Examples:



\- Likely credential phishing

\- Executive impersonation

\- High-risk BEC

\- Benign communication



These categories are kept distinct throughout the investigations.



\## Evidence Handling



The project follows evidence preservation principles designed to keep investigations reproducible.



Key practices include:



\- Preserve original email artifacts.

\- Record SHA-256 hashes for relevant evidence.

\- Keep extracted evidence separate from originals.

\- Preserve useful supporting artifacts.

\- Avoid unnecessary raw tool output.

\- Clearly identify external enrichment.

\- Record evidence limitations.

\- Avoid unsupported claims.



When evidence is unavailable, the investigation explicitly records the limitation rather than inferring a result.



Examples:



```text

User interaction: Unknown

```



```text

Account compromise: Not confirmed

```



```text

Scope: Not available from the provided evidence

```



\## Safe Analysis Approach



MailTrace is designed to demonstrate investigation capability without unnecessarily interacting with live malicious infrastructure.



Suspicious URLs are not directly opened during normal triage.



Malicious URLs and domains are defanged for public documentation.



Attachments are handled through controlled extraction and analysis rather than normal execution.



QR codes are decoded locally and their destinations are documented safely.



External sandbox and reputation services are treated as enrichment sources rather than as substitutes for analyst reasoning.



\## IOC Feed



The project maintains a centralized IOC feed containing indicators that provide practical investigation or detection value.



The feed may contain:



\- Domains

\- URLs

\- Email addresses

\- File hashes



Malicious URLs and domains are defanged for safe public documentation.



Benign indicators are not treated as malicious IOCs.



\## Repository Structure



```text

MailTrace/

│

├── README.md

│

├── playbooks/

│   └── PHISHING-TRIAGE-SOP.md

│

├── cases/

│   │

│   ├── PH-001-credential-phishing/

│   │   ├── sample.eml

│   │   ├── investigation-report.md

│   │   └── evidence/

│   │

│   ├── PH-002-malicious-attachment/

│   │   ├── sample.eml

│   │   ├── investigation-report.md

│   │   └── evidence/

│   │

│   ├── PH-003-bec-impersonation/

│   │   ├── sample.eml

│   │   ├── investigation-report.md

│   │   └── evidence/

│   │

│   ├── PH-004-qr-phishing/

│   │   ├── sample.eml

│   │   ├── investigation-report.md

│   │   └── evidence/

│   │

│   ├── PH-005-advanced-credential-phishing/

│   │   ├── investigation-report.md

│   │   └── evidence/

│   │

│   └── PH-006-benign-email/

│       ├── sample.eml

│       ├── investigation-report.md

│       └── evidence/

│

├── iocs/

│   └── ioc-feed.csv

│

├── templates/

│   └── investigation-template.md

│

├── methodology/

│   └── evidence-handling.md

│

└── tools/

&#x20;   └── defang\_tool.py

```



\## Standard Investigation Report



Each case uses a consistent investigation structure covering:



1\. Case Metadata

2\. Executive Summary

3\. Observed Evidence

4\. Authentication Analysis

5\. Header Divergence

6\. URL Analysis where applicable

7\. Attachment Analysis where applicable

8\. QR Analysis where applicable

9\. Threat Intelligence Enrichment

10\. User Interaction

11\. Scope

12\. Impact Assessment

13\. Verdict

14\. Severity Assessment

15\. Containment

16\. Remediation

17\. Detection Opportunities

18\. MITRE ATT\&CK when justified

19\. Evidence References

20\. Evidence Limitations where applicable



\## Analyst Principles



MailTrace follows several core analyst principles.



\### Do not trust a single indicator



A suspicious sender, authentication failure, URL, attachment, or reputation result should be evaluated in context.



\### Tools provide evidence



Security tools support the investigation but do not replace analyst judgment.



\### Do not fabricate findings



The project does not claim:



\- Credential submission without evidence.

\- Account compromise without evidence.

\- Successful payment without transaction evidence.

\- Session theft without supporting evidence.

\- OAuth authorization without supporting evidence.

\- Malware execution without execution evidence.

\- Redirect chains that were not observed.

\- Infrastructure ownership that was not established.



\### Negative findings matter



A strong SOC investigation must also recognize when a message is legitimate.



PH-006 demonstrates the ability to distinguish legitimate internal communication from malicious phishing activity.



\## Public Repository Safety



Before publication, MailTrace is reviewed to ensure that:



\- Malicious URLs are defanged.

\- Credentials and secrets are absent.

\- Unnecessary personal information is removed.

\- Screenshots do not expose sensitive information.

\- Unnecessary live malicious infrastructure details are avoided.

\- External analysis is clearly identified.

\- Reports do not claim unsupported compromise.

\- Suspicious artifacts are not unnecessarily distributed.



\## Skills Demonstrated



MailTrace demonstrates practical capability in:



\- Phishing email triage

\- Email header analysis

\- SPF, DKIM, and DMARC interpretation

\- Sender identity analysis

\- BEC investigation

\- Executive impersonation analysis

\- Credential phishing analysis

\- QR phishing analysis

\- Attachment triage

\- File hashing

\- Threat intelligence enrichment

\- Sandbox analysis

\- IOC extraction

\- Evidence preservation

\- Analyst reasoning

\- Incident severity assessment

\- Containment recommendations

\- Remediation recommendations

\- Detection engineering opportunities

\- False-positive analysis

\- SOC investigation documentation



\## Related SOC Workflow



MailTrace complements broader SOC capabilities demonstrated through other security projects by focusing specifically on the email threat investigation layer.



The project is designed to demonstrate how phishing alerts and user-reported suspicious emails can be investigated before indicators and findings are incorporated into wider security monitoring and detection workflows.



\## Disclaimer



MailTrace is an educational and portfolio-focused security investigation lab.



The project uses public or controlled artifacts and analysis results where available.



No claim is made that a particular artifact compromised a real organization unless the evidence explicitly supports that conclusion.



All findings are documented according to the evidence available for each case.
