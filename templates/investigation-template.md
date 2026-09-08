\# Phishing Investigation Report Template



\## Case Metadata



| Field | Value |

|---|---|

| Case ID | |

| Case Type | |

| Initial Verdict | |

| Severity | |

| Evidence Source | |

| User Interaction | |

| Account Compromise | |

| Financial Impact | |



\## Executive Summary



\[Summarize the investigation, primary findings, verdict, and key impact considerations in 2 to 5 sentences.]



\## Observed Evidence



\[Record facts directly present in the original artifact or produced through controlled local analysis.]



\## Authentication Analysis



\[Document SPF, DKIM, and DMARC results when available.]



\## Header Divergence



\[Assess From, Return-Path, Reply-To, Received headers, sender identity, and infrastructure relationships.]



\## URL Analysis



\[Document relevant URLs, domains, paths, query parameters, redirect observations, and safe handling.]



\## QR Code Analysis



\[Complete only when a QR code is present. Document extraction, decoding, destination, and safe handling.]



\## Attachment Analysis



\[Complete only when an attachment is present. Document filename, type, size, MIME type, magic bytes, hashes, and analysis.]



\## Threat Intelligence Enrichment



\[Document external reputation, sandbox, DNS, or other intelligence sources separately from observed evidence.]



\## User Interaction



\[State whether interaction is confirmed, disproved, or unknown.]



\## Scope



\[Document affected users, messages, endpoints, infrastructure, or explicitly state when broader scope cannot be determined.]



\## Impact Assessment



\[Distinguish potential impact from confirmed impact.]



\## Verdict



\*\*\[Malicious / Benign / Suspicious / Further Investigation Required]\*\*



\[Explain the evidence supporting the final disposition.]



\## Severity Assessment



\*\*\[Critical / High / Medium / Low / Informational]\*\*



\[Explain why the severity is appropriate.]



\## Containment



\- \[Immediate containment action]

\- \[Investigation or blocking action]

\- \[User or account action when appropriate]



\## Remediation



\- \[Control improvement]

\- \[Process improvement]

\- \[User awareness or monitoring improvement]



\## Detection Opportunities



\- \[Detection signal]

\- \[Detection signal]

\- \[Detection signal]



\## MITRE ATT\&CK



\[Assign only when the evidence supports a defensible technique mapping. Otherwise state that no ATT\&CK technique is assigned.]



\## Evidence References



1\. `\[evidence file]`

2\. `\[evidence file]`

3\. `\[external enrichment source when applicable]`



\## Evidence Limitations



\[Document unavailable telemetry, unknown user interaction, unconfirmed compromise, unavailable scope, or other limitations.]



\## Evidence Classification



\### OBSERVED



\[Direct artifact or controlled local analysis findings.]



\### ENRICHED



\[External intelligence or sandbox findings.]



\### INFERRED



\[Analyst conclusions based on the observed and enriched evidence.]
