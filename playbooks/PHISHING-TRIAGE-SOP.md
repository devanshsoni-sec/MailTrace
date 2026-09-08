\# Phishing Email Triage SOP



\## Purpose



This SOP defines a repeatable Security Operations Center workflow for investigating suspicious or user-reported phishing emails.



The objective is to determine whether an email is malicious, benign, or requires further investigation while preserving evidence, documenting analyst reasoning, and producing actionable containment and detection recommendations.



\## Scope



This procedure covers:



\- Credential phishing

\- Malicious attachments

\- Business Email Compromise and executive impersonation

\- QR phishing

\- Advanced credential and access phishing

\- Benign emails and false positives



The procedure is designed for SOC L1 style email triage and investigation.



\## Investigation Principles



\### Preserve the Original Artifact



The original email should be preserved before analysis.



Do not modify the original message during investigation.



Create working copies when transformations or extraction are required.



Record cryptographic hashes of preserved artifacts where practical.



\### Separate Evidence From Interpretation



Use three evidence categories:



\*\*OBSERVED\*\*



Information directly present in the original artifact or directly produced during controlled analysis.



\*\*ENRICHED\*\*



Information obtained from external sources such as reputation services, sandbox reports, DNS records, or other threat intelligence sources.



\*\*INFERRED\*\*



The analyst's conclusion based on the observed and enriched evidence.



Do not present inferred conclusions as directly observed facts.



\### Do Not Overstate Findings



Do not claim:



\- Credential submission without evidence.

\- Account compromise without evidence.

\- Malware execution without execution evidence.

\- Successful payment or financial loss without transaction evidence.

\- Session theft without evidence.

\- OAuth authorization without evidence.

\- Mailbox compromise without mailbox telemetry.

\- Redirect chains that were not observed.

\- Infrastructure ownership that was not established.



When evidence is unavailable, explicitly state:



`Not present in artifact`



or



`Not available from the provided evidence`



\## Standard Investigation Workflow



Suspicious Email



→ Evidence Preservation



→ Header Analysis



→ Sender and Authentication Analysis



→ URL Analysis



→ Attachment Analysis



→ QR Analysis when applicable



→ Threat Intelligence Enrichment



→ IOC Extraction



→ User Interaction Assessment



→ Scope Assessment



→ Impact Assessment



→ Analyst Reasoning



→ Verdict



→ Severity



→ Containment



→ Remediation



→ Detection Opportunities



→ Evidence Documentation



\## 1. Evidence Preservation



Preserve the original email artifact.



Record:



\- Original filename

\- File type

\- File size

\- SHA-256 hash



Where attachments are present, extract them using a controlled method without opening or executing them.



Record hashes for extracted evidence where appropriate.



Preserve useful supporting artifacts such as:



\- Relevant headers

\- URL analysis

\- Attachment metadata

\- Reputation results

\- Sandbox results

\- Screenshots of important evidence

\- IOC records



Do not collect unnecessary tool output.



\## 2. Initial Triage



Review the email for common phishing indicators:



\- Unexpected sender

\- Sender identity mismatch

\- Suspicious Reply-To address

\- Authentication failures

\- Urgency

\- Threats or pressure

\- Requests for credentials

\- Requests for financial transactions

\- Requests for account changes

\- Suspicious URLs

\- Suspicious attachments

\- QR codes

\- Unexpected authentication prompts

\- Executive impersonation

\- Requests for secrecy



Do not determine the verdict from a single indicator.



Assess the complete evidence set.



\## 3. Header Analysis



Review available:



\- From

\- Return-Path

\- Reply-To

\- To

\- Cc

\- Subject

\- Date

\- Message-ID

\- Received

\- Authentication-Results



Look for divergence between:



\- Display name and address

\- From and Reply-To

\- From domain and Return-Path

\- Claimed organization and actual sender infrastructure

\- Message origin and expected mail flow



Record relevant Received headers and source IP addresses when present.



Do not automatically treat an unfamiliar IP as malicious.



\## 4. Authentication Analysis



Review SPF, DKIM, and DMARC results when available.



\### SPF



Determine whether the sending host was authorized by the envelope sender domain.



\### DKIM



Determine whether the message signature validated and identify the signing domain.



\### DMARC



Determine whether the message aligned with the visible From domain and record the policy result when available.



Authentication results are evidence, not a complete verdict.



A legitimate message may fail authentication because of forwarding or infrastructure configuration.



A malicious message may pass authentication if an attacker controls a legitimate sending service or domain.



Interpret authentication together with the rest of the evidence.



\## 5. Sender Identity Analysis



Assess:



\- Display name

\- Email address

\- Domain

\- Reply-To

\- Organizational context

\- Known executive or finance identities

\- External lookalike domains

\- Unexpected free-mail addresses



Pay particular attention to:



\- Executive impersonation

\- Finance impersonation

\- IT support impersonation

\- Vendor impersonation

\- Authentication service impersonation



\## 6. URL Analysis



Never open a suspicious phishing URL directly from the original message during normal triage.



Extract URLs safely.



Preserve:



\- Original URL

\- Defanged URL

\- Domain

\- Host

\- Path

\- Query parameters

\- Redirect information when safely obtained from an appropriate analysis service



Defang URLs for public documentation.



Example:



`hxxps://example\[.]com/login`



Assess:



\- Domain legitimacy

\- Lookalike characteristics

\- Authentication or login paths

\- Suspicious URL parameters

\- URL shorteners

\- External hosting

\- Known phishing infrastructure

\- Redirect behavior when available through safe analysis



Do not claim live destination content unless it was actually observed.



\## 7. QR Phishing Analysis



When a QR code is embedded in an email:



1\. Preserve the original email.

2\. Extract the QR image locally.

3\. Calculate a hash of the extracted image where appropriate.

4\. Decode the QR code locally using a controlled method.

5\. Record the decoded URL.

6\. Defang the URL for documentation.

7\. Do not open the destination directly.

8\. Perform enrichment through appropriate safe analysis services when required.



Treat the QR payload as an equivalent phishing URL.



\## 8. Attachment Analysis



When an attachment is present:



Record:



\- Filename

\- Extension

\- MIME type

\- File size

\- Magic bytes when useful

\- SHA-256 hash



Do not execute the attachment during normal triage.



Use safe static inspection and trusted sandbox or reputation services when appropriate.



Record external enrichment separately from direct artifact observations.



If an endpoint security product removes or quarantines an extracted attachment, do not recreate the file merely to obtain additional evidence.



Document the security product detection instead.



\## 9. BEC and Executive Impersonation Analysis



For suspected BEC cases, evaluate:



\- Executive identity

\- Sender address

\- Reply-To

\- Authentication results

\- Business context

\- Financial request

\- New vendor request

\- Payment detail change

\- Urgency

\- Confidentiality language

\- Pressure to bypass normal approval

\- Request to avoid verification



A high-value financial request combined with executive impersonation and identity divergence should be treated as high risk.



Do not claim financial loss unless transaction evidence exists.



Recommended verification:



Use an independent trusted communication channel to confirm the request.



\## 10. Advanced Credential and Access Phishing



For advanced phishing, assess whether the evidence supports:



\- Adversary-in-the-Middle behavior

\- Microsoft 365 authentication targeting

\- OAuth-related phishing

\- Device-code phishing

\- Session access

\- Browser fingerprinting

\- Authentication page impersonation

\- Session cookie theft



Do not automatically equate a campaign label with successful compromise.



A sandbox report can establish observed malicious behavior, but successful credential submission, session theft, or account compromise must be supported by evidence before being stated as fact.



\## 11. Threat Intelligence Enrichment



Use external enrichment when it provides useful evidence.



Potential sources include:



\- URL reputation

\- File reputation

\- Domain reputation

\- Sandbox analysis

\- DNS information

\- Malware analysis reports



Record:



\- Source

\- Indicator

\- Result

\- Relevant detection

\- Date of analysis when available



Threat intelligence should support analyst reasoning rather than replace it.



Do not write:



`The tool says malicious, therefore malicious.`



Instead explain how the enrichment relates to the observed evidence.



\## 12. User Interaction Assessment



Determine whether the evidence shows:



\- Email opened

\- URL clicked

\- QR code scanned

\- Attachment opened

\- Credentials entered

\- Authentication completed

\- OAuth consent granted

\- Payment initiated

\- Payment completed

\- Account compromise



If the available evidence cannot establish user interaction, record:



`User interaction: Unknown`



Do not infer interaction from message delivery alone.



\## 13. Scope Assessment



Determine whether evidence identifies:



\- Additional recipients

\- Additional messages

\- Additional endpoints

\- Additional accounts

\- Additional infrastructure

\- Related indicators

\- Campaign activity



If organizational telemetry is unavailable, explicitly state that broader scope cannot be determined.



\## 14. Impact Assessment



Assess the realistic consequences supported by the evidence.



Potential impacts include:



\- Credential exposure

\- Account takeover

\- Session compromise

\- Malware infection

\- Financial fraud

\- Data exposure

\- Business disruption



Distinguish:



\*\*Potential impact\*\*



from



\*\*Confirmed impact\*\*



Never present potential impact as confirmed compromise.



\## 15. IOC Extraction



Extract only useful investigation or detection indicators.



Potential IOC types:



\- Domains

\- URLs

\- IP addresses

\- Email addresses

\- File hashes

\- Attachment hashes

\- QR destinations



Defang malicious URLs and domains in public documentation.



Do not place unrelated artifact hashes into the central IOC feed unless they provide practical detection value.



Do not include benign case indicators as malicious IOCs.



\## 16. Verdict



Use one of the following primary dispositions:



\### Malicious



Evidence demonstrates a phishing or malicious activity.



\### Benign



Available evidence supports legitimate communication.



\### Suspicious / Further Investigation Required



Evidence is insufficient to make a confident malicious or benign determination.



The final verdict must be supported by multiple relevant indicators where possible.



\## 17. Severity



Suggested severity guidance:



\### Critical



Confirmed active compromise, significant financial loss, widespread impact, or highly privileged account compromise.



\### High



High-confidence malicious phishing with significant credential, financial, or access risk.



\### Medium



Credible malicious activity with limited demonstrated impact.



\### Low



Suspicious activity with limited risk or incomplete evidence.



\### Informational



Benign or low-risk activity that does not require incident response.



Severity should reflect demonstrated or reasonably supported risk rather than the presence of a single suspicious indicator.



\## 18. Containment



Containment actions depend on the case.



Potential actions include:



\- Do not interact with the message.

\- Preserve the original artifact.

\- Remove malicious messages from affected mailboxes.

\- Block malicious domains or URLs where appropriate.

\- Block malicious file hashes where supported.

\- Search for related messages.

\- Review affected users.

\- Review identity activity.

\- Reset credentials when compromise is suspected or confirmed.

\- Revoke sessions when compromise is confirmed.

\- Validate financial transactions independently.

\- Escalate confirmed incidents according to organizational procedure.



\## 19. Remediation



Potential remediation actions include:



\- Improve email authentication controls.

\- Strengthen phishing filtering.

\- Deploy phishing-resistant authentication where supported.

\- Improve payment verification procedures.

\- Improve executive impersonation controls.

\- Improve QR phishing detection.

\- Improve attachment analysis.

\- Improve identity telemetry.

\- Conduct targeted security awareness training.

\- Tune detections based on observed indicators.



\## 20. Detection Opportunities



Every malicious case should identify useful detection opportunities when practical.



Examples:



\- External Reply-To combined with corporate impersonation.

\- SPF, DKIM, or DMARC failures for executive identities.

\- Suspicious authentication-themed URLs.

\- QR phishing messages containing embedded images.

\- High-value payment language.

\- New vendor payment requests.

\- Malicious attachment hashes.

\- Known phishing domains.

\- Suspicious browser fingerprinting associated with authentication phishing.

\- Authentication anomalies following phishing exposure.



Detection opportunities should be realistic and actionable for a SOC environment.



\## 21. MITRE ATT\&CK Mapping



Assign ATT\&CK techniques only when the evidence supports the mapping.



Do not force a technique into a case merely because the technique could theoretically apply.



A case may legitimately contain:



`No ATT\&CK technique assigned`



when the available evidence does not support a defensible mapping.



\## 22. Evidence References



Every investigation report should identify the supporting evidence.



Typical references:



1\. Original email artifact

2\. Header evidence

3\. Attachment evidence

4\. URL analysis

5\. QR analysis

6\. Threat intelligence results

7\. Sandbox analysis

8\. Hash records

9\. Relevant screenshots



Use filenames that correspond to the repository evidence structure.



\## 23. Evidence Quality Rules



\### OBSERVED



Use for facts directly present in the artifact.



Examples:



\- Subject line

\- Sender address

\- Reply-To

\- Authentication result

\- Attachment name

\- QR decoded value



\### ENRICHED



Use for facts obtained from external analysis.



Examples:



\- VirusTotal detections

\- Sandbox verdict

\- DNS result

\- Reputation result



\### INFERRED



Use for analyst conclusions.



Examples:



\- Likely credential phishing

\- Likely executive impersonation

\- High-risk BEC attempt

\- Benign communication



Do not mix the three categories without identifying the source.



\## 24. Analyst Quality Check



Before closing a case, confirm:



\- Original artifact preserved.

\- SHA-256 recorded.

\- Relevant headers documented.

\- Sender identity assessed.

\- Authentication assessed where available.

\- URLs handled safely.

\- Attachments handled safely.

\- QR codes handled safely when applicable.

\- External enrichment clearly identified.

\- User interaction stated accurately.

\- Scope stated accurately.

\- Impact distinguished from potential impact.

\- Verdict supported by evidence.

\- Severity justified.

\- Containment documented.

\- Remediation documented.

\- Detection opportunities identified.

\- Unsupported claims removed.

\- Evidence references are complete.



\## 25. Public Repository Safety



Before publishing the project:



\- Defang live malicious URLs and domains.

\- Do not publish active credentials or secrets.

\- Do not publish personal information unnecessarily.

\- Do not execute malicious files.

\- Do not publish unnecessary malicious infrastructure details.

\- Review screenshots for sensitive information.

\- Remove unnecessary tool logs.

\- Clearly distinguish external enrichment from original evidence.



The public repository should demonstrate investigation capability without unnecessarily increasing operational risk.
