# MailTrace

## Phishing Email Triage & Forensics Lab

MailTrace is a practical SOC focused phishing investigation lab covering email triage, evidence preservation, header analysis, threat intelligence enrichment, analyst reasoning, and incident response recommendations.

The project demonstrates a repeatable workflow for taking a suspicious or user reported email from initial triage through final disposition.

## Cases

| Case | Scenario | Disposition |
|---|---|---|
| PH-001 | Credential Phishing | Malicious |
| PH-002 | Malicious Attachment | Malicious |
| PH-003 | BEC / Executive Impersonation | Malicious |
| PH-004 | QR Phishing | Malicious |
| PH-005 | Advanced Credential / Access Phishing | Malicious |
| PH-006 | Benign Email / False Positive | Benign |

Each case focuses on a different investigation pattern rather than repeating the same workflow.

## Investigation Workflow

```text
Suspicious Email
      |
      v
Evidence Preservation
      |
      v
Header Analysis
      |
      v
Sender & Authentication Analysis
      |
      v
URL / Attachment / QR Analysis
      |
      v
Threat Intelligence Enrichment
      |
      v
IOC Extraction
      |
      v
User Interaction & Scope Assessment
      |
      v
Impact Assessment
      |
      v
Verdict & Severity
      |
      v
Containment & Remediation
      |
      v
Detection Opportunities
      |
      v
Documentation
```

## Investigation Coverage

### PH-001: Credential Phishing

Credential phishing investigation focused on sender identity, authentication results, suspicious destination analysis, and credential theft risk.

### PH-002: Malicious Attachment

Attachment focused investigation covering file identification, MIME characteristics, hashing, endpoint security detection, file reputation, and safe enrichment.

### PH-003: BEC / Executive Impersonation

Business Email Compromise investigation focused on executive impersonation, sender identity divergence, Reply To analysis, authentication failures, urgent financial requests, and payment fraud risk.

### PH-004: QR Phishing

QR phishing investigation covering embedded image extraction, local QR decoding, safe URL handling, and authentication themed phishing analysis.

### PH-005: Advanced Credential / Access Phishing

Advanced Microsoft 365 credential and access phishing investigation using public sandbox enrichment associated with a Sneaky 2FA Adversary in the Middle phishing campaign.

The original email artifact was not directly obtained from the public analysis interface, so the repository documents the external analysis rather than fabricating the missing source artifact.

### PH-006: Benign Email / False Positive

Legitimate internal business communication used to demonstrate false positive handling and the ability to distinguish normal activity from phishing.

## Evidence Model

MailTrace separates evidence into three categories.

### OBSERVED

Evidence directly present in the original artifact or produced through controlled local analysis.

Examples:

- Sender address
- Reply To address
- Subject
- Authentication results
- Received headers
- Attachment metadata
- File hashes
- QR decoded URLs

### ENRICHED

Evidence obtained from an external analysis or intelligence source.

Examples:

- VirusTotal results
- Sandbox analysis
- Public malware analysis
- Domain reputation
- DNS information

### INFERRED

Analyst conclusions based on observed and enriched evidence.

Examples:

- Credential phishing
- Executive impersonation
- High risk BEC
- Benign communication

These categories are kept separate throughout the investigations.

## Evidence Handling

MailTrace follows a simple evidence preservation model:

- Preserve original email artifacts.
- Record SHA 256 hashes for relevant evidence.
- Keep extracted evidence separate from originals.
- Preserve useful supporting artifacts.
- Identify external enrichment clearly.
- Record evidence limitations.
- Avoid unsupported conclusions.

When evidence is unavailable, the investigation states the limitation rather than inferring a result.

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

## Safe Analysis Approach

MailTrace is designed to demonstrate phishing investigation without unnecessary interaction with live malicious infrastructure.

Suspicious URLs are not directly opened during normal triage.

Malicious URLs and domains are defanged for public documentation.

Attachments are handled through controlled extraction and analysis rather than normal execution.

QR codes are decoded locally and their destinations are documented safely.

External sandbox and reputation services are treated as enrichment sources rather than substitutes for analyst judgment.

## IOC Feed

The project maintains a centralized IOC feed containing indicators that provide practical investigation or detection value.

The feed may contain:

- Domains
- URLs
- Email addresses
- File hashes

Malicious URLs and domains are defanged for public documentation.

Benign indicators are not treated as malicious IOCs.

## Public Artifact Handling

Raw email artifacts are intentionally excluded from the public repository.

## Repository Structure

```text
MailTrace/
├── README.md
├── playbooks/
│   └── PHISHING-TRIAGE-SOP.md
├── cases/
│   ├── PH-001-credential-phishing/
│   │   ├── investigation-report.md
│   │   └── evidence/
│   ├── PH-002-malicious-attachment/
│   │   ├── investigation-report.md
│   │   └── evidence/
│   ├── PH-003-bec-impersonation/
│   │   ├── investigation-report.md
│   │   └── evidence/
│   ├── PH-004-qr-phishing/
│   │   ├── investigation-report.md
│   │   └── evidence/
│   ├── PH-005-advanced-credential-phishing/
│   │   ├── investigation-report.md
│   │   └── evidence/
│   └── PH-006-benign-email/
│       └── evidence/
│       ├── investigation-report.md
│       └── evidence/
├── iocs/
│   └── ioc-feed.csv
├── methodology/
│   └── evidence-handling.md
├── templates/
│   └── investigation-template.md
└── tools/
    └── defang_tool.py
```

## Standard Investigation Report

Each case uses a consistent investigation structure:

1. Case Metadata
2. Executive Summary
3. Observed Evidence
4. Authentication Analysis
5. Header Divergence
6. URL Analysis where applicable
7. Attachment Analysis where applicable
8. QR Analysis where applicable
9. Threat Intelligence Enrichment
10. User Interaction
11. Scope
12. Impact Assessment
13. Verdict
14. Severity Assessment
15. Containment
16. Remediation
17. Detection Opportunities
18. MITRE ATT&CK where justified
19. Evidence References
20. Evidence Limitations where applicable

## Analyst Principles

### Do not rely on a single indicator

A suspicious sender, authentication failure, URL, attachment, or reputation result should be evaluated in context.

### Tools provide evidence

Security tools support the investigation but do not replace analyst judgment.

### Do not fabricate findings

MailTrace does not claim:

- Credential submission without evidence.
- Account compromise without evidence.
- Successful payment without transaction evidence.
- Session theft without supporting evidence.
- OAuth authorization without supporting evidence.
- Malware execution without execution evidence.
- Redirect chains that were not observed.
- Infrastructure ownership that was not established.

### Negative findings matter

A useful SOC investigation must also recognize when a message is legitimate.

PH-006 demonstrates false positive handling and avoids unnecessary escalation.

## Public Repository Safety

The public repository is reviewed to ensure that:

- Malicious URLs are defanged.
- Credentials and secrets are absent.
- Unnecessary personal information is removed.
- Screenshots do not expose sensitive information.
- Unnecessary live malicious infrastructure details are avoided.
- External analysis is clearly identified.
- Reports do not claim unsupported compromise.
- Suspicious artifacts are not unnecessarily distributed.

## Skills Demonstrated

MailTrace demonstrates practical capability in:

- Phishing email triage
- Email header analysis
- SPF, DKIM, and DMARC interpretation
- Sender identity analysis
- BEC investigation
- Executive impersonation analysis
- Credential phishing analysis
- QR phishing analysis
- Attachment triage
- File hashing
- Threat intelligence enrichment
- Sandbox analysis
- IOC extraction
- Evidence preservation
- Analyst reasoning
- Incident severity assessment
- Containment recommendations
- Remediation recommendations
- Detection opportunities
- False positive analysis
- SOC investigation documentation

## Related SOC Workflow

MailTrace focuses specifically on the email threat investigation layer.

The project demonstrates how phishing alerts and user reported suspicious emails can be investigated, documented, and converted into useful indicators and detection opportunities for wider SOC workflows.

## Disclaimer

MailTrace is an educational and portfolio focused security investigation lab.

The project uses public or controlled artifacts and analysis results where available.

No claim is made that a particular artifact compromised a real organization unless the available evidence explicitly supports that conclusion.

All findings are documented according to the evidence available for each case.