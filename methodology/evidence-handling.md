# Evidence Handling Methodology

## Purpose

This document defines how email artifacts, extracted evidence, threat intelligence, and analyst conclusions are handled throughout the MailTrace phishing investigation workflow.

The objective is to preserve evidence integrity, maintain traceability, avoid unsupported claims, and ensure that investigation results remain reproducible.

## Evidence Handling Principles

### Preserve the Original

The original email artifact is treated as the primary evidence source.

The original file should not be modified during investigation.

Where analysis requires extraction, decoding, conversion, or transformation, the resulting artifact is stored separately from the original.

### Record Cryptographic Hashes

SHA-256 hashes are recorded for important evidence artifacts where practical.

Hashes provide a reproducible identifier for an artifact and allow later verification that the file has not changed.

Example:

```text
sample.eml
SHA-256: <hash>
```

### Maintain Evidence Separation

MailTrace distinguishes between three evidence categories.

#### OBSERVED

Evidence directly present in the original artifact or directly produced by controlled local analysis.

Examples:

- Sender address
- Reply-To address
- Subject
- Authentication result
- Received headers
- Attachment filename
- Attachment hash
- QR-decoded URL

#### ENRICHED

Evidence obtained from external analysis or threat intelligence sources.

Examples:

- VirusTotal detection results
- Sandbox verdicts
- External reputation results
- DNS information
- Public malware analysis

External enrichment is documented separately from the original artifact.

#### INFERRED

The analyst's interpretation based on the observed and enriched evidence.

Examples:

- Likely credential phishing
- Executive impersonation
- High-risk BEC attempt
- Benign communication

An inferred conclusion must not be presented as directly observed evidence.

## Original Artifact Handling

The investigation begins with preservation of the original email.

The following information should be recorded:

- Original filename
- File size
- File type
- SHA-256 hash
- Source
- Acquisition context when available

The original artifact should remain unchanged.

## Email Header Handling

Relevant headers are preserved separately when useful.

Typical headers include:

- Return-Path
- Received
- From
- Reply-To
- To
- Cc
- Subject
- Date
- Message-ID
- Authentication-Results
- MIME information

Header evidence should remain traceable to the original message.

Do not manually alter header values while preserving evidence.

## URL Handling

URLs from suspicious messages are handled without directly accessing the destination during normal triage.

The investigation may record:

- Original URL
- Defanged URL
- Domain
- Host
- Path
- Query parameters
- Redirect information when safely obtained

Public documentation should use defanged URLs.

Example:

```text
hxxps://example[.]com/login
```

A live destination should only be described when its content was actually observed through an appropriate controlled analysis method.

Do not claim redirect chains, page content, or infrastructure behavior that was not observed.

## QR Code Handling

When a QR code is present:

1. Preserve the original email.
2. Extract the QR image locally.
3. Preserve the extracted image separately.
4. Record the image hash where appropriate.
5. Decode the QR code using a controlled local method.
6. Record the decoded value.
7. Defang URLs for public documentation.
8. Avoid directly visiting the decoded destination.

The decoded URL is treated as an observed indicator because it was directly obtained from the QR image.

Any reputation or sandbox result associated with the destination is treated as enriched evidence.

## Attachment Handling

Attachments are extracted without executing them.

Relevant metadata may include:

- Filename
- Extension
- MIME type
- File size
- Magic bytes
- SHA-256 hash

Static analysis and external reputation or sandbox services may be used when appropriate.

If an endpoint security product quarantines or removes an extracted attachment, the investigation should not recreate the removed file merely to generate additional evidence.

The security product detection should be preserved as evidence instead.

## Threat Intelligence Handling

External intelligence is treated as enrichment rather than as the sole basis for a verdict.

For external sources, record when practical:

- Source
- Indicator
- Result
- Detection information
- Analysis date

A threat intelligence result should be combined with artifact evidence and analyst reasoning.

For example:

```text
Observed:
The email contains a suspicious attachment.

Enriched:
The attachment hash is detected by multiple security vendors.

Inferred:
The attachment is assessed as malicious.
```

## Hash Handling

Hashes are recorded exactly as produced by the analysis tool.

Do not manually alter capitalization or characters except for presentation consistency.

Where multiple artifacts exist, identify each artifact separately.

Example:

```text
sample.eml
SHA-256: <hash>

attachment.pdf
SHA-256: <hash>
```

Artifact hashes and malicious IOC hashes serve different purposes.

A hash is not automatically a threat IOC simply because it identifies an investigation artifact.

## IOC Handling

The centralized IOC feed contains indicators that provide practical detection or investigation value.

Potential IOC types include:

- Domains
- URLs
- IP addresses
- Email addresses
- File hashes

Malicious URLs and domains are defanged for public documentation.

Benign indicators are not included as malicious IOCs.

Artifact hashes are included only when they provide useful detection or investigation value.

## Evidence Limitations

Absence of evidence must not be converted into a positive claim.

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

```text
Redirect chain: Not observed
```

When evidence is unavailable, explicitly state the limitation.

## Sandbox Evidence

Sandbox results are treated as external enriched evidence.

The sandbox environment may demonstrate:

- Malicious behavior
- Phishing detection
- Network activity
- Browser activity
- Process activity
- Fingerprinting
- Malware execution
- Other controlled behaviors

Sandbox observations should not automatically be interpreted as proof of real-world victim activity.

A sandbox observation such as credential submission must not be described as a real user entering credentials unless the investigation has separate evidence supporting that conclusion.

## Evidence Integrity

Evidence files should remain unchanged after finalization unless a documented correction is required.

When a correction is necessary:

1. Identify the affected evidence.
2. Correct the artifact or report.
3. Recalculate hashes where applicable.
4. Ensure references remain accurate.
5. Remove outdated unsupported claims.

Do not silently replace evidence after a verdict has been finalized.

## Case Documentation

Each case should maintain a consistent structure:

```text
case/
├── sample.eml
├── investigation-report.md
└── evidence/
    ├── headers.txt
    ├── hashes.txt
    └── supporting-analysis
```

Only useful supporting artifacts should be retained.

Avoid storing large raw tool outputs that do not materially support the investigation.

## Analyst Reasoning

The final verdict should reflect the totality of evidence.

Example reasoning structure:

```text
Observed evidence
        ↓
Authentication and sender analysis
        ↓
URL / attachment / QR analysis
        ↓
Threat intelligence enrichment
        ↓
User interaction and scope assessment
        ↓
Impact assessment
        ↓
Analyst verdict
```

Tools provide evidence.

The analyst makes the decision.

## Public Repository Safety

Before publishing MailTrace:

- Defang malicious URLs and domains.
- Remove credentials and secrets.
- Avoid unnecessary personal information.
- Review screenshots for sensitive information.
- Do not publish unnecessary active malicious infrastructure details.
- Do not include malware samples that create unnecessary risk.
- Ensure external analysis links are clearly identified as external enrichment.
- Verify that case reports do not claim unsupported compromise.

## Quality Standard

A completed investigation should allow another analyst to understand:

1. What evidence was available.
2. How the evidence was handled.
3. Which findings were directly observed.
4. Which findings came from external enrichment.
5. What conclusions were inferred.
6. What evidence limitations existed.
7. Why the final verdict and severity were assigned.

This methodology is intended to make MailTrace reproducible, evidence-driven, and representative of a practical SOC phishing investigation workflow.