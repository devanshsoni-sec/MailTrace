# PH-003: BEC / Executive Impersonation

## Case Metadata

| Field | Value |
|---|---|
| Case ID | PH-003 |
| Case Type | Business Email Compromise / Executive Impersonation |
| Initial Verdict | Malicious |
| Severity | High |
| Evidence Source | Provided email artifact |
| User Interaction | Unknown |
| Account Compromise | Not confirmed |
| Financial Loss | Not confirmed |

## Executive Summary

The email impersonates a company CEO and requests an urgent EUR 87,500 wire transfer to a new vendor. The message uses a mismatched Reply-To address and fails SPF, DKIM, and DMARC authentication, strongly indicating sender impersonation. The request also uses urgency, confidentiality, and a claim that the executive is unavailable to avoid normal verification. No evidence in the provided artifact confirms that the transfer was completed or that an account was compromised.

## Observed Evidence

The message identifies the sender as:

`ceo.johnson@yourcompany-corp.net`

The recipient is:

`cfo@yourcompany.com`

The Reply-To address is:

`ceo.johnson@gmail.com`

The Reply-To address differs from the claimed corporate sender identity.

The subject is:

`Urgent wire transfer needed today`

The email requests an urgent EUR 87,500 wire transfer to a new vendor and provides Deutsche Bank and an IBAN as payment details.

The message instructs the recipient not to discuss the request with anyone else and describes the request as confidential.

## Authentication Analysis

The provided Authentication-Results header records:

- SPF: fail
- DKIM: fail
- DMARC: fail

These authentication failures conflict with the claimed corporate sender identity and support the assessment that the message is impersonating the claimed executive.

## Header Divergence

The visible From address claims the sender is using the corporate domain:

`ceo.johnson@yourcompany-corp.net`

The Reply-To address points to an external Gmail account:

`ceo.johnson@gmail.com`

This divergence is a significant BEC indicator because replies may be directed to an external account outside the organization's expected email infrastructure.

## Business Context and Social Engineering

The message requests a high-value financial transaction to a new vendor and emphasizes immediate action.

The sender claims to be in a board meeting and unable to talk. This creates pressure while discouraging direct verification.

The instruction to keep the request confidential is another social engineering indicator intended to bypass normal approval and verification procedures.

## Threat Intelligence Enrichment

No external threat intelligence enrichment was performed because the provided artifact contains no URL or attachment requiring enrichment.

## User Interaction

User interaction is not present in the provided evidence.

There is no evidence confirming that the recipient replied, followed the instructions, initiated the transfer, or disclosed credentials.

## Scope

The provided artifact does not contain mailbox telemetry, endpoint telemetry, authentication logs, financial transaction records, or evidence of additional affected users.

The scope of the incident cannot therefore be determined from this artifact alone.

## Impact Assessment

The requested transaction is financially significant and represents a potential direct financial loss.

No evidence confirms that the requested transfer was completed.

No evidence confirms account compromise, credential theft, malware execution, or unauthorized mailbox access.

## Verdict

**Malicious: BEC / Executive Impersonation**

The combination of executive impersonation, failed SPF/DKIM/DMARC authentication, Reply-To divergence, urgent financial instructions, a new vendor payment request, and confidentiality language provides sufficient evidence to classify the message as a malicious BEC attempt.

## Severity Assessment

**High**

The attempted transaction involves EUR 87,500 and could result in significant financial loss if the request were acted upon.

## Containment

- Do not process the requested wire transfer.
- Preserve the original email and associated headers.
- Report the message to the security team.
- Search for additional messages using the sender address, Reply-To address, subject, and other identifying indicators.
- Verify the request through an independent trusted communication channel with the executive.

## Remediation

Strengthen financial transaction verification procedures for requests involving new vendors or changes to payment details.

Require independent verification for high-value payment requests, particularly when urgency or confidentiality is emphasized.

Review email authentication configuration and monitoring for spoofing attempts.

Provide user awareness training focused on executive impersonation and payment fraud indicators.

## Detection Opportunities

Potential detection signals include:

- Corporate sender identity combined with an external Reply-To address.
- SPF, DKIM, or DMARC failures on messages claiming to originate from internal executives.
- High-value payment language such as wire transfer, urgent payment, or new vendor.
- Requests containing confidentiality or secrecy language.
- Messages impersonating executive or finance-related identities.

## MITRE ATT&CK

No ATT&CK technique is assigned to this case because the provided artifact does not contain sufficient evidence to support a specific technique mapping.

## Evidence References

1. `sample.eml`
2. Authentication-Results header contained in `sample.eml`
3. From / Reply-To divergence contained in `sample.eml`
4. Payment request and business context contained in `sample.eml`
5. `evidence/hashes.txt`