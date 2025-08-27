# Security Policy

## Supported Versions

Use this section to tell people about which versions of your project are
currently being supported with security updates.

| Version | Supported          |
| ------- | ------------------ |
| 5.1.x   | ✅                 |
| 5.0.x   | ❌                 |
| 4.0.x   | ✅                 |
| < 4.0   | ❌                 |

## Reporting a Vulnerability

**Preferred:** [Open a private security report on GitHub](../../security/advisories/new).  
This creates a private thread with the maintainers so we can triage and fix the issue before disclosure.

**Alternate:** Email **security@yourdomain.com** with the subject `Vulnerability Report: <project>`.  
(If you need encryption, include your PGP key or request ours.)

### What to include
- Affected version(s) and environment
- Impact and severity (how it could be exploited)
- Reproduction steps / proof of concept
- Any suggested fixes or mitigations
- Your contact info (for follow-up and credit)

### Our process & timelines
- **Acknowledgement:** within **48 hours**  
- **Triage & initial assessment:** within **5 business days**  
- **Status updates:** at least **every 7 days** until resolved  
- **Fix & release:** patch supported versions ASAP; advisories and release notes will document the fix  
- **Coordinated disclosure:** please don’t publish details until a fix is released and the advisory is public (target ≤ **90 days**, sooner for actively exploited issues)

### Safe Harbor
We will not pursue legal action for good-faith security research that:
- avoids privacy violations, data exfiltration, and service disruption (DoS),
- avoids social engineering or physical attacks,
- and limits testing to your own accounts/data.

If you’re unsure, contact us first—we’re happy to clarify scope.

### Out of scope (examples)
- Self-XSS or issues requiring victim-controlled input
- Clickjacking on pages without sensitive actions
- Rate-limit or brute-force findings without demonstrated impact
- Missing security headers without exploitable impact
- Duplicate reports or issues already known

### Credit & CVE
With your consent, we’ll credit you in the security advisory.  
If applicable, we’ll request a CVE through GitHub’s CNA program.
