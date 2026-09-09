# PH-001: Credential Phishing

## Case Metadata

| Field | Value |
|---|---|
| Case ID | PH-001 |
| Case Type | Credential Phishing |
| Initial Verdict | Malicious |
| Severity | High |
| Evidence Source | Provided email artifact |
| User Interaction | Unknown |
| Credential Submission | Not confirmed |
| Account Compromise | Not confirmed |
| Financial Impact | Not indicated |

## Executive Summary

The email impersonates a Proton Mail helpdesk and presents a password expiry notification for the recipient. The claimed sender uses an unrelated external domain, while the available authentication results show SPF temporary failure, DKIM absent, and no DMARC policy evaluation. The HTML body contains a link to an external domain using a password and phishing themed path. These indicators support classification as a credential phishing attempt. No evidence confirms that the recipient clicked the link, submitted credentials, or experienced account compromise.

## Observed Evidence

The message identifies the sender as:

`"proton.me Helpdesk" <proton.me@medimovil.com.mx>`

The recipient is:

`phishing@pot`

The subject is:

`Password Expiry Notification for phishing@pot`

The message date is:

`18 May 2023 12:06:39 +0200`

The Message-ID is:

`<20230518120629.D7E6F3DC9B412CD0@medimovil.com.mx>`

The email uses a multipart MIME structure containing an HTML body.

The original email artifact SHA-256 is:

`22DB462F196BC63EDEDFA77617B01A783803889CF24AB7C865F212A61A7947A8`

## Authentication Analysis

The available Authentication-Results headers record:

- DMARC: none
- SPF: tempfail
- DKIM: none
- ARC: none

The claimed sender identity is:

`proton.me@medimovil.com.mx`

The sender address does not correspond to the Proton Mail brand presented in the display name.

The available authentication evidence therefore does not support the claimed Proton Mail identity.

## Header Divergence

The display name is:

`proton.me Helpdesk`

The actual sender address is:

`proton.me@medimovil.com.mx`

The sender domain is:

`medimovil.com.mx`

This domain does not correspond to the claimed Proton Mail identity.

The Received headers also show delivery involving infrastructure associated with:

`vps.vps.medimovil.com.mx`

and the source IP:

`185.189.112.27`

The available evidence therefore shows a mismatch between the impersonated brand and the observed sending infrastructure.

## URL Analysis

The HTML body contains the following observed URL:

`hxxps://mail[.]contianer[.]best/international[.]html?look=phishing@pot`

The destination uses an external domain unrelated to the claimed Proton Mail identity.

The path and query structure are consistent with a phishing workflow targeting a specific recipient.

The URL was extracted from the email artifact but was not opened or accessed during the investigation.

No redirect chain or live destination content was observed.

## Attachment Analysis

No file attachment requiring analysis was identified in the available email artifact.

## Threat Intelligence Enrichment

No external reputation lookup was performed for the observed URL or domain.

The primary malicious assessment is based on evidence directly present in the email artifact, including brand impersonation, sender domain mismatch, authentication anomalies, and the external phishing destination.

## User Interaction

User interaction is unknown.

There is no evidence confirming that the recipient clicked the phishing link, entered credentials, or completed authentication.

## Scope

The available evidence represents a single email artifact.

No mailbox telemetry, endpoint telemetry, identity provider logs, or evidence of additional affected recipients was provided.

The broader campaign or organizational scope therefore cannot be determined from this artifact alone.

## Impact Assessment

The email presents a credential theft risk by impersonating a trusted email provider and directing the recipient to an external authentication themed destination.

Potential impact includes credential disclosure and subsequent unauthorized account access.

No credential submission or account compromise is confirmed by the available evidence.

## Verdict

**Malicious: Credential Phishing**

The combination of Proton Mail impersonation, an unrelated sender domain, anomalous authentication results, and an external authentication themed URL provides sufficient evidence to classify the message as a malicious credential phishing attempt.

## Severity Assessment

**High**

The message directly targets account credentials through a trusted brand impersonation and a phishing URL.

Successful interaction could expose account credentials and potentially lead to unauthorized access.

No successful compromise is confirmed.

## Containment

- Do not access the phishing URL.
- Preserve the original email artifact.
- Report the message to the security team.
- Search for additional messages using the sender address, sender domain, subject, and phishing domain.
- Block or monitor the phishing domain where appropriate.
- Reset credentials if user interaction or credential submission is later confirmed.

## Remediation

Strengthen detection for brand impersonation and password expiry themed phishing messages.

Improve email filtering for suspicious external domains impersonating trusted authentication providers.

Monitor for phishing campaigns using authentication or password reset terminology.

Provide user awareness training focused on password expiry lures and suspicious login links.

## Detection Opportunities

Potential detection signals include:

- Trusted brand display names paired with unrelated sender domains.
- Password expiry or account access themed subjects.
- SPF failure or temporary failure combined with sender impersonation.
- Missing DKIM for messages claiming to originate from trusted providers.
- External authentication themed URLs.
- Domains unrelated to the impersonated organization.
- Query parameters containing recipient identifiers.

## MITRE ATT&CK

**T1566.002: Phishing: Spearphishing Link**

The email contains a malicious link designed to direct the recipient toward a credential phishing destination.

## Analyst Reasoning

The phishing assessment is based on the observed sender identity, authentication results, message path, and credential harvesting URL present in the original email artifact. DMARC returned **none** and SPF returned **tempfail**, while DKIM and ARC were not present. These values are authentication observations rather than standalone verdicts; the malicious assessment is based on the totality of the evidence.

## Evidence Classification

- **OBSERVED:** Sender identity, authentication results, Received headers, and phishing URL present in the original artifact.
- **ENRICHED:** External reputation or analysis results documented in the case evidence.
- **INFERRED:** Credential phishing verdict and associated risk assessment.

## Evidence References

1. Original `sample.eml` retained in the local forensic workspace; the raw artifact is intentionally excluded from the public repository.
2. `evidence/headers.txt`
3. `evidence/hashes.txt`
4. Observed phishing URL extracted from the HTML body

## Evidence Limitation

The investigation was performed using the available email artifact and controlled local parsing.

The phishing destination was not opened.

The available evidence does not establish credential submission, successful authentication, account compromise, malware execution, or broader campaign scope.