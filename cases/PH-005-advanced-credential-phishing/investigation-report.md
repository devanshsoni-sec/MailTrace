# PH-005: Advanced Credential / Access Phishing

## Case Metadata

| Field | Value |
|---|---|
| Case ID | PH-005 |
| Case Type | Advanced Credential / Access Phishing |
| Initial Verdict | Malicious |
| Severity | High |
| Evidence Source | Public ANY.RUN analysis of original email artifact |
| Original Artifact | `original (11).eml` |
| User Interaction | Sandbox browser activity observed; real user interaction not established |
| Credential Submission | Not independently confirmed from available evidence |
| Account Compromise | Not independently confirmed |
| Analysis Platform | ANY.RUN |

## Executive Summary

The analyzed email artifact was classified by ANY.RUN as **Sneaky 2FA**, an Adversary-in-the-Middle phishing kit targeting Microsoft 365 accounts. The sandbox recorded malicious phishing detections, Sneaky 2FA phishing kit detection, an email pattern in a URL fragment, and WebGL fingerprinting activity. The available evidence supports classification as an advanced Microsoft 365 credential and access phishing case, but the available artifact does not independently establish successful credential theft, session theft, or account compromise.

## Observed Evidence

The public analysis identifies the original artifact as:

`original (11).eml`

Artifact SHA-256:

`D8D3780B9E751673DEB6E91C9A91919BC205D17D8CB0C6C8D53389CE588DAC01`

MIME type:

`message/rfc822`

ANY.RUN classified the artifact with the verdict:

**Malicious activity**

Threat classification:

**Sneaky 2FA**

Relevant analysis tags include:

`sneaky2fa`

`oauth-ms-phish`

`phishing`

`phishing-ml`

`possible-phishing`

`fingerprinting`

`attachments`

`attc-eml`

`susp-attachments`

## Authentication Analysis

The raw email headers are not available in the acquired evidence set.

No SPF, DKIM, or DMARC result is therefore assigned to this case.

## Advanced Phishing Analysis

ANY.RUN identified the artifact as involving a **Sneaky 2FA phishing kit**.

Sneaky 2FA is an Adversary-in-the-Middle style phishing mechanism associated with Microsoft 365 credential and authentication targeting.

The analysis also contains the `oauth-ms-phish` tag, supporting the Microsoft authentication context of the campaign.

The available evidence does not independently establish that OAuth authorization was successfully granted, credentials were successfully submitted, session cookies were successfully stolen, or a victim account was compromised.

## Behavioral Evidence

The sandbox recorded the following relevant findings:

- Phishing detected by machine-learning analysis.
- Phishing detected by Suricata.
- Sneaky 2FA phishing kit detected.
- Email pattern detected in a URL fragment.
- WebGL fingerprinting detected.
- Microsoft Edge activity associated with the phishing workflow.
- Outlook was launched during the analysis.
- Environment values were read.
- Computer name information was read.
- Supported language information was checked.

These observations demonstrate a phishing workflow with browser-based interaction and fingerprinting behavior.

## Threat Intelligence Enrichment

The ANY.RUN public analysis serves as external enrichment for the original email artifact.

The analysis directly identifies the sample as malicious activity and associates it with Sneaky 2FA.

No additional reputation result is claimed beyond the evidence preserved in `evidence/anyrun-analysis.txt`.

## User Interaction

The sandbox analysis observed browser activity associated with the phishing workflow.

The available evidence does not establish whether a real user entered credentials or completed authentication.

No successful account compromise is confirmed.

## Scope

The available evidence represents analysis of one email artifact.

No organizational mailbox telemetry, endpoint telemetry outside the sandbox, identity provider logs, authentication records, or evidence of additional affected users was provided.

The broader incident scope therefore cannot be determined from the available evidence.

## Impact Assessment

An AiTM phishing workflow targeting Microsoft 365 authentication can create a credential and session access risk.

The available evidence supports classification of the email as a high-risk credential and access phishing attempt.

Successful credential theft, session theft, unauthorized access, or account compromise are not independently confirmed from the evidence available.

## Verdict

**Malicious: Advanced Credential / Access Phishing**

The public sandbox evidence identifies the artifact as a **Sneaky 2FA** phishing case and records multiple malicious phishing detections together with fingerprinting behavior. This is sufficient to classify the artifact as an advanced credential and access phishing attempt.

## Severity Assessment

**High**

The case targets Microsoft 365 authentication and uses an AiTM-style phishing mechanism. Successful victim interaction could potentially expose authentication material and enable unauthorized account access.

The available evidence does not confirm successful compromise.

## Containment

- Block or monitor identified phishing infrastructure where appropriate.
- Search for related messages using the original artifact indicators and campaign characteristics.
- Review identity provider logs for suspicious authentication activity involving potentially affected users.
- Investigate suspicious Microsoft 365 sessions if user interaction is confirmed.
- Reset affected credentials when compromise is suspected or confirmed.
- Revoke active sessions when account compromise is confirmed.

## Remediation

Strengthen phishing-resistant authentication controls where supported.

Increase detection coverage for Microsoft 365 phishing pages and AiTM-style authentication activity.

Monitor for anomalous authentication patterns associated with suspicious phishing campaigns.

Provide user awareness training focused on modern credential phishing and adversary-in-the-middle techniques.

Review identity telemetry for suspicious sign-ins, session anomalies, and unexpected authentication activity following phishing exposure.

## Detection Opportunities

Potential detection signals include:

- Microsoft 365-themed phishing campaigns.
- Sneaky2FA or AiTM-related indicators.
- Authentication phishing pages hosted outside expected organizational infrastructure.
- Suspicious URL fragments containing email or account patterns.
- Browser fingerprinting behavior associated with credential phishing.
- Phishing detections from network or email security controls.
- Suspicious authentication activity following exposure to a phishing email.

## MITRE ATT&CK

No ATT&CK technique is assigned to this case because the available public analysis does not provide sufficient direct evidence from the original email artifact to support a specific technique mapping.

## Analyst Reasoning

The available evidence supports an advanced credential and access phishing assessment based on the external sandbox findings. The analysis identifies phishing behavior and Sneaky 2FA characteristics, but the raw email artifact and endpoint or mailbox telemetry were not available for independent validation. No conclusion is made about credential submission, token theft, account compromise, or successful user interaction.

## Evidence Classification

- **OBSERVED:** No raw email artifact was directly available for independent inspection.
- **ENRICHED:** External ANY.RUN analysis, including reported phishing activity and Sneaky 2FA findings.
- **INFERRED:** Advanced credential and access phishing assessment based on the available evidence.

## Evidence References

1. `evidence/anyrun-analysis.txt`
2. `evidence/hashes.txt`
3. Public ANY.RUN analysis of `original (11).eml`
4. Original artifact SHA-256: `D8D3780B9E751673DEB6E91C9A91919BC205D17D8CB0C6C8D53389CE588DAC01`

## Evidence Limitation

The original `original (11).eml` artifact was not directly acquired from the public analysis interface.

The investigation therefore does not claim email header values, message body content, credential submission, session cookie theft, successful authentication, or account compromise unless independently supported by the available evidence.
