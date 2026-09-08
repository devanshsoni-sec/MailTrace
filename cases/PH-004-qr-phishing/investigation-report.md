# PH-004: QR Phishing

## Case Metadata

| Field | Value |
|---|---|
| Case ID | PH-004 |
| Case Type | QR Code Phishing |
| Initial Verdict | Malicious |
| Severity | High |
| Evidence Source | Provided email artifact and embedded QR image |
| User Interaction | Unknown |
| Credential Submission | Not confirmed |
| Account Compromise | Not confirmed |

## Executive Summary

The email presents a Microsoft-themed MFA expiry notification and uses an embedded QR image to direct the recipient toward an authentication-themed destination hosted on an external domain. The QR code was extracted from the original email and decoded locally, revealing an external URL. The combination of an authentication lure, embedded QR code, and external login destination is consistent with a QR phishing attempt targeting user credentials. No evidence in the provided artifact confirms that the recipient scanned the QR code, submitted credentials, or experienced account compromise.

## Observed Evidence

The original message contains the following sender and recipient information:

**From:**

`"Tyrell Corp Exchange Settings" <tyrellcorp@mfa-settings-secure.onmicrosoft.com>`

**To:**

`"Kenny Suarez" <kenny.suarez@tyrellcorp.com>`

**Subject:**

`MFA Expiry | Tyrell Corp Multi-Factor Auth`

The message contains an embedded image:

`refresh.png`

The extracted image was preserved as:

`evidence/qr-code.png`

The QR image was successfully decoded locally.

## Header Analysis

The provided email contains multiple Received headers showing the following mail path:

`internal-mx.company.com [10.0.1.50]`

`relay.emailprovider.net [198.51.100.75]`

`smtp.sender.org [203.0.113.25]`

The available artifact does not contain a complete authentication verdict for SPF, DKIM, or DMARC.

No Reply-To header was present in the provided message header set.

The available header evidence is preserved for investigation context but does not independently establish that the listed mail infrastructure is malicious.

## QR Code Analysis

The embedded `refresh.png` image was extracted from the MIME message and preserved as:

`evidence/qr-code.png`

The QR code decoded successfully to the following destination:

`hxxps://files[.]delivrto[.]me/login/microsoft[.]html`

The URL was decoded locally but was not opened or accessed during the investigation.

## URL Analysis

The decoded destination uses the external domain:

`files[.]delivrto[.]me`

The path is:

`/login/microsoft.html`

The Microsoft-themed login path is consistent with an authentication phishing lure.

The available evidence does not establish the live content hosted at the destination because the URL was not accessed.

No redirect chain, page content, credential harvesting event, or successful authentication event was observed from the provided evidence.

## Threat Intelligence Enrichment

No external threat intelligence enrichment was required to establish the primary verdict because the email artifact and decoded QR destination provide sufficient evidence of a QR-based phishing attempt.

No external reputation result is claimed in this case.

## User Interaction

User interaction is unknown.

There is no evidence confirming that the recipient scanned the QR code, opened the resulting destination, entered credentials, or authenticated to an attacker-controlled service.

## Scope

The provided artifact contains a single email and its embedded QR image.

No mailbox telemetry, endpoint telemetry, identity provider logs, authentication events, or evidence of additional affected users was provided.

The broader incident scope therefore cannot be determined from this artifact alone.

## Impact Assessment

The message presents a potential credential theft risk by directing the recipient toward a Microsoft-themed login path hosted on an external domain.

Successful interaction could potentially result in credential disclosure or subsequent account compromise, but neither credential submission nor compromise is confirmed by the available evidence.

## Verdict

**Malicious: QR Phishing**

The email uses a Microsoft-themed MFA expiry lure and an embedded QR code that resolves to an external login path. The decoded destination and social engineering context provide sufficient evidence to classify the message as a malicious QR phishing attempt.

## Severity Assessment

**High**

The message presents a plausible credential theft vector targeting authentication information. The potential downstream impact includes unauthorized account access if a recipient were to submit valid credentials, although no such event is confirmed.

## Containment

- Do not scan the QR code or access the decoded destination.
- Preserve the original email and embedded image.
- Report the message to the security team.
- Search for additional messages containing the sender address, subject, QR destination domain, or related indicators.
- Block or monitor the identified destination domain where appropriate.
- Reset credentials and investigate authentication activity if user interaction is later confirmed.

## Remediation

Strengthen email filtering and user awareness controls for QR-based phishing messages.

Treat unexpected MFA expiry or account verification requests as suspicious and require verification through established organizational channels.

Monitor for QR phishing campaigns using external domains and authentication-themed subjects.

Review identity provider telemetry for suspicious authentication activity associated with affected recipients when applicable.

## Detection Opportunities

Potential detection signals include:

- MFA or account expiry themed messages containing embedded QR images.
- Microsoft-themed sender names using external or unexpected infrastructure.
- QR codes that resolve to non-corporate domains.
- Login or authentication language combined with embedded images.
- Messages directing users to externally hosted login paths.

## MITRE ATT&CK

**T1566.002: Phishing: Spearphishing Link**

The QR code provides a link-based phishing mechanism intended to direct the victim to an external authentication path.

## Evidence References

1. `sample.eml`
2. `evidence/headers.txt`
3. `evidence/qr-code.png`
4. `evidence/qr-analysis.txt`
5. `evidence/hashes.txt`

## Evidence Limitation

The phishing destination was not opened or accessed.

The available evidence does not establish credential submission, successful authentication, account compromise, malware execution, or broader campaign scope.