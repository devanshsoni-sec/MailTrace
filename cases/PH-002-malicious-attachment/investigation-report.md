# PH-002: Malicious Attachment

## 1. Case Metadata

Case ID:
PH-002

Case Type:
Malicious Attachment

Source:
rf-peixoto/phishing_pot

Initial Alert:
Phishing email sample selected for investigation

Sample:
sample.eml

Date Analyzed:
2026-09-07

Final Verdict:
Malicious

Severity:
High

## 2. Executive Summary

The email uses a financial themed lure and delivers a PDF attachment. The attachment `csWuYjyqO2IR.pdf` was identified as a valid PDF and contains a clickable external URL. Microsoft Defender detected the attachment as `Trojan:PDF/Phish!atmn`, while VirusTotal reported 23 of 63 security vendors detecting the file as malicious or suspicious. No evidence confirms user interaction, execution, or compromise.

## 3. Observed Evidence

### Sender

From:
`prestonconstance587@gmail.com`

Reply-To:
Not identified in the available artifact

Return-Path:
`prestonconstance587@gmail.com`

### Message

Subject:
`Liberação de IRPF - 6NwlyfzWcsNerv0`

Date:
`26 Jul 2023`

Message-ID:
Present in the original artifact

### Message Content

The message presents a financial themed lure and directs the recipient to obtain additional information from the attachment.

Observed body content includes:

`Saldo para crédito em conta.`

`Mais informações em anexo.`

A protocol number is also included in the message.

### Routing

The available Received headers show the message passing through Gmail infrastructure before delivery through Microsoft 365 infrastructure.

Observed Gmail server IP:
`209.85.160.178`

Observed IP in the authenticated SMTP connection:
`20.97.213.223`

These values are recorded as observed header data and are not treated as proof of malicious origin.

## 4. Authentication Analysis

SPF:
Pass

DKIM:
Pass

DMARC:
Pass

Authentication Results:
`spf=pass`, `dkim=pass`, `dmarc=pass`

Assessment:

The message passed SPF, DKIM, and DMARC for the Gmail sending domain. Successful authentication indicates that the message was authenticated for the sending domain, but it does not establish that the message content or attachment is legitimate.

## 5. Header Divergence

From:
`prestonconstance587@gmail.com`

Reply-To:
Not identified

Return-Path:
`prestonconstance587@gmail.com`

header.from:
`gmail.com`

smtp.mailfrom:
`gmail.com`

Assessment:

No From, Return-Path, or authentication domain mismatch was identified in the available artifact.

## 6. URL Analysis

Observed URL:

`hxxps://ookokoaksoa[.]z13[.]web[.]core[.]windows[.]net/`

Location:
Embedded within the PDF attachment

Handling:

The URL was recorded in defanged form and was not accessed during analysis.

Assessment:

The PDF contains a clickable external URL. Because the URL was not accessed, no claim is made about its live destination, redirect behavior, or current availability.

## 7. Attachment Analysis

Filename:
`csWuYjyqO2IR.pdf`

Content Type:
`application/pdf`

File Size:
97,566 bytes

Magic Bytes:
`%PDF-1.4`

SHA 256:
`cfc5fbc759dcc599c8329dd94f9364394c7b1e875d6ff515c7337e00fb1f30cf`

Microsoft Defender Detection:
`Trojan:PDF/Phish!atmn`

Defender Execution Status:
`DidThreatExecute: False`

Assessment:

The email contains a valid PDF attachment with an embedded external URL. Microsoft Defender detected the attachment as `Trojan:PDF/Phish!atmn` and automatically removed the extracted file from the analysis environment.

The attachment was not executed during analysis.

## 8. Threat Intelligence Enrichment

### VirusTotal

Lookup Method:
SHA 256 hash lookup

Lookup Indicator:
`cfc5fbc759dcc599c8329dd94f9364394c7b1e875d6ff515c7337e00fb1f30cf`

Detection Result:
23 / 63 security vendors detected the file as malicious or suspicious

Evidence:

`evidence/virustotal-detection.png`

`evidence/virustotal-vendors.png`

Assessment:

VirusTotal provides independent reputation evidence that supports the malicious classification observed through Microsoft Defender.

The VirusTotal result is treated as supporting evidence rather than the sole basis for the verdict.

## 9. User Interaction

Interaction Status:
Unknown

No evidence in the available artifact confirms that a recipient opened the attachment, followed the embedded URL, or experienced account or endpoint compromise.

## 10. Scope

Scope Status:
Not available from the provided evidence

Recipient wide mailbox telemetry and endpoint telemetry were not available for this lab artifact.

No claim is made regarding additional recipients or organizational spread.

## 11. Impact Assessment

Potential Impact:

The attachment presents a phishing risk and may direct a recipient toward external malicious infrastructure.

Confirmed Impact:

No user interaction, execution, credential submission, or compromise was established from the available evidence.

Assessment:

The case demonstrates confirmed malicious email delivery, but victim impact remains unknown.

## 12. Verdict

Verdict:
Malicious

Assessment:

The malicious classification is supported by multiple independent signals:

1. The email uses a financial themed lure.
2. The message delivers a PDF attachment containing a clickable external URL.
3. Microsoft Defender classified the attachment as `Trojan:PDF/Phish!atmn`.
4. VirusTotal reported detections from 23 of 63 security vendors.
5. The attachment was not executed during analysis.

The available evidence therefore supports a malicious verdict without claiming confirmed compromise.

## 13. Severity Assessment

Severity:
High

Rationale:

The case involves confirmed malicious content delivered through email. The attachment has an associated external URL and received independent malicious detections from Microsoft Defender and VirusTotal.

Severity reflects the risk of the malicious delivery mechanism. It does not imply confirmed user impact or compromise.

## 14. Containment

Recommended Actions:

1. Quarantine the message.
2. Search for additional deliveries of the same attachment hash.
3. Block the attachment hash where technically supported.
4. Confirm whether any recipient interacted with the attachment or embedded URL.
5. Escalate if user interaction, execution, credential submission, or follow on activity is identified.

## 15. Remediation

Recommended Actions:

1. Review available email telemetry for additional recipients.
2. Review available endpoint telemetry for attachment interaction or execution.
3. Investigate any confirmed follow on phishing or credential activity.
4. Initiate account response only if evidence indicates credential submission or compromise.

## 16. Detection Opportunities

Potential Detection Opportunities:

1. Alert on email attachments matching a known malicious SHA 256.
2. Detect malicious or suspicious PDF attachments containing external URLs.
3. Correlate malicious attachment hash activity across multiple recipients.
4. Monitor for subsequent endpoint or identity activity following delivery of the attachment.

These are defensive detection opportunities derived from the investigation and are not claims that such detections were executed in this lab.

## 17. MITRE ATT&CK

Technique:
T1566.001: Spearphishing Attachment

Why:

The malicious content was delivered through an email attachment.

Evidence:

The message contains `csWuYjyqO2IR.pdf`, which was detected by Microsoft Defender as `Trojan:PDF/Phish!atmn`.

## Analyst Reasoning

The malicious attachment assessment is supported by the observed PDF attachment, its hash, the embedded external URL, and the Microsoft Defender detection. VirusTotal provides independent enrichment that further supports the assessment. No conclusion is made about user interaction, execution, credential submission, or compromise because those events were not established by the available evidence.

## Evidence Classification

- **OBSERVED:** PDF attachment metadata, SHA-256, and embedded URL from the email artifact.
- **ENRICHED:** Microsoft Defender detection and VirusTotal vendor results.
- **INFERRED:** Malicious attachment disposition based on the totality of the available evidence.

## 18. Evidence References

Original Email:
the original `sample.eml` retained in the local forensic workspace

Email SHA 256:
`4D57534EEB97D11E8D63595DFFB222512666E69923C56F55215AF9FC817C4FD6`

Attachment:
`csWuYjyqO2IR.pdf`

Attachment SHA 256:
`cfc5fbc759dcc599c8329dd94f9364394c7b1e875d6ff515c7337e00fb1f30cf`

Attachment Hash Evidence:
`evidence/hashes.txt`

Defender Evidence:
`evidence/defender-detection.txt`

VirusTotal Summary:
`evidence/virustotal-result.txt`

VirusTotal Detection Screenshot:
`evidence/virustotal-detection.png`

VirusTotal Vendor Screenshot:
`evidence/virustotal-vendors.png`